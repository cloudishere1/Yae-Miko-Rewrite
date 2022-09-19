import discord
from discord.ext import commands

class April(commands.Cog):

  def __init__(self,bot):
    self.bot = bot
  

  @commands.command(hidden = True)
  
  async def aprilfools(self,ctx):
    meraki = ctx.guild.get_member(273107876300718081)
    #cloud = ctx.guild.get_member(206784694094790656)
    nano = ctx.guild.get_member(132916831425003521)
    ari = ctx.guild.get_member(226092067737174026)
    peach = ctx.guild.get_member(393169573417058306)
    inacia = ctx.guild.get_member(440723536814800899)
    nayde = ctx.guild.get_member(308058048289570817)
    frigid = ctx.guild.get_member(454721011946881046)
    dubby = ctx.guild.get_member(517820784702521345)
    keybears = ctx.guild.get_member(300487798161670144)
    previsible = ctx.guild.get_member(303934150673432576)
    vladdy = ctx.guild.get_member(371838805382135810)
    #rikku = ctx.guild.get_member(272466481273503747)

    await meraki.edit(nick="Brock")
    #await cloud.edit(nick="Sabrina")
    await nano.edit(nick="Volkner")
    await ari.edit(nick="Acerola")
    await peach.edit(nick="Malva")
    await inacia.edit(nick="Erika")
    await nayde.edit(nick="Cynthia")
    await frigid.edit(nick="Morty")
    await dubby.edit(nick="Akari")
    await keybears.edit(nick="Whitney")
    await previsible.edit(nick="Lance")
    await vladdy.edit(nick="Misty")
    #await rikku.edit(nick="Lorelei")

def setup(bot):
  bot.add_cog(April(bot))