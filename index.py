
import discord
from discord.ext import commands
import os

# Create bot instance with a command prefix
bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}.')

@bot.command()
async def join(ctx):
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("You need to be in a voice channel for me to join!")

@bot.command()
async def leave(ctx):
    if ctx.voice_client:
        await ctx.guild.voice_client.disconnect()
    else:
        await ctx.send("I'm not in a voice channel.")

@bot.command()
async def play(ctx, url: str):
    voice_client = ctx.voice_client
    if not voice_client:
        await ctx.send("I need to join a voice channel first!")
        return
    
    # Note: This requires additional setup for audio playback
    # You'll need to install FFmpeg and ytdl for this to work
    await ctx.send("Audio playback requires additional setup (FFmpeg, youtube-dl)")

@bot.command()
async def stop(ctx):
    voice_client = ctx.voice_client
    if voice_client and voice_client.is_playing():
        voice_client.stop()
        await ctx.send("Music stopped.")
    else:
        await ctx.send("No audio is currently playing.")

# Run the bot (token should be in environment variable for security)
if __name__ == "__main__":
    bot.run("***REMOVED***")
