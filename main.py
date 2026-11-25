import os
import json
import asyncio

import discord
import requests

from bs4 import BeautifulSoup

BOT_TOKEN = os.environ["DISCORD_BOT_TOKEN"]
CHANNEL_ID = int(os.environ["DISCORD_CHANNEL_ID"])
# USER_ID = int(os.environ["DISCORD_USER_ID"])

async def main():
    intents = discord.Intents.default()
    intents.message_content = True

    client = discord.Client(intents=intents)

    try:
        await client.login(BOT_TOKEN)
        channel = await client.fetch_channel(CHANNEL_ID)
        await channel.send("Test")
    finally:
        await client.close()

if __name__ == "__main__":
    asyncio.run(main())