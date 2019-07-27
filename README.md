# Coursebot

### A helpful Discord bot used to manage a Google Sheets spreadsheet of Super Mario Maker 2 courses.

## Dependencies

Before running this bot you must have the ![discord.py](https://github.com/Rapptz/discord.py) package installed as well as gspread and oauth2client.

`python3 -m pip install -U discord.py gspread oauth2client`

## Commands

* !cbhelp - Displays a list of commands

* !cbadd - Adds a course to the spreadsheet

* !cbremove - Removes a course from the spreadsheet

* !cbrandom - Prints a random course ID from the spreadsheet

* !cblink - Prints the link to the spreadsheet

## Deploying this Discord Bot

* Create a new app: https://discordapp.com/developers/applications/

* In the `coursebot.py` file replace TOKEN with your app's token.

* Replace CLIENTID with your app's client ID in this URL and follow it: https://discordapp.com/oauth2/authorize?client_id=CLIENTID&scope=bot

* Create a new project at https://console.developers.google.com/

* Enable the Google Drive and Google Sheets APIs

* Create credentials, download the JSON file

* Place JSON file in same directory as `coursebot.py` script, rename it to `coursebot_credentials.json`

* Execute `coursebot.py` script.
