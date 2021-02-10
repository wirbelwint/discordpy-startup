import discord
import urllib.request
import json
import re
import os
from datetime import datetime, timezone, timedelta
from discord.ext import tasks

token = os.environ['DISCORD_BOT_TOKEN']
channel_id = 808919318359834624
client = discord.Client()
JST = timezone(timedelta(hours=+9), "JST")


# timer
@tasks.loop(seconds=60)
async def loop():
    now_time = datetime.now(JST).strftime("%H:%M")
            if now_time == "17:44":
            msg = "テスト"
            channel = client.get_channel(channel_id)
            await channel.send(msg)
            
        elif now_time == "23:00":
            msg = "テスト"
            channel = client.get_channel(channel_id)
            await channel.send(msg)
            
loop.start()
client.run(token)
