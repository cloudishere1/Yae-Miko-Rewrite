import random
import discord

def globalvar():
  #name, mainstat value, rngupgrade1, rng2,rng3,rng4,weight
  global HP
  HP = ["HP",4780, 209.13,239.00,269.88,299.75,150,1000]
  global ATK
  ATK = ["ATK",311, 13.62, 15.56, 17.51, 19.45, 150,1000]
  global DEF
  DEF = ["DEF",0, 16.2,18.52,20.83,23.15,150,1000]
  global ATKP
  ATKP = ["ATK%", 46.6, 4.08, 4.66, 5.25, 5.83, 100,1000]
  global DEFP
  DEFP = ["DEF%", 46.6, 5.1, 5.83, 6.56, 7.29, 100,1000]
  global HPP
  HPP = ["HP%", 46.6, 4.08, 4.66, 5.25, 5.83, 100,1000]
  global EM
  EM = ["Elemental Mastery", 187, 16.32, 18.65, 20.98, 23.31,100,1000]
  global ER
  ER = ["Energy Recharge", 51.8, 4.53, 5.18, 5.83, 6.48, 100,1000]
  global CR
  CR = ["Crit Rate", 31.1, 2.72, 3.11, 3.5, 3.89, 75,1000]
  global CD 
  CD = ["Crit Damage", 62.2, 5.44, 6.22, 6.99, 7.77, 75,1000]
  global HealP
  HealP = ["Healing Bonus%", 35.9]
  global Elements
  Elements = ["Hydro Damage%","Pyro Damage%","Cryo Damage%","Electro Damage%","Geo Damage%","Anemo Damage%", "Dendro Damage%", 46.6]
  global Physical
  Physical = ["Physical Damage%", 58.3]
  global Elem_P
  Elem_P = [Elements, 46.6]

  global substat
  substat = [HP,ATK,DEF,ATKP,DEFP,HPP,EM,ER,CR,CD]
  global value
  value = [0,0,0,0]

  #possible mainstat
  global Flower
  Flower = [HP]
  global Feather
  Feather = [ATK]
  global Sand
  Sand = [HPP, ATKP, DEFP, EM, ER]
  global Goblet
  Goblet = [HPP, ATKP, DEFP, EM, Physical, Elements]
  global Circlet
  Circlet = [HPP, ATKP, DEFP, CR, CD, HealP, EM]

  global stat
  stat = [0,0,0,0]

  global message
  message =[0,0,0,0,0,0]

  global Mainstat
  Mainstat = [0,0]

def mainfeather():
  Mainstat[0] = Feather[0][0]
  Mainstat[1] = Feather[0][1]
  substat.remove(ATK)
  message[5] = "Plume of Death"

def mainflower():
  Mainstat[0] = Flower[0][0]
  Mainstat[1] = Flower[0][1]
  substat.remove(HP)
  message[5] = "Flower of Life"

def mainsand():
  ran = random.random() * 100

  if ran < 26.68:
    Mainstat[0] = Sand[0][0]
    Mainstat[1] = Sand[0][1]
    substat.remove(HPP)
  elif ran < 53.34:
    Mainstat[0] = Sand[1][0]
    Mainstat[1] = Sand[1][1]
    substat.remove(ATKP)
  elif ran < 80:
    Mainstat[0] = Sand[2][0]
    Mainstat[1] = Sand[2][1]
    substat.remove(DEFP)
  elif ran < 90:
    Mainstat[0] = Sand[3][0]
    Mainstat[1] = Sand[3][1]
    substat.remove(EM)
  else:
    Mainstat[0] = Sand[4][0]
    Mainstat[1] = Sand[4][1]
    substat.remove(ER)  
  
  message[5] = "Sands of Eon"

