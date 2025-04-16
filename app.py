import asyncio
import discord
from discord.ext import commands
import random
import os
import datetime
import sys
from content import *  # Import all constants from data.py
from bottoken import bot_token

# Initialize bot
is_playing = False
activity = discord.Activity(
    type=discord.ActivityType.streaming,
    name="the haunting reminder of past failures, bestowed upon me as a token of your unrelenting superiority."
)

intents = discord.Intents.all()
client = commands.Bot(command_prefix="!", intents=intents, activity=activity, status=discord.Status.do_not_disturb)
tree = client.tree

def ensure_path(path):
    """Normalize path and ensure directory exists"""
    path = os.path.normpath(path)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    return path

def get_audio_path(*parts):
    """Safe cross-platform path construction for audio files"""
    path = os.path.join(*parts)
    return ensure_path(path)

def log(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {str(message)}"
    with open("bot_errors.log", "a") as f:
        f.write(log_entry + "\n")
    print(log_entry)

def get_random_audio(file=None, directory_mp3s=None):
    """Get a random audio file from either a text list or directory"""
    if file and os.path.exists(file):
        with open(file, 'r') as f:
            lines = f.readlines()
            return random.choice(lines).strip()
    elif directory_mp3s and os.path.exists(directory_mp3s):
        files = [f for f in os.listdir(directory_mp3s) if f.endswith('.mp3')]
        if files:
            return os.path.join(directory_mp3s, random.choice(files))
    return None

async def play_audio(mem, audio):
    """Improved audio playback with robust error handling"""
    voice = None
    try:
        audio = get_audio_path(audio)
        if not os.path.exists(audio):
            raise FileNotFoundError(f"Audio file not found: {audio}")

        voice = discord.utils.get(client.voice_clients, guild=mem.guild)
        
        if not voice:
            if not mem.voice or not mem.voice.channel:
                return
            voice = await mem.voice.channel.connect()
        
        if voice.is_playing():
            voice.stop()

        ffmpeg_options = {
            'before_options': '-nostdin',
            'options': '-vn -loglevel quiet'
        }

        try:
            voice.play(discord.FFmpegPCMAudio(source=audio, **ffmpeg_options))
            log(f"Playing: {audio} (system FFmpeg)")
        except Exception as sys_err:
            log(f"System FFmpeg failed, trying local: {sys_err}")
            ffmpeg_path = get_audio_path(DEPENDENCIES_PATH, 
                                       "ffmpeg.exe" if sys.platform == "win32" else "ffmpeg")
            
            if os.path.exists(ffmpeg_path):
                if sys.platform != "win32":
                    os.chmod(ffmpeg_path, 0o755)
                voice.play(discord.FFmpegPCMAudio(
                    source=audio,
                    executable=ffmpeg_path,
                    **ffmpeg_options
                ))
                log(f"Playing: {audio} (local FFmpeg)")
            else:
                raise Exception(f"FFmpeg not found at {ffmpeg_path}")

        while voice.is_playing() and not voice.is_closed():
            await asyncio.sleep(0.1)
            
        if not voice.is_closed():
            await voice.disconnect()
            
    except Exception as e:
        log(f"Playback error: {str(e)}")
        if voice and not voice.is_closed():
            await voice.disconnect(force=True)
        raise

async def check_for_id(user_id):
    """Check for user-specific audio folder"""
    directory_path = get_audio_path(INOUTVC_PATH)
    if os.path.exists(directory_path):
        for dirname in os.listdir(directory_path):
            if str(user_id) in dirname:
                return dirname
    return None

@client.event
async def on_ready():
    await tree.sync()
    log(f"Synced slash commands for {client.user}")
    for guild in client.guilds:
        if guild.name in ["Chanoool", "privacy hoti ha"]:
            break

    log(f"{client.user} connected to {guild.name} (id: {guild.id})")
    user = client.get_user(sani)
    await user.send(f"{random.choice(copy)}\n{random.choice(gifs)}")

@client.event
async def on_voice_state_update(member, before, after):
    """Handle voice channel joins"""
    if member.bot:
        return

    # Only handle joins (not leaves or moves)
    if before.channel or not after.channel:
        return

    member_folder = await check_for_id(member.id) or "else"
    audio_file = get_audio_path(INOUTVC_PATH, member_folder, 
                              random.choice(os.listdir(get_audio_path(INOUTVC_PATH, member_folder))))

    try:
        voice_client = after.channel.guild.voice_client
        
        # Clean up any existing connection
        if voice_client:
            if voice_client.is_playing():
                voice_client.stop()
            await voice_client.disconnect(force=True)
            
        voice_client = await after.channel.connect()
        await play_audio(member, audio_file)
        
    except Exception as e:
        log(f"Voice join error: {str(e)}")

@tree.command(name="play", description="Play random audio in your voice channel")
async def play_command(ctx: discord.Interaction):
    global is_playing
    if is_playing:
        return await ctx.response.send_message("Already playing something!", ephemeral=True)
        
    denied_users = [aon, garv, ayan, mbot, gbot]
    if ctx.user.id in denied_users:
        channel = client.get_channel(dildya)
        await channel.send(f"{random.choice(denied)}\nhttps://tenor.com/bWHZB.gif")
        return await ctx.response.send_message("Access denied.", ephemeral=True)

    if not ctx.user.voice or not ctx.user.voice.channel:
        return await ctx.response.send_message("You need to be in a voice channel!", ephemeral=True)

    await ctx.response.send_message("Playing audio...", ephemeral=True)

    is_playing = True
    
    try:
        voice_client = ctx.guild.voice_client or await ctx.user.voice.channel.connect()
        
        while is_playing:
            audio = get_random_audio(
                file=get_audio_path(DEPENDENCIES_PATH, "mp3s.txt"),
                directory_mp3s=get_audio_path(RANDOMVC_PATH)
            )

            try:
                if voice_client.is_playing():
                    voice_client.stop()

                audio = audio.replace("\\", "/")
                voice_client.play(discord.FFmpegPCMAudio(source=audio))
                log(f"Now Playing: {audio}")

                while voice_client.is_playing() and is_playing:
                    await asyncio.sleep(0.1)

                await asyncio.sleep(random.randint(150, 250))

            except Exception as e:
                log(f"Playback error: {str(e)}")
                break

    except Exception as e:
        log(f"Command error: {str(e)}")

    finally:
        is_playing = False
        if ctx.guild.voice_client:
            await ctx.guild.voice_client.disconnect(force=True)

@tree.command(name="stop", description="Stop the audio playback")
async def stop(ctx: discord.Interaction):
    global is_playing

    if is_playing:
        is_playing = False
        await ctx.response.send_message("See Ya Chump!", ephemeral=True)

        if ctx.guild.voice_client:
            await ctx.guild.voice_client.disconnect(force=True)
    else:
        await ctx.response.send_message("No audio is playing right now.", ephemeral=True)

# Initialize required directories
required_dirs = [
    get_audio_path(DEPENDENCIES_PATH),
    get_audio_path(INOUTVC_PATH),
    get_audio_path(RANDOMVC_PATH)
]
for dir_path in required_dirs:
    os.makedirs(dir_path, exist_ok=True)

client.run(bot_token)