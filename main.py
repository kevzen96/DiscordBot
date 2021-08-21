import discord
from discord.ext import commands
import youtube_dl




client = commands.Bot(command_prefix='#',intents = discord.Intents.all(),help_command=None)


        

@client.event
async def on_ready():
    print("The bot is now ready for use!")
    print("------------------------------")

#เมื่อมีคนเข้า bot แจ้งข้อความ
@client.event
async def on_member_join(member):
    channel = client.get_channel(876020893367820310)
    await channel.send("Welcome,to the server.🎉🎉")
    
@client.command()
async def hello(ctx):
    await ctx.send("สวัสดี ฉันคือ YoutubeBot 😀")

#คำสั่งเรียกบอทเข้าร่วมห้อง
@client.command(pass_context = True)
async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
        await ctx.send("Bot เข้าร่วมห้องเสียงแล้ว 😎")
    else:
        await ctx.send("คุณไม่ได้อยู่ในห้องเสียง❗")
#คำสั่งเตะบอทออกจากห้อง
@client.command(pass_context = True)
async def leave(ctx):
    if(ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("Bot ได้ออกจากห้องเสียงแล้ว 👋")
    else:
        await ctx.send("Bot ไม่ได้อยู่ในห้องเสียง❗")

#หยุดชั่วคราว
@client.command(pass_context = True)
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients,guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
        await ctx.send("Paused ⏸")
    else:
        await ctx.send("ขณะนี้ไม่มีเพลงเล่นในห้องเสียง!❗")
#เล่นเพลงต่อ
@client.command(pass_context = True)
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients,guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
        await ctx.send("Resume ⏯")
    else:
        await ctx.send("ขณะนี้ไม่มีเพลงที่กำลังหยุดชั่วคราว❗")
#หยุดเพลง
@client.command(pass_context = True)
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients,guild=ctx.guild)
    voice.stop()
    await ctx.send("Stop ⛔")
    
#เล่นเพลง
@client.command(pass_context = True)
async def play(ctx,url):
    ydl_opts = {'format': 'bestaudio'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    voice = ctx.voice_client

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
    voice.play(discord.FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
    voice.is_playing()



@client.command(pass_context = True) 
async def help(ctx):
    # help  hello play stop pause resume
    emBed = discord.Embed(title="Bot help", description="All available bot commands", color=0xff0040)
    emBed.add_field(name="#play", value="play music", inline=False)
    emBed.add_field(name="#stop", value="stop music", inline=False)
    emBed.add_field(name="#pause", value="pause music", inline=False)
    emBed.add_field(name="#resume", value="resume music", inline=False)
    emBed.set_thumbnail(url='https://i.imgur.com/oNgFWZ7.png')
    emBed.set_image(url='https://i.imgur.com/oNgFWZ7.png')
    await ctx.channel.send(embed=emBed)





client.run('TOKEN')