def maingoblet():
  ran = random.random() * 100

  if ran < 21.25:
    Mainstat[0] = Goblet[0][0]
    Mainstat[1] = Goblet[0][1]
    substat.remove(HPP)
  elif ran < 42.5:
    Mainstat[0] = Goblet[1][0]
    Mainstat[1] = Goblet[1][1]
    substat.remove(ATKP)
  elif ran < 62.5:
    Mainstat[0] = Goblet[2][0]
    Mainstat[1] = Goblet[2][1]
    substat.remove(DEFP)
  elif ran < 65:
    Mainstat[0] = Goblet[3][0]
    Mainstat[1] = Goblet[3][1]
    substat.remove(EM)
  elif ran < 70:
    Mainstat[0] = Goblet[4][0]
    Mainstat[1] = Goblet[4][1]
  else:
    ran = ran - 70
    if ran < (30/7):
      Mainstat[0] = Goblet[5][0]
      Mainstat[1] = Goblet[5][7]
    elif ran < (60/7):
      Mainstat[0] = Goblet[5][1]
      Mainstat[1] = Goblet[5][7]  
    elif ran < (90/7):
      Mainstat[0] = Goblet[5][2]
      Mainstat[1] = Goblet[5][7]  
    elif ran < (120/7):
      Mainstat[0] = Goblet[5][3]
      Mainstat[1] = Goblet[5][7]
    elif ran < (150/7):
      Mainstat[0] = Goblet[5][4]
      Mainstat[1] = Goblet[5][7]  
    elif ran < (180/7):
      Mainstat[0] = Goblet[5][5]
      Mainstat[1] = Goblet[5][7] 
    else:
      Mainstat[0] = Goblet[5][6]
      Mainstat[1] = Goblet[5][7]   

  message[5] = "Goblet of Eonothem"    

def maincirclet():
  ran = random.random() * 100
  if ran < 22:
    Mainstat[0] = Circlet[0][0]
    Mainstat[1] = Circlet[0][1]
    substat.remove(HPP)
  elif ran < 44:
    Mainstat[0] = Circlet[1][0]
    Mainstat[1] = Circlet[1][1]
    substat.remove(ATKP)
  elif ran < 66:
    Mainstat[0] = Circlet[2][0]
    Mainstat[1] = Circlet[2][1]
    substat.remove(DEFP)
  elif ran < 76:
    Mainstat[0] = Circlet[3][0]
    Mainstat[1] = Circlet[3][1]
    substat.remove(CR)
  elif ran < 86:
    Mainstat[0] = Circlet[4][0]
    Mainstat[1] = Circlet[4][1]
    substat.remove(CD)  
  elif ran < 96:
    Mainstat[0] = Circlet[5][0]
    Mainstat[1] = Circlet[5][1]
  else:
    Mainstat[0] = Circlet[6][0]
    Mainstat[1] = Circlet[6][1]
    substat.remove(EM)

  message[5] = "Circlet of Logos"  
      
