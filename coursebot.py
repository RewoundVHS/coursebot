#! /bin/python
import discord
from discord.ext import commands
import random

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
async def addcourse(ctx, *, course: str):
    metadata = course.split('\n')
    for data in metadata:
        data.lstrip()
    print(metadata)
    title = metadata[0]
    courseID = metadata[1].upper()
    description = metadata[2]
    difficulty = metadata[3]
    creator = metadata[4]
    if len(courseID) != 11:
        addedMessage = 'Invalid course ID length, not added.'
    else:
        addedMessage = 'Course ' + courseID + ' added!'
    await ctx.send(addedMessage)

@bot.command()
async def removecourse(ctx, *, courseID: str):
    # Make sure course ID is 11 characters long
    courseID = courseID.upper()
    removedMessage = 'Course ' + courseID + ' removed!'
    await ctx.send(removedMessage)

@bot.command()
async def randomcourse(ctx):
    await ctx.send('PL4-C3H-LDR')

bot.run('TOKEN')
