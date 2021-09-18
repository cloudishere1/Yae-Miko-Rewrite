import asyncpraw
import os
import time
#import asyncprawcore

"""Should be the reddit check, but it is still unstable
Permission: Admin"""

from discord.ext import commands
from asyncio import sleep

reddit = asyncpraw.Reddit( client_id = os.environ['r_id'],
                      client_secret = os.environ['r_secret'],
                      username = os.environ['r_user'],
                      password = os.environ['r_pass'],
                      user_agent = "Yae_Miko")

class Mikoshrine(commands.Cog):

  def __init__(self,bot):
    self.bot = bot

  
  @commands.command(hidden = True)
  @commands.has_permissions(administrator = True)
  async def yaemikoshrine(self,ctx):
    self.bot.loop.create_task(subredditcheck(ctx))

async def subredditcheck(self):
    subreddit = await reddit.subreddit("yaemikoshrine")
    print("checking subreddit:", subreddit)
    now = time.time()
    channel = self.bot.get_channel(834752769972764672)
    
    while True:
      try:
        async for submission in subreddit.stream.submissions(skip_existing = True):
            time_submitted = now - submission.created_utc
            if time_submitted <= 60:
              await channel.send(reddit.config.reddit_url + submission.permalink)
              await sleep(1)

      except asyncpraw.exceptions.PRAWException as e:
        await channel.send(f"async praw error: {e}")

      except Exception:
        await channel.send(f"Bot error")  


def setup(bot):
  bot.add_cog(Mikoshrine(bot))                          