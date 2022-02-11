import re
import urllib
import pafy
import discord
from discord.ext import commands
from discord import FFmpegPCMAudio, PCMVolumeTransformer
import requests
import ffmpeg
import youtube_dl
client = commands.Bot(command_prefix='$')
FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options': '-vn'}

queue = 0

isPlaying = False
@client.event
async def on_ready():
    print('Der Bot ist bereit!')

@client.command()
async def join(ctx):

    if(ctx.author.voice):
        channel = ctx.author.voice.channel
        await channel.connect()
    else:
        await ctx.send('Du befindest dich nicht in einem Voice-Channel!')

@client.command()
async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    if (voice):

        await voice.disconnect()
    else:
        await ctx.send('Du befindest dich nicht in einem Voice-Channel!')

@client.command(aliases=['p'])
async def play(ctx, arg):
    global url
    url = arg
    channel = ctx.message.author.voice.channel
    global player

    try:
        player = await channel.connect()
    except:
        pass


    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if isPlaying == False:
        try:
            voice.play(discord.FFmpegOpusAudio(executable='C:/users/vince/documents/ffmpeg/bin/ffmpeg.exe',
                                               source='http://' + url + '.skycharts-radio.eu/'))
        except:
            await ctx.send('Stream wurde nicht gefunden. Bitte benutze "**charts**" oder "**nightlife**".')

    else:
        await ctx.send('Bitte Skip diesen Stream mit %skip')

@client.command()
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    if voice.is_playing:
        voice.stop()
    else:
        await ctx.send("Der Bot Spielt Keine Musik")


@client.command()
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    if url != None:

        voice.play(discord.FFmpegOpusAudio(executable='C:/users/vince/documents/ffmpeg/bin/ffmpeg.exe', source='http://' + url + '.skycharts-radio.eu/'))

    else:
        await ctx.send("Du hast noch keine Musik angemacht")

@client.command()
async def skip(ctx):
    isPlaying == False
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    if voice.is_playing:
        voice.stop()
    else:
        await ctx.send("Der Bot Spielt Keine Musik.")

@client.command()
async def channel(ctx):


    if url != None:
        await ctx.send('Du hörst gerade "**#' + url + '**" zu')
    else:
        await ctx.send("Du hörst keinem Channel zu")


client.run('OTQxMDczNjExMTg2Mzk3MjQ0.YgQpGQ.sTHZWH_sbWSWZq-T5Kri8VTvSoQ')