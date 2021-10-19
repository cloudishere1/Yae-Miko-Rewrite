import discord
import random

from discord.ext import commands

"""Auto message

-> on member update
  ->Server Boost message 
    ->boost role id: 888053107601338389)
    ->Announcement channel id: 888053718182932480
  
-> on member join
  ->DM the instruction
  ->Welcome message
    ->Welcome channel id: 888054635305250856

->Auto role
  ->enter
    ->to give shrine member role (shrine member role id: 888055555661398036)
"""
"""await member.dm_channel.send(
          f'Hello {member.name} <a:YaeJump:888060435042017320><a:YaeJump:888060435042017320><a:YaeJump:888060435042017320>, welcome to **{guild.name}**! Make sure to read the <#888054653877633074> to get started!'
        )"""

class Yae_automsg(commands.Cog):
  
  def __init__ (self, bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_member_update(self,before,after):
  
    role = discord.utils.get(before.guild.roles, id=888053107601338389)
    channel = self.bot.get_channel(888053718182932480)

    if role not in before.roles:
      if role in after.roles:
        await channel.send(f"Thank you for boosting our shrine {after.mention}!<a:YaeJump:888060435042017320><a:YaeJump:888060435042017320><a:YaeJump:888060435042017320>\n"
        f"You can create your own __custom role__ and set your __color name__ in <#888053538012413992>,\nYou can also apply for __custom role icon__, Please check the pinned messages there for more details! <a:YaeStonks:888090125832167484><a:YaeStonks:888090125832167484><a:YaeStonks:888090125832167484>")

  @commands.Cog.listener()
  async def on_member_join(self,member):
    guild = discord.utils.get(self.bot.guilds, name=member.guild.name)    

    try: #this is the welcome DM code
      await member.create_dm()
      await member.dm_channel.send(
          f'Hello {member.name} <a:YaeJump:888060435042017320><a:YaeJump:888060435042017320><a:YaeJump:888060435042017320>, welcome to **{guild.name}**! Make sure to read the <#888054653877633074> to receive your **Shrine Member** role to access the server and get started! \n\n'
          f"If you cannot get the `Shrine Member` role to enter the server after getting roles from <#888054674798837770>, try it again but do not spam it.\n\n" 
          f"If it still doesn't work, type the command `!!enter` in <#888054635305250856> in {guild.name}. **I cannot respond to commands in DMs**\n\n"
          f"If it still does not give you the role, kindly contact **SHRINE CHIEF** or **SHRINE GUARD** for manual roles.\n\nOr you can send a message to me! <a:YaeWink_noBG2:832972418045050900>")

    except:
      pass    

    channel = self.bot.get_channel(888054635305250856)

    emb_colour = 0xB320B6
    emb_thumbnail = member.avatar_url
    emb_author = guild.name
    member_id = member.id
    emb_image = ["https://media.discordapp.net/attachments/765662367538610198/858717661092249620/ezgif-6-692e7b979e07.gif",
      "https://cdn.discordapp.com/attachments/765662367538610198/879764015461580810/ezgif-6-5e4d6b21d808.gif",
      "https://media.discordapp.net/attachments/765662367538610198/882288825215377499/ezgif-6-e324bbbb68ff.gif"]

    emb_title = f"Welcome to {guild.name} | Genshin Impact!"
    emb_description = (f"Make sure to read our simple <#888054653877633074> and follow the instructions there to access the server.") 

    rand = random.choice(emb_image)

    embed = discord.Embed(author = emb_author,
      title = emb_title, 
      description = emb_description,
      colour = emb_colour)

    embed.set_image(url = rand)
    embed.set_author(name = emb_author, icon_url = guild.icon_url)
    embed.set_thumbnail(url = emb_thumbnail)
    embed.set_footer(text= f"User ID:{member_id}")

    await channel.send(f"Hello {member.mention}, Welcome to our shrine!",embed=embed)

  @commands.command(name='enter', help= 'gives shrine member role', hidden = True)
  async def enter(self, ctx):
    
    role = discord.utils.get(ctx.guild.roles, id=888055555661398036)
    await ctx.message.delete()
    
    if ctx.author == self.bot.user:
      return

    if role not in ctx.author.roles:
      await ctx.author.add_roles(role)
      await ctx.send(f"Shrine Member role is given to {ctx.author.mention}.")
      return

    else:
      pass   

def setup(bot):
  bot.add_cog(Yae_automsg(bot))    

  