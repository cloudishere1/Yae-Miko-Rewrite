import asyncpraw
import random
import os

from discord.ext import (commands,tasks)

reddit = asyncpraw.Reddit( client_id = os.environ['r_id'],
                      client_secret = os.environ['r_secret'],
                      username = os.environ['r_user'],
                      password = os.environ['r_pass'],
                      user_agent = "Yae_Miko")


"""Sends a random meme from r/genshin_memepact once every 3 hours"""


class Memes(commands.Cog):

  def __init__(self,bot):
    self.bot = bot
    self.meme.start()

  def cog_unload(self):
    self.meme.cancel()

  @tasks.loop(hours = 3, reconnect = True)
  async def meme(self):
    
    subreddit = await reddit.subreddit("genshin_memepact")
    meme_channel = self.bot.get_channel(888054325891461131)
    memes_list = []
    form = ["jpg","png"]
    check = False

    try:
      async for submission in subreddit.new(limit = 100):
        memes_list.append(submission)

    except asyncpraw.exceptions.PRAWException as error:
      print(f"async praw error: {error}")

    except Exception:
      print("Bot error")

    while check == False:
      meme = random.choice(memes_list)
      y = str(meme.url)
      if y[-3:] in form:
        check = True

    await meme_channel.send(meme.url)

  @meme.before_loop
  async def before_printer(self):
    print('waiting...')
    await self.bot.wait_until_ready()

      
def setup(bot):
  bot.add_cog(Memes(bot))