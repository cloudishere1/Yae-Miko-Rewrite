import discord

from asyncio import sleep
from discord.ext import commands

"""Commands for yae miko bot to interact in chat
Permission: Shrine Chief, Cloud, Shrine Guard

->yae
  ->sends a message to a channel
->reply
  -> replies to a message
->edit
  -> edit her own message
->react  
  -> reacts to a message
->yaedm
  -> DMs a user
-slowsend
  -> Send a message on a channel one letter at a time  
"""

class Yae_Miko(commands.Cog):
  
  def __init__(self, bot):
    self.bot = bot 

  @commands.command(name='yae',
             help='Sends a message to a specific channel through the bot',
             hidden = True)
  @commands.has_any_role(761484787235946498, 852026036471463968,
                       761486609682006026)           
  async def yae(self, ctx, channel : commands.TextChannelConverter = None, *, message = None):
    
    if ctx.author == self.bot.user:
      return
    
    if message == None:
      await ctx.send(f"No message was given.")
      return

    await channel.send(message)
  
  @yae.error
  async def yae_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.send(f"Channel isn't specified.\n`{self.bot.command_prefix}yae [channel] <message>`")
      return

  @commands.command(
      name='edit',
      help='edits the specified message link, (can only edit the bot message)',
             hidden = True)
  @commands.has_any_role(761484787235946498, 852026036471463968,
                       761486609682006026)     
  async def edit(self, ctx, message_link: discord.Message, *, new_message=None):
    
    if new_message == None:
      await ctx.send("No message was given.")
      return

    await message_link.edit(content=new_message)

  @edit.error
  async def edit_error(self, ctx, error):
    if isinstance(error, commands.CommandInvokeError):
      await ctx.send(f"I cannot edit another user's message")
      return
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.send(f"Message was not specified.\n`{self.bot.command_prefix}edit [message link or message ID] <message>`")
      return  

  @commands.command(name='reply',
             help='replies to the specified message link',
             hidden = True)
  @commands.has_any_role(761484787235946498, 852026036471463968,
                       761486609682006026)     
  async def reply(self, ctx, message_link: discord.Message, *, message = None):
    
    if message == None:
      await ctx.send("No message was given.")
      return

    await message_link.reply(message)

  @reply.error
  async def reply_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.send(f"Message was not specified.\n`{self.bot.command_prefix}reply [message link or message ID] <message>`")
      

  @commands.command(name='react',
            help='Reacts to the specified message link with given reaction',
             hidden = True)
  @commands.has_any_role(761484787235946498, 852026036471463968,
                       761486609682006026)     
  async def react(self,ctx, message_link: discord.Message, emoji : commands.EmojiConverter = None):
    
    if emoji == None:
      await ctx.send("Please specify the emoji to react with.")
      return

    await message_link.add_reaction(emoji)

  @react.error
  async def react_error(self,ctx,error):
    
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.send(f"Message was not specified.\n`{self.bot.command_prefix}react [message link or message ID] <emoji>`")
      return

    if isinstance(error, commands.EmojiNotFound):
      await ctx.send("The given emoji does not exist in my list of useable emojis.") 
      return

  @commands.command(name = 'yaedm',
            help = "DMs a specified user with given message",
            hidden = True)
  @commands.has_any_role(761484787235946498, 852026036471463968,
                       761486609682006026)     
  async def yaedm(self, ctx, member : commands.MemberConverter, *, message = None):
    
    if message == None:
      await ctx.send("No message was given.")
      return

    try:
      channel = await member.create_dm()
      x = await channel.send(message)
      mailbox= self.bot.get_channel(874284953356099625)
      await mailbox.send(f"Message was sent to {member.mention}.\n**User ID**: {member.id}\n"
              f"**Content**: {message}\n"
              f"**Content ID**: {x.id}\n"
              f"**Invoked by**: {ctx.author.mention}")

    except discord.Forbidden:
      await ctx.send(f"Message was not sent, {member.mention}'s DM is closed")
    

  @yaedm.error
  async def yaedm_error(self, ctx, error):
    if isinstance(error, commands.MemberNotFound):
      await ctx.send(error)
      return

    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.send(f"Target user was not specified.\n`{self.bot.command_prefix}yaedm [@user/user ID] <message>`")
      return

  @commands.command(name = "slowsend", help = "Sends a message one letter at a time. (Character limit: 30)", hidden = True, aliases =["ss", "slow"])
  #@commands.has_any_role(761484787235946498, 852026036471463968,
  #                     761486609682006026)     
  async def slowsend(self,ctx,channel: commands.TextChannelConverter = None, *, message):
    
    message_split = message.split() #separate each words in a list
    emote_order = []
    loop = 0
    msg_store = ""

    #check if there's guild emoji in messages then replace them with thumbsup
    for emoji in ctx.guild.emojis:
      if str(emoji) in message:
        message = message.replace(str(emoji),"👍")

    #check if the character exceeded 30 because it is 1 letter per second
    if len(message) > 30:
      await ctx.send(f"30 character limit exceeded, character count: {len(message)}")
      return

    #if the emotes is found in the guild, store them to emote_order list to get the order of each emote
    for items in message_split:
      for emotes in ctx.guild.emojis:
        if str(items) == str(emotes):
          emote_order.append(items)

    #for each letter, send one letter and then edit to next
    for letter in message:
      if letter == "👍":
        letter = emote_order[0] #replace the thumbsup back to the emoji so that it gets sent as a whole
        del emote_order[0] #remove them from the list
      loop += 1
      msg_store += letter
      if letter == " ": #if space is found, skip to the next iteration and go to next letter
        continue

      if loop == 1: #send it at start
        msg = await channel.send(msg_store)
      else: #then edit it afterward
        await msg.edit(content = msg_store)
      await sleep(1)

  @slowsend.error
  async def slowsend_error(self,ctx,error):
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.send(f"Channel isn't specified.\n`{self.bot.command_prefix}slowsend [channel] <message>`")
    elif isinstance(error,commands.CommandOnCooldown):
      await ctx.send("**Command is still on cooldown**. Please try again after {:.0f} seconds".format(error.retry_after))

def setup(bot):
  bot.add_cog(Yae_Miko(bot))    
