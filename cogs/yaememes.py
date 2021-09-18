import asyncpraw
import random
import os

from discord.ext import commands

reddit = asyncpraw.Reddit( client_id = os.environ['r_id'],
                      client_secret = os.environ['r_secret'],
                      username = os.environ['r_user'],
                      password = os.environ['r_pass'],
                      user_agent = "Yae_Miko")

class Memes(commands.Cog):

  def __init__(self,bot):
    self.bot = bot


  @commands.command()
  async def meme(self,ctx):
    
    subreddit = await reddit.subreddit("genshin_memepact")
    memes_list = []
    form = ["jpg","png"]
    print("wut")
    check = False
    try:
      async for submission in subreddit.new(limit = 25):
        memes_list.append(submission)

    except asyncpraw.exceptions.PRAWExcetion as error:
      print(f"async praw error: {error}")

    except Exception:
      print("Bot error")

    while check == False:
      meme = random.choice(memes_list)
      y = str(meme.url)
      if y[-3:] in form:
        check = True

    await ctx.send(meme.url)


      
def setup(bot):
  bot.add_cog(Memes(bot))