import discord
from discord.ext import tasks
from datetime import datetime 

TOKEN = "ODA4OTI1Nzc1OTk0MjkwMjM3.YCNo1g.lKAz63_rVsi5wRytNveRLiEAPaE"
CHANNEL_ID = 808919318359834624 
client = discord.Client()

@tasks.loop(seconds=60)
async def loop():
    # 現在の時刻
    now = datetime.now().strftime('%H:%M')
    if now == '16:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('テスト')  

loop.start()

bot.run(token)

