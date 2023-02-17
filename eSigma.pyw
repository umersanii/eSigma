import asyncio
import discord
from discord.ext import commands
import random
import time
from librosa import get_duration


activity = discord.Activity(type=discord.ActivityType.listening, name="Nose to the Grindstone")


intents = discord.Intents.all()
client = commands.Bot(command_prefix="!", intents=intents, activity=activity, status=discord.Status.do_not_disturb)
denied = ["Access Denied: Insufficient Privileges.","IQ Requirements Not Met: Command Usage Unavailable."]
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


chanoool_v = 1014908772256337930
gen_v = 871666076885331972

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
    await user.send(random.choice(gifs)) 



@client.command()

async def p(ctx):
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
        while (True):
            file = "Y:\Python\DiscBot\mp3s.txt"
            fileback = "Y:\Python\DiscBot\mp3sback.txt"

            global one_from_grind
            with open(file,"r") as f:
                readog = f.read()
                grindlist = readog.split('\n')
                one_from_grind = random.choice(grindlist)
                ind =grindlist.index(one_from_grind)
                del grindlist[ind]
                grindstring = ' '.join([str(elem) for elem in grindlist])
                grindog = grindstring.replace( " ","\n")
            if grindog=="":
                with open(fileback,"r") as g:
                    readback = g.read()
                    grindbacklist = readback.split('\n')
                    grindbackstring = ' '.join([str(elem) for elem in grindbacklist])
                    grindbackog = grindbackstring.replace( " ","\n")
                    with open(file,"w") as g:
                        g.write(str(grindbackog))
            else:
                with open(file,"w") as f:
                    f.write(str(grindog))   
                    print('yeah')
            x = one_from_grind
            audio = "Y:\\discord\\" + x + ".mp3"
            print("Now Playing  " + x + "\n")
            vlen = get_duration(filename=audio)
            voiceChannel = discord.utils.get(ctx.guild.voice_channels, name="Chanoool")
            try:
                await voiceChannel.connect()
                voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
                    
                voice.play(discord.FFmpegPCMAudio(source = audio))
                await asyncio.sleep(vlen)
                await voice.disconnect()
                time.sleep(40)     
            except commands.errors.CommandInvokeError:
                voice.play(discord.FFmpegPCMAudio(source = audio))
                await asyncio.sleep(vlen)
                await voice.disconnect() 





client.run("MTA1NjIxMTI0NDIyNDM2MDQ0OA.GQ3n7L.ZD2txG6oFrTOGo2ln4CXLRO1oeqg36FWTx7-Ck")