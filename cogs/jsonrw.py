import discord
import json
from discord.ext import commands

class Jsonmessages(commands.Cog):
  
  def __init__(self,bot):
    self.bot = bot
  
  @commands.command(hidden=True)
  @commands.is_owner()
  async def writemsg(self,ctx,value,*,content):
    with open('messages.json','r') as msg:
      message = json.load(msg)

    message[value] = content

    with open('messages.json','w') as msg:
      json.dump(message,msg,indent=4)

    await ctx.send(f"logged {{{value} : {content}}}")

  @commands.command(hidden=True)
  @commands.is_owner()
  async def readmsg(self,ctx,value):
    with open('messages.json','r') as msg:
      message = json.load(msg)

    content = message[value]
    await ctx.send(content)

  

def setup(bot):
  bot.add_cog(Jsonmessages(bot))      