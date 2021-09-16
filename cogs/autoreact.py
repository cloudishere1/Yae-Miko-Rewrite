import discord
import random
import datetime

"""Autoreact and mailbox
->global yaewhat reaction 0.5% chance to trigger
->Yae's DM Mailbox (mailbox channel id: 888068697107869756)
->Yaepray reaction on yaepray in yaeshrine(yaeshrine channel id: 888052924662575104)
"""

from discord.ext import commands

class Auto_React(commands.Cog):
  
  def __init__(self, bot):
    self.bot = bot 

  @commands.Cog.listener()
  async def on_message(self,message):

    if message.author == self.bot.user:
      return

    #random yaewhat react 
    #if message.guild != None:
      #randx = random.random()
      #if randx < .005:
        #await message.add_reaction("<:YaeWhat:851097444350689360>") #need new yaewhat

    #Yae-Mailbox Embed
    if message.guild == None and message.author != self.bot.user:

      if message.content == "":
          return
      
      emb_colour = 0xB320B6
      emb_thumbnail = message.author.avatar_url
      emb_author = message.author
      member_id = message.author.id
      emb_description = message.content
    
      embed = discord.Embed(author = emb_author, 
        description = emb_description,
        colour = emb_colour
        )

      embed.set_author(name = emb_author, icon_url = emb_thumbnail)
      embed.set_footer(text= f"User ID:{member_id}")
      embed.timestamp = datetime.datetime.now()

      channel = self.bot.get_channel(888068697107869756)
      await channel.send(embed=embed)
      
      return

    #yaepray react on yaepray in yaeshrine
    if message.channel.id == 862324071579516929:
        if message.content.startswith("<:YaePray:888064916400001035>"):
            await message.add_reaction("<:YaePray:888064916400001035>")


def setup(bot):
  bot.add_cog(Auto_React(bot))