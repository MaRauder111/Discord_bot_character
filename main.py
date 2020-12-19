import discord
import os
from discord.ext import commands
from alive import keep_alive

client = commands.Bot(command_prefix='&')

#function to show bot has start up
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.command(pass_context=True)
async def hello(ctx):
  await ctx.send('hello')


@client.command(pass_context=True)
async def bobby(ctx):
  await ctx.send('Hello Noob Bobo SEA cancer!')

@client.command(pass_context=True)
async def ramu(ctx):
  await ctx.send('Subarashi Black Ram Medha gymer!')
  
@client.command(pass_context=True)
async def arbin(ctx):
  await ctx.send('Waifu Collector!')

@client.command(pass_context=True)
async def nicholas(ctx):
  await ctx.send('Dont call me Neehcholash and Cup noodles sponsor with Frooti!')
  
@client.command(pass_context=True)
async def padam(ctx):
  await ctx.send('The only legend bracket player in DOTA 2!')
  
@client.command(pass_context=True)
async def pradip(ctx):
  await ctx.send('Corona positive!')
  
@client.command(pass_context=True)
async def surji(ctx):
  await ctx.send('Thangapat best Mid Player!')

  
@client.command(pass_context=True)
async def daya(ctx):
  await ctx.send('All rounder!')

  
@client.command(pass_context=True)
async def avi(ctx):
  await ctx.send('Press recalibration and delete DOTA 2!')

  
@client.command(pass_context=True)
async def ashish(ctx):
  await ctx.send('Living in Detroit of Manipur Uripok!')

  
@client.command(pass_context=True)
async def somo(ctx):
  await ctx.send('Dieting every night but my weight is 99 Kg sad is lyf!')


@client.command(pass_context=True)
async def birjit(ctx):
  await ctx.send('Punjab best DOTA player!')

 
@client.command(pass_context=True)
async def anand(ctx):
  await ctx.send('Forever LP my lyf is LP!')
 
@client.command(pass_context=True)
async def aditya(ctx):
  await ctx.send('Jiri Drunker!')

 
@client.command(pass_context=True)
async def oson(ctx):
  await ctx.send('Phayeng lambo driver!')

 
@client.command(pass_context=True)
async def palbir(ctx):
  await ctx.send('Sala Malikum, Kaifr!')

#function call to keep the bot alive
keep_alive()
#hide the bot token which should not be shown to public
client.run(os.getenv('TOKEN'))