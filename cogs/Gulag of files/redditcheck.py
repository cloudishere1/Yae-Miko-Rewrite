import asyncpraw
import os
import time
import asyncprawcore

from discord.ext import (commands, tasks)
from asyncio import sleep

reddit = asyncpraw.Reddit( client_id = os.environ['r_id'],
                      client_secret = os.environ['r_secret'],
                      username = os.environ['r_user'],
                      password = os.environ['r_pass'],
                      user_agent = "Cloud_is_here")


class Reddit(commands.Cog):
  
  def __init__(self, bot):
    self.bot = bot 
    self.sub = None
    self.cnl = None
  
  
  #Start the subreddit check
  @commands.command()
  @commands.has_permissions(administrator=True)
  async def startcheck(self, ctx, subreddit: str = None, channel: commands.TextChannelConverter = None):
    
    if subreddit == None:
      await ctx.send("Please specify a subreddit to check.")
      return

    try: #check if subreddit exists
      check_sub = await reddit.subreddit(subreddit, fetch=True) 

    except asyncprawcore.Redirect: #raise an error if it doesn't exist
      await ctx.send(f"Subreddit {check_sub} doesn't exist.")
      return

    if channel == None:
      await ctx.send("Please specify on which channel to post.")  
      return
      
    if self.subredditstart.is_running() == True:
      await ctx.send(f'I am already checking the subreddit: __{self.sub}__  in {self.cnl.mention} and cannot invoke another instance of this command.')
      return  

    self.sub = await reddit.subreddit(subreddit)
    self.cnl = channel 
    self.subredditstart.start(ctx, subreddit,self.cnl,self.sub)

  #stops any case of is_running if an error occured
  @startcheck.error
  async def start_error(self,ctx,error):
    if isinstance(error, commands.MissingPermissions):
      pass
    else:
      self.subredditstart.cancel()
      print("this was invoked")

  #stop the subreddit check
  @commands.command()
  @commands.has_permissions(administrator=True)
  async def stopcheck(self, ctx):
    
    if self.sub == None:
      await ctx.send(f"I am not checking any subreddits right now")
      return

    else:
      await ctx.send(f"Stopped checking the subreddit: {self.sub}")
      self.sub = None
      self.cnl = None
      self.subredditstart.cancel()

  @tasks.loop(seconds = 60, reconnect = True)
  async def subredditstart(self, ctx, subreddit: str,cnl,sub):
    
    await ctx.send(f'I am now watching the subreddit: __{sub}__ and will post in {cnl.mention}')

    try:
      async for submission in sub.stream.submissions():
          now = time.time()
            
          time_submitted = now - submission.created_utc
          if time_submitted <= 60:
            await cnl.send(reddit.config.reddit_url + submission.permalink)
            await sleep(1)
      
    except:
      print("An unknown error has occured")
      self.sub = None
      self.cnl = None
      self.subredditstart.cancel()
      return
      
    cnl.send("The loop ended for some reason???")

def setup(bot):
  bot.add_cog(Reddit(bot))
  