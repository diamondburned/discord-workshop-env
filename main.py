#!/usr/bin/env python3
import os

from dotenv import load_dotenv
from bot import bot


# Load the .env file, if it exists, so that os.getenv() can read the environment
# variable in it.
load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
if DISCORD_TOKEN is None:
    raise EnvironmentError("'DISCORD_TOKEN' is not set!")

# Run the bot with the token
bot.run(DISCORD_TOKEN)
