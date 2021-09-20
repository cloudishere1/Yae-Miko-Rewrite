from discord.ext import commands

class Assist(commands.Cog):
  
  def __init__(self,bot):
    self.bot = bot
    

  @commands.command(name="assist", help="Pings a helper role based on the channel, Cooldown = 10 minutes")
  @commands.cooldown(1,600, commands.BucketType.member)
  async def assist(self,ctx,uid = None, *, reason = "unspecified"):
      
    if ctx.author == self.bot.user:
      return

    check = False
    wl = "Unknown"

    helper_roles = { "america" : 889517957904994314,
                    "europe" : 889518004075913297,
                    "asia" : 889517911994171422,
                    "hk/tw/mo" : 889518084036132934}

    helper_channel = { "ch_america" : 889515011125420033,
                      "ch_europe" : 889514974920196106,
                      "ch_asia" : 889514959514521621,
                      "ch_hk/tw/mo" : 889515047682998282}     

    wl_roles = { "1" : 889515455939756045,
                "2" : 889515491847188602,
                "3" : 889515522893438996,
                "4" : 889515535283400765,
                "5" : 889515551095934976,
                "6" : 889515564291207239,
                "7" : 889515581462695986,
                "8" : 889515593982697592}

    if ctx.channel.id not in list(helper_channel.values()):
      await ctx.message.delete(delay = 5)
      await ctx.send(f'{ctx.author.mention} Please use this command in <#889506367709274172>.', delete_after = 5)
      self.assist.reset_cooldown(ctx)
      return

    if uid == None:
      await ctx.message.delete(delay=5)
      await ctx.send(f"{ctx.author.mention}, Please input your UID",delete_after = 5)
      self.assist.reset_cooldown(ctx)
      return

    if uid.isdigit() == False:
      await ctx.message.delete(delay =5)
      await ctx.send(f"{ctx.author.mention}, Please input a valid UID",delete_after = 5)
      self.assist.reset_cooldown(ctx)
      return

    if len(uid) != 9:
      await ctx.message.delete(delay=5)
      await ctx.send(f"{ctx.author.mention}, Please input a valid UID, length must be 9 characters",delete_after = 5)
      self.assist.reset_cooldown(ctx)
      return

    

    for items in list(wl_roles.values()):
      if check == True:
        break
      else:  
        for roles in ctx.author.roles:
          if items == roles.id:
            wl = [k for k, v in wl_roles.items() if v == items][0] #i dont understand this but this works
            check = True
            break
       
    if ctx.channel.id == helper_channel["ch_america"]:
      await ctx.send(f'<@&{helper_roles["america"]}>\n{ctx.author.mention} Needs help for __{reason}__.\n'
      f'**WL**: {wl}'
      f'**UID**: {uid}')

    elif ctx.channel.id == helper_channel["ch_europe"]:
      await ctx.send(f'<@&{helper_roles["europe"]}>\n{ctx.author.mention} Needs help for __{reason}__.\n'
      f'**WL**: {wl}'
      f'**UID**: {uid}')

    elif ctx.channel.id == helper_channel["ch_asia"]:
      await ctx.send(f'<@&{helper_roles["asia"]}>\n{ctx.author.mention} Needs help for __{reason}__.\n'
      f'**WL**: {wl}'
      f'**UID**: {uid}')

    elif ctx.channel.id == helper_channel["ch_hk/tw/mo"]:
      await ctx.send(f'<@&{helper_roles["hk/tw/mo"]}>\n{ctx.author.mention} Needs help for __{reason}__.\n'
      f'**WL**: {wl}'
      f'**UID**: {uid}')

    else:
      await ctx.message.delete()
      await ctx.send(f'{ctx.author.mention} Please use this command in <#889506367709274172>.', delete_after = 5)
      self.assist.reset_cooldown(ctx)

  @commands.command(hidden=True)
  @commands.is_owner()
  async def refresh(self,ctx):
    self.assist.reset_cooldown(ctx)
    
  @assist.error
  async def assist_error(self,ctx,error):
    if isinstance(error,commands.CommandOnCooldown):
      await ctx.send("**Command is still on cooldown**. Please try again after {:.0f} seconds".format(error.retry_after))

    elif isinstance(error,commands.BadArgument):
      await ctx.message.delete(delay =5)
      await ctx.send(f"{ctx.author.mention}, Please input a valid UID",delete_after = 5)
      self.assist.reset_cooldown(ctx)
   


def setup(bot):
  bot.add_cog(Assist(bot))