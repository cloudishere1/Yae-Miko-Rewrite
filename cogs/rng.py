import discord
import random
import artifactsim

from discord.ext import commands

"""fun commands for playing with RNG
Permission: everyone

-> rps
  -> rock paper scissor simulator
-> flip
  -> flip a coin
-> artifact (flower,feather,sands,goblet,circlet)
  -> generates a random artifact
  -> artifact rng channel: 873402211131097158

"""

class Play(commands.Cog):

  def __init__(self,bot):
    self.bot = bot

  def artifact_channel(ctx):
    if ctx.channel.id == 873402211131097158:
      return True

  #janken simulator
  @commands.command(name ="rps", help = f"Rock paper scissor simulator command(!!rps r/p/s)")
  async def rps(self, ctx, choice :str = None ):
    
    if ctx.author == self.bot.user:
      return

    result = {"rock" : 1, 
              "paper" : 2, 
              "scissor" : 3, 
              "r" : 1, 
              "p" : 2, 
              "s" : 3}  

    lazy = ["👊","🖐️","✌️"]


    if choice == None:
      await ctx.send(f"No input was given. `{self.bot.command_prefix}rps <r/p/s>`")
      return
    

    if choice.lower() not in result.keys():
      await ctx.send(f"invalid input was given. `{self.bot.command_prefix}rps <r/p/s>`")
      return
    
    yae = random.choice(list(result.values()))
    you = result[choice.lower()]

    if yae == you:
      winner = "**draw.**<:YaeThink:866315816047738880>"

    if yae == 1:
      if you == 2:
        winner = "**You win!**<:YaeSad2:871040820088815646>"
      elif you == 3:
        winner = "**You lose.**<:YaeSmug:864328107812323328>"
      else:
        pass  
    elif yae == 2:
      if you == 1:
        winner = "**You lose.**<:YaeSmug:864328107812323328>"
      elif you == 3:
        winner = "**You win!**<:YaeSad2:871040820088815646>"
      else:
        pass  
    elif yae == 3:
      if you == 1:
        winner = "**You win!**<:YaeSad2:871040820088815646>"
      elif you == 2:
        winner = "**You lose.**<:YaeSmug:864328107812323328>"
      else:
        pass    
    else:
      return

    yae = lazy[yae-1]
    you = lazy[you-1]
    
    embed = discord.Embed(author = ctx.author.name,
        title = "Rock, Paper, Scissor", 
        description = f"Your pick: {you}\nMy pick: {yae}\n {winner}",
        colour = 0xB320B6)

    await ctx.reply(embed=embed)

  #coin toss simulator
  @commands.command(name = "flip", help = "flip a coin simulator")
  async def flip(self,ctx):
    if ctx.author == self.bot.user:
      return
      
    result = ["Heads", "Tails"]
    await ctx.reply(random.choice(result))  

  #Artifact RNG simulator
  @commands.command(name='feather',
             help='simulates the stat rolling of feather artifact')
  @commands.check(artifact_channel)               
  async def feather(self,ctx):

      await artifactsim.feather(ctx)

  @commands.command(name='flower',
              help='simulates the stat rolling of flower artifact')
  @commands.check(artifact_channel)                
  async def flower(self,ctx):

      await artifactsim.flower(ctx)

  @commands.command(name='sand', help='simulates the stat rolling of sand artifact')
  @commands.check(artifact_channel)    
  async def sands(self,ctx):

      await artifactsim.sand(ctx)

  @commands.command(name='goblet',
              help='simulates the stat rolling of goblet artifact')
  @commands.check(artifact_channel)                
  async def goblet(self,ctx):

      await artifactsim.goblet(ctx)

  @commands.command(name='circlet',
              help='simulates the stat rolling of circlet artifact')
  @commands.check(artifact_channel)                
  async def circlet(self,ctx):

      await artifactsim.circlet(ctx)

  @commands.command(name='artifact',
              help='generates one random artifact and simulate its stats',
              pass_context=True)
  @commands.check(artifact_channel)            
  async def artifact(self,ctx):

      rand = random.random()
      if rand < 0.2:
          await artifactsim.flower(ctx)
          return
      elif rand < 0.4:
          await artifactsim.feather(ctx)
          return
      elif rand < 0.6:
          await artifactsim.sand(ctx)
          return
      elif rand < 0.8:
          await artifactsim.goblet(ctx)
          return
      else:
          await artifactsim.circlet(ctx)
          return



def setup(bot):
  bot.add_cog(Play(bot))    
