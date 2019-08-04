#! /usr/bin/python3

import discord
from discord.ext import commands
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import random
import os

# Open spreadsheet using coursebot_credentials.json
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(os.getcwd() + '/coursebot_credentials.json', scope)
client = gspread.authorize(creds)
sheet = client.open('Smash Erie Mario Maker Courses').sheet1

description = '''A bot used to manage a Google Sheets spreadsheet of Super Mario
Maker 2 levels.'''
bot = commands.Bot(command_prefix='!')

# Print bot information
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    game = discord.Game('!cbhelp for command list')
    await bot.change_presence(activity=game)

# Help command, prints list of commands
@bot.command()
async def cbhelp(ctx):
    await ctx.send('`!cbadd` - Add a course to the spreadsheet in the following format: Title, Course ID, Description, Difficulty, Creator\n`!cbremove` - Remove a course corresponding to given ID from the spreadsheet\n`!cbrandom` - Prints a random course ID from the spreadsheet\n`!cblink` - Prints the link to the spreadsheet')

# Adds a course to the spreadsheet
@bot.command()
async def cbadd(ctx, *, course: str):
    # Split on newline characters
    metadata = course.split('\n')
    for data in metadata:
        data.lstrip()
    metadata[1] = metadata[1].upper()

    if len(metadata[1]) != 11:
        addedMessage = 'Invalid course ID length, not added.'
    else:
        if len(metadata) != 5:
            addedMessage = 'Invalid number of metadata fields!'
        else:
            sheet.insert_row(metadata, 2)
            print('Adding ' + metadata[1] + ' to spreadsheet')
            addedMessage = 'Course ' + metadata[1] + ' added!'
    await ctx.send(addedMessage)

# Removes a course from the spreadsheet
# Must have one or more of the following roles to run
@bot.command()
@commands.has_any_role('Mod Squad', 'Admin', 'Staff')
async def cbremove(ctx, courseID: str):
    courseID = courseID.upper().lstrip()

    if len(courseID) != 11:
        removedMessage = 'Invalid course ID length, could not remove.'
    else:
        # Try to find the course ID, continue if found
        try:
            cell = sheet.find(courseID)
            print('Course found at row ' + str(cell.row))
            print('Removing ' + courseID + ' from spreadsheet')
            sheet.delete_row(cell.row)
            removedMessage = 'Course ' + courseID + ' removed!'
        # If course ID not found, send an error message
        except gspread.exceptions.CellNotFound:
            removedMessage = 'Could not remove ' + courseID + ', course not found!'
    await ctx.send(removedMessage)

# Selects a random course ID from the spreadsheet
@bot.command()
async def cbrandom(ctx):
    print('Selecting random course ID')
    randID = sheet.cell(random.randint(2,sheet.row_count), 2).value
    await ctx.send(randID)

# Sends a link to the spreadsheet
@bot.command()
async def cblink(ctx):
    await ctx.send('SPREADLINK')

bot.run('TOKEN')
