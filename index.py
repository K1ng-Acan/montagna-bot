import discord
from discord.ext import commands
from pytube import YouTube
import os

# Create bot instance with a command prefix
bot = commands.Bot(command_prefix="!")

# Ensure bot has necessary permissions
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}.')

# Join voice channel
@bot.command()
async def join(ctx):
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("You need to be in a voice channel for me to join!")

# Leave voice channel
@bot.command()
async def leave(ctx):
    if ctx.voice_client:
        await ctx.guild.voice_client.disconnect()
    else:
        await ctx.send("I'm not in a voice channel.")

# Play music from YouTube
@bot.command()
async def play(ctx, url: str):
    voice_client = ctx.voice_client
    if not voice_client:
        await ctx.send("I need to join a voice channel first!")
        return

    # Download YouTube video as audio
    yt = YouTube(url)
    stream = yt.streams.filter(only_audio=True).first()
    output_file = stream.download(filename="song.mp3")

    # Play audio
    voice_client.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: print(f"Finished playing: {e}"))
    await ctx.send(f"Now playing: {yt.title}")

# Stop playing and clean up
@bot.command()
async def stop(ctx):
    voice_client = ctx.voice_client
    if voice_client.is_playing():
        voice_client.stop()
        os.remove("song.mp3")
        await ctx.send("Music stopped.")

# Run the bot with your token
bot.run("***REMOVED***")
