#! /bin/python

import discord
from discord.ext import commands
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import random

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('coursebot_credentials.json', scope)
client = gspread.authorize(creds)

sheet = client.open('Smash Erie Mario Maker Courses').sheet1

description = '''A bot used to manage a Google Sheets spreadsheet of Super Mario
Maker 2 levels.'''
bot = commands.Bot(command_prefix='!', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def cbhelp(ctx):
    await ctx.send('Placeholder help text')

@bot.command()
async def cbadd(ctx, *, course: str):
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

@bot.command()
@commands.has_role('Mod Squad')
@commands.has_role('Admin')
async def cbremove(ctx, courseID: str):
    courseID = courseID.upper()
    if len(courseID) != 11:
        removedMessage = 'Invalid course ID length, could not remove.'
    else:
        try:
            cell = sheet.find(courseID)
            print('Course found at row ' + str(cell.row))
            print('Removing ' + courseID + ' from spreadsheet')
            sheet.delete_row(cell.row)
            removedMessage = 'Course ' + courseID + ' removed!'
        except gspread.exceptions.CellNotFound:
            removedMessage = 'Could not remove ' + courseID + ', course not found!'
    await ctx.send(removedMessage)

@bot.command()
async def cbrandom(ctx):
    await ctx.send('PL4-C3H-LDR')

@bot.command()
async def cblink(ctx):
    await ctx.send('SPREADLINK')

bot.run('TOKEN')
