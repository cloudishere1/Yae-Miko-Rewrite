import discord

from asyncio import sleep
from discord.ext import commands

"""Moderation commands
Permission: Ban member = True

-> ban
  -> Bans a user, doesn't needed to be in the server
-> cdban
  -> Bans a user after specified time(for fun)
"""

class Yaemod(commands.Cog):

  def __init__(self,bot):
    self.bot = bot

  @commands.command(name = "ban", help="bans a user", hidden = True)
  @commands.has_permissions(ban_members=True)
  async def ban(self, ctx, user: commands.UserConverter = None,*,reason = None):

    if user == None:
        await ctx.send(f"Specify the person to ban `{self.bot.command_prefix}ban <@user> <reason>`")
        return

    if ctx.author == user:
        await ctx.send("I cannot ban you.")
        return

    try:
      await ctx.guild.ban(user, reason=f'{reason} :banned by {ctx.author}')
      await ctx.send(f'{user} has been instantly banned, Reason: {reason}')

    except discord.Forbidden:
      await ctx.send("Unable to ban an administrator")    
      
    
  @ban.error
  async def ban_error(self,ctx,error):
    if isinstance(error, commands.UserNotFound):
      await ctx.send(error)
    
  @commands.command(name = "cdban", help = "bans a user after specified amount of time in seconds", aliases = ["countdownban", "timeban", "tb"], hidden = True)
  @commands.has_permissions(ban_members=True)
  async def cdban(self, ctx, user: commands.UserConverter = None, count: int = None,*,reason = None):

    if user == None:
        await ctx.send(f"Specify the person to ban `{self.bot.command_prefix}ban <@user> <reason>`")
        return

    if ctx.author == user:
        await ctx.send("I cannot ban you.")
        return

    msg = await ctx.send(
        f'Banning {user.mention} in {count}, Reason: {reason}')

    while count:
        await sleep(1)
        count -= 1
        await msg.edit(
            content=f'Banning {user.mention} in {count}, Reason: {reason}')

    await sleep(1)
    
    try:
      await ctx.guild.ban(user, reason=f'{reason} :banned by {ctx.author}')
      await msg.edit(content = f'Get out of here! <:YaeFeet:852664359696072734>')
      await sleep(1)
      await ctx.send(f'{user} has been banned, Reason: {reason}')

    except discord.Forbidden:
      await ctx.send("Unable to ban an administrator")    
      
  @cdban.error
  async def tban_error(self,ctx,error):

    if isinstance(error, commands.UserNotFound):
      await ctx.send(error)

    elif isinstance(error, commands.BadArgument):
      await ctx.reply(f"Please input an integer on __count__ argument of the command. `{self.bot.command_prefix}tban [@user] [integer in seconds] <reason>`",delete_after = 5, mention_author = True)

  
def setup(bot):
  bot.add_cog(Yaemod(bot))