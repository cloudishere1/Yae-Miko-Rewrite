import logging
import datetime

from discord.ext import commands

class Error_Handler(commands.Cog):
  
  def __init__(self, bot):
    self.bot = bot 
    logging.basicConfig(filename = "error.log")
  

  @commands.Cog.listener()
  async def on_command_error(self,ctx: commands.Context,error: commands.CommandError):
    now = datetime.datetime.now()
    
    if isinstance(error, commands.CommandNotFound):
      pass

    elif isinstance(error, commands.MissingAnyRole):
      pass

    elif isinstance(error, commands.MissingPermissions):
      pass  
      
    elif isinstance(error, commands.ChannelNotFound):
      await ctx.send("Channel not found.")

    elif isinstance(error, commands.NotOwner):
      await ctx.send("Dev command only")

    elif isinstance(error, commands.CheckFailure):  
      await ctx.reply("Use this command in <#888053481007611966>.")

    elif isinstance(error, commands.MessageNotFound):
      await ctx.send(f"Message does not exist or was deleted.") 
    
    else:
      logging.error(f'\n {error} - {now} \n')
      print("Error was logged in error.log.")
      #logs the error not specified in exception for further analysis
      



def setup(bot):
  bot.add_cog(Error_Handler(bot))      