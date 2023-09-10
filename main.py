import asyncio
import discord
from discord.ext import commands
import random
from myfunctions import *
from bottoken import bot_token
import os

activity = discord.Activity(type=discord.ActivityType.streaming, name="the haunting reminder of past failures, bestowed upon me as a token of your unrelenting superiority.")

intents = discord.Intents.all()
client = commands.Bot(command_prefix="!", intents=intents, activity=activity, status=discord.Status.do_not_disturb)
copy = ["Overwatch, this is Task Force 141, requesting sitrep, over.",
"Viper Actual, this is Delta Force, ready for extraction, over.",
"Sandman, this is Rangers, prepare for assault, acknowledge.",
"Soap, this is Price, target acquired, awaiting orders, over.",
"Bravo Team, this is Metal 0-1, rally at LZ Bravo, copy?",
"Command, this is War Pig, requesting fire support, over.",
"Tango Company, this is Whiskey Delta, eyes on hostile movement, how copy?",
"Air Support, this is Reaper 3-1, initiating air-to-ground assault, over.",
"Team Sabre, this is SAS, objective secured, awaiting further orders, over.",
"Commander, this is Overlord, we are Oscar Mike, ready to neutralize the target, copy?"]


denied = ["Command Unavailable: IQ Threshold Unmet.",
"Intelligence Inadequate: Command Access Denied.",
"Insufficient IQ: Command Usage Unavailable.",
"IQ Requirements Unfulfilled: Command Restricted.",
"Command Denied: IQ Not Up to Par.",
"Access Rejected: IQ Insufficiency Detected.",
"Unauthorized: IQ Below Command Threshold.",
"Command Inaccessible: IQ Requirements Not Met.",
"Denied: IQ Insufficient for Command Usage.",
"Restricted Access: IQ Falls Short of Requirement.","IQ Requirements Not Met: Command Usage Unavailable."]
gifs = ["https://media.giphy.com/media/YlRpYzrkHbtSYDAlaE/giphy.gif","https://media.giphy.com/media/kwcRp24Wz4lZm/giphy.gif",
"https://media.giphy.com/media/kwcRp24Wz4lZm/giphy.gif","https://media.giphy.com/media/kwcRp24Wz4lZm/giphy.gif",
"https://media.giphy.com/media/eFxpuiAuG4nrPNCPEM/giphy-downsized-large.gif","https://media.giphy.com/media/eFxpuiAuG4nrPNCPEM/giphy-downsized-large.gif",
"https://giphy.com/clips/callofduty-call-of-duty-cod-modern-warfare-2-qJchEF3csHPGSFApHK",
"https://media.giphy.com/media/YNEHsd4m0MoIKWB3c6/giphy-downsized-large.gif","https://media.giphy.com/media/nGdTqgjljqZn3ahjlX/giphy.gif"]

ayan = 936149909818707968
aon = 851488467657818142
sani =693664844095946763
dildya = 790490721450459179
gen = 871666076885331971
eghost = 1067809005591859360
esigma = 1056211244224360448
koni = 787697488105570304
gbot = 783708073390112830
garv = 852844925677600818
echad = 1067411473313304596
mbot = 489076647727857685
qasim = 729631642544766997



async def play_audio(mem, audio):
    try:
        voice = discord.utils.get(client.voice_clients, guild=mem.guild)       
        try:
            voice.play(discord.FFmpegPCMAudio(source = audio, executable="data\\dependencies\\ffmpeg.exe"))
        except Exception as e:
            log("Error ha bhai"+e)
        log("playing")
        while voice.is_playing():
            await asyncio.sleep(1)
        await voice.disconnect()
    except Exception as e:
        try:
            log(e)
            pass
        except:
            pass



async def check_for_id(string):

    directory_path = 'data\\inoutvc'
    if os.path.exists(directory_path):
        directories = list_directories(directory_path)
        for directory in directories:
            if str(string) in directory:
                return directory
        return None    



@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == "Chanoool" or "privacy hoti ha":
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    user = client.get_user(sani)
    await user.send(random.choice(copy)+"\n"+random.choice(gifs))

@client.event
async def on_voice_state_update(member, before, after):
    if member.bot:
        return

    member_folder = await check_for_id(member.id)
    if member_folder == None:
        member_folder = "else"

    


    if before.channel is None and after.channel is not None:
        x = f"data\\inoutvc\\{str(member_folder)}\\" + fun(f"data\\inoutvc\\{str(member_folder)}")
        await after.channel.connect()

        try:
            await play_audio(member, x)
        except Exception as e:
            try:
                log(e)
                pass
            except:
                pass
                await play_audio(member, x)



@client.command()

async def p(ctx):
    global is_playing
    is_playing = True

    mem = ctx.message.author.id
    channel = client.get_channel(dildya)
    if mem == aon:
        await channel.send(random.choice(denied))
        await channel.send(("https://tenor.com/bWHZB.gif")) 
    elif mem == garv:
        await channel.send(random.choice(denied))
        await channel.send(("https://tenor.com/bWHZB.gif")) 
    elif mem == ayan:
        await channel.send(random.choice(denied))
        await channel.send(("https://tenor.com/bWHZB.gif")) 
    elif mem == mbot:
        await channel.send(random.choice(denied))
        await channel.send(("https://tenor.com/bWHZB.gif")) 
    elif mem == gbot:
        await channel.send(random.choice(denied))
    else:
        while is_playing:
            try:
                channel = ctx.author.voice.channel
                await channel.connect()

            except Exception as e:
                print(e)
                pass
            
            audio = get_random_audio(file = "data\\dependencies\\mp3s.txt", directory_mp3s = 'data\\randomvc')
            await play_audio(channel, audio)
            print("Now Playing  " + audio + "\n")
            time_wait = ['200', '150', '250']
            await asyncio.sleep(int(random.choice(time_wait)))   

            

@client.command()
async def f(ctx):   
    global is_playing
    if is_playing:
        is_playing = False
        await ctx.send("See Ya Chump!")

    else:
        pass



client.run(bot_token)