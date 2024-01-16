import discord
from discord.ext import commands
from  bottoken import *
intents = discord.Intents.all()
intents.voice_states = True  
intents.messages = True 
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command(name='m')
async def mute_all(ctx):
    print('1')
    channel = ctx.author.voice.channel

    # Check if the bot has permission to mute and deafen members
    if not channel.permissions_for(ctx.guild.me).mute_members or not channel.permissions_for(ctx.guild.me).deafen_members:
        await ctx.send("I don't have the required permissions to mute and deafen members in this channel.")
        return

    # Mute and deafen all members in the voice channel
    for member in channel.members:
        if member.id == 693664844095946763:
            continue
        elif member.id == 787697488105570304:
            continue
        await member.edit(mute=True, deafen=True)


@bot.command(name='u')
async def unmute_all(ctx):
    channel = ctx.author.voice.channel

    # Check if the bot has permission to mute and deafen members
    if not channel.permissions_for(ctx.guild.me).mute_members or not channel.permissions_for(ctx.guild.me).deafen_members:
        await ctx.send("I don't have the required permissions to mute and deafen members in this channel.")
        return

    # Unmute and undeafen all members in the voice channel
    for member in channel.members:
        if member.id == 693664844095946763:
            continue
        elif member.id == 787697488105570304:
            continue
        await member.edit(mute=False, deafen=False)

bot.run(bot_token)