import discord
import random
import datetime
import asyncio

"""Autoreact and modmail
->global yaewhat reaction 0.5% chance to trigger
->Yaepray reaction on yaepray in yaeshrine(yaeshrine channel id: 888052924662575104)
->Yae's DM Mailbox (mailbox channel id: 888068697107869756)

-> Modmail will create a new private channel for people who dms the bot after confirming it

->!!mmreply -> reply to a modmail channel
->!!anon -> reply to a modmail channel anonymously
->!!close -> deletes the modmail channel
"""

from discord.ext import commands

class Mod_Mail(commands.Cog):
  
  def __init__(self, bot):
    self.bot = bot 
    self.authorlist = []

  @commands.Cog.listener()
  async def on_message(self,message):
    
    async def sendembed():
      attachment = message.attachments
      sticker = message.stickers

      emb_colour = 0xB320B6
      emb_thumbnail = message.author.avatar_url
      emb_author = message.author
      member_id = message.author.id
      emb_description = message.content + "\n\n Note: " + reacted_with 
    
      embed = discord.Embed(author = emb_author, 
        description = emb_description,
        colour = emb_colour
        )

      embed.set_author(name = emb_author, icon_url = emb_thumbnail)
      embed.set_footer(text= f"User ID:{member_id}")
      embed.timestamp = datetime.datetime.now()

      channel = self.bot.get_channel(888068697107869756)
      await channel.send(embed=embed)
      
      if message.attachments:
        for items in attachment:
          await channel.send(items.url)

      if message.stickers:
        for stuffs in sticker:
          await channel.send(stuffs.image_url)

    if message.author != self.bot.user:

      #Ko-fi logs stuff
      kofi_channel = self.bot.get_channel(951587462965235793)
      parsed_message = ""

      if message.content.startswith('{"message_id":'):
        if message.channel.id == 952430465053253642:
          msg_content = message.content.split(",")
          for msg_line in msg_content:
            msg_line = msg_line.replace('{',"")
            msg_line = msg_line.replace('}',"")
            parsed_message = parsed_message + msg_line + '\n'
  
          final_message = parsed_message.split("Sent via")
          await kofi_channel.send(final_message[0])
          
      #random yaewhat react 
      
      if message.guild != None:
        randx = random.random()
        if randx < .005:
          await message.add_reaction("<:YaeWhat:888079405514121237>")

      #yaepray react on yaepray in yaeshrine
      if message.channel.id == 888052924662575104:
          if message.content.startswith("<:YaePray:888064916400001035>"):
              await message.add_reaction("<:YaePray:888064916400001035>")

      #Yae-Modmail and mailbox
      if message.guild == None: #no guild = DM
        
        if message.content != "": #message is not blank
          
          author = str(message.author.id)

          if author not in self.authorlist:

            try: #respond to DM
              self.authorlist.append(author)
              modmail = await message.author.create_dm()

              mailembed = discord.Embed(author = "Modmail Request",
              description =  f"**__WARNING: If you do not have any concern, please press ❌ to cancel__**\n"
              f"**__Opening a modmail without any concern will result to an infraction__**\n\n"
    
              f"Hello there {message.author.mention}! You are about to send a message to the moderators. This will open a **private modmail** in __Yae Miko Mains | Genshin Impact server__.\n\n"

              f"If you just wish to send me a message, you can press ❤️ and i shall receive it!\n\n",
              colour = 0xFF99CC)

              mailembed.add_field(name= "Do you wish to open a modmail?", value = 
              f"Press ✅ to confirm\n"
              f"Press ❌ to cancel", inline = False)

              mailembed.title = "Modmail Request Prompt (timeout = 30s)"

              confirmation = await modmail.send(embed = mailembed)
              await confirmation.add_reaction("❤️")
              await confirmation.add_reaction("❌")
              await confirmation.add_reaction("✅")
  
              

            except discord.Forbidden:
              print("nope")  

            valid_reactions = ["✅","❌","❤️"]

            def check(reaction,user): #checks the reaction click
              return user == message.author and str(reaction.emoji) in valid_reactions

            try: 
              reaction, user = await self.bot.wait_for('reaction_add',timeout=30.0, check=check)


              if str(reaction.emoji) == "✅":
                await confirmation.remove_reaction("❌",self.bot.user)
                await confirmation.remove_reaction("❤️",self.bot.user)
                mailembed.title = "Confirmed ✅"
                mailembed.description = "Creating a modmail channel. Please wait."
                mailembed.clear_fields()
                await confirmation.edit(embed=mailembed) 

                yaeGuild = self.bot.get_guild(888052002368671804)
                modRole = yaeGuild.get_role(888055899694972950)
                bonkerRole = yaeGuild.get_role(889019983777124422)
                traineeRole = yaeGuild.get_role(889560780234719272)

                if "modmail" not in str(yaeGuild.channels): #check if category exists, if not, create one
                  category = await yaeGuild.create_category("modmail")
                  await category.set_permissions(yaeGuild.default_role, read_messages = False)
                  await category.set_permissions(modRole, read_messages = True, send_messages = False)
                  await category.set_permissions(bonkerRole, read_messages = True, send_messages = False)
                  await category.set_permissions(traineeRole, read_messages = True, send_messages = False)

                else: #if category exists, get its id instead
                  for channels in yaeGuild.channels:
                    if channels.name == "modmail":
                      categoryId = channels.id
                      category = yaeGuild.get_channel(categoryId)

                
                if author in str(yaeGuild.channels): #check if the modmail channel for user already exists and send them to that channel
                  for channels in yaeGuild.channels:
                    if str(channels) == author:
                      modmail_channel = channels.id
                      newChannel = self.bot.get_channel(modmail_channel)
                      intro = f"Redirecting to an existing private modmail {message.author.mention}"

                else: #if not, then create the private modmail     
                  newChannel = await yaeGuild.create_text_channel(author ,category = category, topic = "This is a private modmail channel.")
                  await newChannel.set_permissions(yaeGuild.default_role, read_messages = False)
                  await newChannel.set_permissions(message.author,read_messages = True, send_messages = True)
                  await newChannel.set_permissions(modRole, read_messages = True, send_messages = False)
                  await newChannel.set_permissions(bonkerRole, read_messages = True, send_messages = False)
                  await newChannel.set_permissions(traineeRole, read_messages = True, send_messages = False)

                  intro = f"private modmail has been created {message.author.mention}."

                await asyncio.sleep(2)
                await modmail.send(f"Your modmail channel {newChannel.mention} has been created." )

                #log stuffs in modmail logs
                modmail_logs = self.bot.get_channel(927602714710528051)
                modmail_logs_embed = discord.Embed(author = self.bot.user,
                description = "A new modmail was opened",
                colour = 0x00FFFF)

                modmail_logs_embed.title = "MODMAIL OPENED"
                modmail_logs_embed.set_footer(text=f"UserID: {message.author.id}")
                modmail_logs_embed.timestamp = datetime.datetime.now()

                modmail_logs_embed.add_field(name="Channel", value = newChannel.mention)
                modmail_logs_embed.add_field(name="User", value = message.author.mention)
                modmail_logs_embed.add_field(name="Message", value = message.content, inline = False)

                await modmail_logs.send(embed=modmail_logs_embed)

                #send this message inside the private modmail
                await newChannel.send(f"{intro}\n\n" 
                f"your concern was:\n"
                f"```{message.content}```")
                self.authorlist.remove(author)

                return


              elif str(reaction.emoji) == "❌": #cancel button
                await confirmation.remove_reaction("✅",self.bot.user)
                await confirmation.remove_reaction("❤️",self.bot.user)
                mailembed.title = "Cancelled ❌"
                mailembed.description = "Request has been cancelled, deleting this message in 5 seconds"
                mailembed.clear_fields()
                await confirmation.edit(embed=mailembed, delete_after = 5)
                reacted_with = "Prompt activated and reacted with ❌"

              else: #send to yae's mail-box
                await confirmation.remove_reaction("✅",self.bot.user)
                await confirmation.remove_reaction("❌",self.bot.user)
                mailembed.title = "Thank you for your message ❤️"
                mailembed.description = "Your message has been delivered to my mailbox."
                mailembed.clear_fields()
                await confirmation.edit(embed=mailembed)  
                reacted_with = "A message for me! ❤️"

              await sendembed()
              self.authorlist.remove(author)
        
            except asyncio.TimeoutError: #no response within 30 seconds
              mailembed.title = "Timeout Cancelled ❌"
              mailembed.description = "No response was given within 30 seconds. Request has been cancelled."
              mailembed.clear_fields()
              await confirmation.edit(embed=mailembed, delete_after = 5)  
              self.authorlist.remove(author)
              reacted_with = "Modmail prompt timedout"
              await sendembed()

          else:
            reacted_with = "sent messages during the prompt"
            await sendembed()

      ####Logs replies to #Modmail-logs
      elif str(message.channel.category) == "modmail":
          
          attachment = message.attachments
          sticker = message.stickers

          modmail_logs = self.bot.get_channel(927602714710528051)
          modmail_logs_embed = discord.Embed(author = self.bot.user,
                              description = "A message in a modmail was sent.",
                              colour = 0xFF00FF)

          modmail_logs_embed.title = "MODMAIL REPLY"
          modmail_logs_embed.set_footer(text=f"UserID: {message.author.id}")
          modmail_logs_embed.timestamp = datetime.datetime.now()

          modmail_logs_embed.add_field(name="Channel", value = message.channel.mention)
          modmail_logs_embed.add_field(name="User", value = message.author.mention)

          if message.attachments:
            if message.content == "":
              message_value = "Attachments below"
            
            else:
              message_value = f"{message.content}"
              modmail_logs_embed.add_field(name="Attachments", value = "Attachments below", inline = False)  
            
            modmail_logs_embed.insert_field_at(index = 2, name="Message", value = message_value, inline = False)
            await modmail_logs.send(embed=modmail_logs_embed)

            for items in attachment:
              await modmail_logs.send(items.url)

            await modmail_logs.send(f"--- End of Attachments --- from {message.author.mention}")  

          else:
            modmail_logs_embed.add_field(name="Message", value = message.content, inline = False)
            await modmail_logs.send(embed=modmail_logs_embed)


          if message.stickers:
            for stuffs in sticker:
              await modmail_logs.send(stuffs.image_url)   

  @commands.command(name = "mmreply", help = "reply to a modmail", aliases = ["mrep","mmr","rep"],hidden = True)
  @commands.has_any_role(888056856214401065, 888052696978952222,
                       888055899694972950, 889019983777124422, 889560780234719272)   
  async def mmreply(self, ctx, channel : commands.TextChannelConverter = None, *, message = None):

    if ctx.author != self.bot.user:
      
      if message == None:
        await ctx.send(f"No message was given.")
        return

      if "modmail" not in str(ctx.guild.channels): #check if category exists
        await ctx.send("Modmail category is not found.")
      
      else:   #get modmail category id 
        for channels in ctx.guild.channels:
          if channels.name == "modmail":
            categoryId = channels.id

      if channel.category_id != categoryId:#check if replying to a modmail channel
        await ctx.send("Can only be used to reply to a modmail channel.")
        return

      mm_user = self.bot.get_user(int(channel.name))
      emb_colour = 0xB320B6
      emb_thumbnail = ctx.guild.icon_url
      emb_author = ctx.author.name
      emb_description = message


      embed = discord.Embed(author = emb_author, 
        description = emb_description,
        colour = emb_colour
        )

      embed.set_author(name = "MODMAIL", icon_url = emb_thumbnail)
      embed.set_footer(text= f"Moderator:{emb_author}")
      embed.timestamp = datetime.datetime.now()
      await ctx.send(f"Modmail was sent to {channel.mention}.")
      await channel.send(content=f"{mm_user.mention}",embed=embed)  

  @mmreply.error
  async def mmreply_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.send(f"Channel isn't specified.\n`{self.bot.command_prefix}yae [channel] <message>`")
      return


  @commands.command(name = "anonmmreply", help = "reply to a modmail anonymously", aliases = ["anon","arep"],hidden = True)
  @commands.has_any_role(888056856214401065, 888052696978952222,
                       888055899694972950, 889019983777124422, 889560780234719272)  
  async def anonmmreply(self, ctx, channel : commands.TextChannelConverter = None, *, message = None):
      
    if ctx.author != self.bot.user: #waste of code space but whatever
     
      if message == None:
        await ctx.send(f"No message was given.")
        return

      if "modmail" not in str(ctx.guild.channels): #check if category exists
        await ctx.send("Modmail category is not found.")
      
      else:   #get modmail category id 
        for channels in ctx.guild.channels:
          if channels.name == "modmail":
            categoryId = channels.id

      if channel.category_id != categoryId:#check if replying to a modmail channel
        await ctx.send("Can only be used to reply to a modmail channel.")
        return

      mm_user = self.bot.get_user(int(channel.name))
      emb_colour = 0xB320B6
      emb_thumbnail = ctx.guild.icon_url
      emb_author = ctx.author.name
      emb_description = message

      embed = discord.Embed(author = emb_author, 
        description = emb_description,
        colour = emb_colour
        )

      embed.set_author(name = "MODMAIL", icon_url = emb_thumbnail)
      embed.set_footer(text= f"Moderator: Anonymous")
      embed.timestamp = datetime.datetime.now()

      await ctx.send(f"Modmail was sent to {channel.mention} anonymously.")
      await channel.send(content=f"{mm_user.mention}",embed=embed)

  @anonmmreply.error
  async def anonmmreply_error(self, ctx, error):

    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.send(f"Channel isn't specified.\n`{self.bot.command_prefix}yae [channel] <message>`")
      return
  
  @commands.command(name = "mmdelete", help = "delete a modmail channel", aliases = ["mmdel","close"],hidden = True)
  @commands.has_any_role(888056856214401065, 888052696978952222,
                        888055899694972950, 889019983777124422, 889560780234719272)  
  async def mmdelete(self,ctx, channel : commands.TextChannelConverter = None,*,reason=None):

    if ctx.author != self.bot.user: #waste of code space but whatever

      if "modmail" not in str(ctx.guild.channels): #check if category exists
        await ctx.send("Modmail category is not found.")
      
      else:   #get modmail category id 
        for channels in ctx.guild.channels:
          if channels.name == "modmail":
            categoryId = channels.id

      channel_name = channel.name

      if channel_name.isnumeric() == False: #check if the name is a number to pass through
        await ctx.send("Channel is not a modmail.")
        return

      else:  

        member = self.bot.get_user(int(channel_name)) #get the member and match it with the overwrites
        
        if channel.overwrites_for(member).is_empty() == False and channel.category_id == categoryId:
          del_confirmation =  await ctx.send(f"Are you sure you want to delete {channel.mention} of {member}? (timeout = 10s)")
          await del_confirmation.add_reaction("✅")
          await del_confirmation.add_reaction("❌")

          del_reactions = ["✅","❌"]
          def check(reaction,user): #checks the reaction click
            return user == ctx.author and str(reaction.emoji) in del_reactions

          try: 
            reaction, user = await self.bot.wait_for('reaction_add',timeout=10.0, check=check)  

            if str(reaction.emoji) == "✅":
              await ctx.send(f"the channel #{channel.name} of {member} has been deleted.")
              await channel.delete() 
              #log it to somewhere maybe??? someday
            else:
              await ctx.send(f"aborting instructions.")  
              return
          
          except asyncio.TimeoutError:
            await ctx.send("No response was given, aborting instructions.")
            return

        else:
          await ctx.send("the channel you are trying to delete is not a modmail channel")  

  @mmdelete.error
  async def mmdelete_error(self, ctx, error):

    if isinstance(error, commands.ChannelNotFound):
      await ctx.send(f"Channel was not found.")
      return
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.send(f"Channel isn't specified.\n`{self.bot.command_prefix}mmdel [channel] <reason>`")  
  

def setup(bot):
  bot.add_cog(Mod_Mail(bot))