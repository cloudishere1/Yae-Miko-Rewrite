import os
import discord

from keep_alive import keep_alive
from discord.ext import commands

my_secret = os.environ['DToken']
intents = discord.Intents.default()
intents.members = True
owner = os.environ['DevID']
bot = commands.Bot(command_prefix='!!',
                  owner_id = int(owner),
                  intents=intents)

@bot.event
async def on_ready():
    print("Bot is now ready.")

@bot.command(hidden = True)
@commands.is_owner()
async def load(ctx, extension):
  bot.load_extension(f'cogs.{extension}')
  await ctx.send(f'Loaded {extension}')

@bot.command(hidden = True)
@commands.is_owner()
async def unload(ctx, extension):
  bot.unload_extension(f'cogs.{extension}')
  await ctx.send(f'Unloaded {extension}')

@bot.command(hidden = True)
@commands.is_owner()
async def reload(ctx, extension):
  bot.reload_extension(f'cogs.{extension}') 
  await ctx.send(f'reloaded {extension}')  
       
for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    bot.load_extension(f'cogs.{filename[:-3]}')
    print(f"loaded {filename}")
        
keep_alive()
bot.run(my_secret)