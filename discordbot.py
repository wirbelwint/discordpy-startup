from discord.ext import commands
import os
import traceback

import discord
from discord.ext import tasks
from datetime import datetime 


bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
CHANNEL_ID = 808919318359834624 
client = discord.Client()

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@tasks.loop(seconds=60)
async def loop():
    # 現在の時刻
    now = datetime.now().strftime('%H:%M')
    if now == '16:25':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('テスト')  

loop.start()

bot.run(token)