async def get_substat(ctx,thumbnail):
  count = 0 
  total_weight = 0 
  upgrade = 0

 
  #phase 2 RNG Substat roll
    #get the total weight
  while len(substat) > count:
    total_weight = total_weight + substat[count][6]
    count += 1

  weight = total_weight
  count = 0
    #RNG for 3 or 4 substat line
  rand0 = random.random() * 100

  if rand0 > 80:
    line = 4
  else:
    line = 3

    #RNG for taking the substats

  for x in range(line):

    rand = random.random() * weight

    while rand < weight:
      stat[x] = substat[count]
      weight = weight - substat[count][6]
      count += 1
      
      vrand = random.random() * 100
      
      if vrand < 25:
        value[x] = stat[x][2]
      elif vrand < 50:
        value[x] = stat[x][3]
      elif vrand < 75:
        value[x] = stat[x][4]
      else:
        value[x] = stat[x][5]
  

    weight = total_weight
    weight = weight - stat[x][6]
    total_weight = weight

    substat.remove(stat[x])
    count = 0

    message[0] = (f'**{message[5]} : +20**\n'
    f'**{Mainstat[0]} = {Mainstat[1]}**')

    #RNG for getting 4th line if line = 3
  if line == 3:
    rand = random.random() * weight
    
    while rand < weight:
      stat[line] = substat[count]
      weight = weight - substat[count][6]
      count += 1
      
      vrand = random.random() * 100
      
      if vrand < 25:
        value[line] = stat[line][2]
      elif vrand < 50:
        value[line] = stat[line][3]
      elif vrand < 75:
        value[line] = stat[line][4]  
      else:
        value[line] = stat[line][5]
    
    upgrade += 1
    count = 0
    
    splitmsg = (f'{stat[0][0]} = {round(value[0],1)}\n'
        f'{stat[1][0]} = {round(value[1],1)}\n'
        f'{stat[2][0]} = {round(value[2],1)}\n\n')
    
    message[1] = (f'__**{stat[line][0]}** **+{value[line]}**__\n\n'
        f'{stat[0][0]} = {round(value[0],1)}\n'
        f'{stat[1][0]} = {round(value[1],1)}\n'
        f'{stat[2][0]} = {round(value[2],1)}\n'
        f'{stat[3][0]} = {round(value[3],1)}\n')

  total_weight = 0

  #Phase 3 rng for upgrade
    #get weight of the current stats
  while len(stat) > count:
    total_weight = total_weight + stat[count][7]
    count += 1

  weight = total_weight
  count = 0

    #start RNG
  if line == 4:
    message[4] = (f'{stat[0][0]} = {round(value[0],1)}\n'
        f'{stat[1][0]} = {round(value[1],1)}\n'
        f'{stat[2][0]} = {round(value[2],1)}\n'
        f'{stat[3][0]} = {round(value[3],1)}\n\n'
    )

  for x in range(upgrade, 5):

    rand = random.random() * weight

    while rand < weight:
      weight = weight - stat[count][7]
      count += 1

    if count > 0:
      count -= 1
    
    vrand = random.random() * 100
    if vrand < 25:
      value[count] = value[count] + stat[count][2]
      y=2
    elif vrand < 50:
      value[count] = value[count] + stat[count][3]
      y=3
    elif vrand < 75:
      value[count] = value[count] + stat[count][4]
      y=4
    else:
      value[count] = value[count] + stat[count][5]
      y=5

    upgrade += 1

    message[upgrade] = (f'__**{stat[count][0]}** **+{stat[count][y]}**__\n\n'
        f'{stat[0][0]} = {round(value[0],1)}\n'
        f'{stat[1][0]} = {round(value[1],1)}\n'
        f'{stat[2][0]} = {round(value[2],1)}\n'
        f'{stat[3][0]} = {round(value[3],1)}\n'
    )
    if line == 4 and upgrade == 1:
      splitmsg = message[4]

  #await ctx.reply(f'{message[0]}\n{message[1]}\n{message[2]}\n{message[3]}\n{message[4]}\n{message[5]}', mention_author = True)
  embed = discord.Embed(author = "Artifact RNG",
                         colour = 0xff99cc)
  
  embed.title = message[0]
  embed.set_author(name = "Artifact Simulator RNG",icon_url = thumbnail)
  print(thumbnail)
  embed.add_field(name = "Initial Substats", value = splitmsg,inline=False)                       
  embed.add_field(name = "Upgrade #1: +4", value = message[1])
  embed.add_field(name = "Upgrade #2: +8", value = message[2])
  embed.add_field(name = "Upgrade #3: +12", value = message[3])
  embed.add_field(name = "Upgrade #4: +16", value = message[4])
  embed.add_field(name = "Upgrade #5: +20", value = message[5])
  embed.add_field(name = u"\u200B", value = u"\u200B")
  embed.set_footer(text = "Bot made by Cloud#3260. For any errors, please DM Cloud#3260.")
  await ctx.reply(embed=embed, mention_author = True)

  
async def feather(ctx):
  
  globalvar()
  mainfeather()
  thumbnail = "https://static.wikia.nocookie.net/gensin-impact/images/8/8b/Icon_Plume_of_Death.png/revision/latest?cb=20210712005411"
  await get_substat(ctx,thumbnail)
  
  
async def flower(ctx):

  globalvar()
  mainflower()
  thumbnail = "https://static.wikia.nocookie.net/gensin-impact/images/2/2d/Icon_Flower_of_Life.png/revision/latest?cb=20210712005358"
  await get_substat(ctx,thumbnail)

async def sand(ctx):
  globalvar()
  mainsand()
  thumbnail = "https://static.wikia.nocookie.net/gensin-impact/images/9/9f/Icon_Sands_of_Eon.png/revision/latest?cb=20210713185616"
  await get_substat(ctx,thumbnail)

async def goblet(ctx):
  globalvar()
  maingoblet()
  thumbnail = "https://static.wikia.nocookie.net/gensin-impact/images/3/37/Icon_Goblet_of_Eonothem.png/revision/latest?cb=20210713185527"
  await get_substat(ctx,thumbnail)

async def circlet(ctx):
  globalvar()
  maincirclet()
  thumbnail = "https://static.wikia.nocookie.net/gensin-impact/images/6/64/Icon_Circlet_of_Logos.png/revision/latest?cb=20210712005353"
  await get_substat(ctx,thumbnail)
