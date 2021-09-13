import discord
from discord.ext import commands

"""Change the presence status of the bot
Permission: Shrine chief, Cloud, shrine Guard

->Playing
->Watching
->Listening 
->streaming
->nostatus

"""

class Presence(commands.Cog):
  
  def __init__(self, bot):
    self.bot = bot

  @commands.command(name = "playing", help='Change the presence status to "Playing <something>', hidden = True)
  @commands.has_any_role(761484787235946498, 852026036471463968,
                       761486609682006026)    
  async def playing(self,ctx,*,game):  
    await self.bot.change_presence(activity=discord.Game(name=game))

  @commands.command(name = "watching", help='Change the presence status to "Watching <something>', hidden = True)
  @commands.has_any_role(761484787235946498, 852026036471463968,
                       761486609682006026)    
  async def watching(self,ctx,*,watch):
    await self.bot.change_presence(activity = discord.Activity(type=discord.ActivityType.watching, name=watch))
  
  @commands.command(name = "listening", help='Change the presence status to "Listening to <something>', hidden = True)
  @commands.has_any_role(761484787235946498, 852026036471463968,
                       761486609682006026)    
  async def listening(self,ctx,*,listen):
    await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=listen))
  
  @commands.command(name = "streaming", help='Change the presence status to "Streaming <game>', hidden = True)
  @commands.has_any_role(761484787235946498, 852026036471463968,
                       761486609682006026)    
  async def streaming(self,ctx,url, * , stream):
    await self.bot.change_presence(activity=discord.Streaming(name=stream, url=url))

  @commands.command(name = "nostatus", help='remove the presence status', hidden = True, aliases = ["nst","statusoff"])
  @commands.has_any_role(761484787235946498, 852026036471463968,
                       761486609682006026)    
  async def nostatus(self,ctx):
    await self.bot.change_presence(activity = None)  

  @commands.command(name = "ping", hidden = True, aliases=["latency"])
  @commands.has_permissions(administrator=True)
  async def ping(self,ctx):
    await ctx.send(f"beep boop... Latency: {round(self.bot.latency*1000)}ms")

def setup(bot):
  bot.add_cog(Presence(bot))        
