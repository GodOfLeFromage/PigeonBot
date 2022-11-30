import os
my_secret = os.environ['TOKEN']
import discord
import requests
import json
from discord.ext import commands
import random
num=random.randint(0,39)
rps=random.randint(0,2)
eightBallNum=random.randint(0,8)
matchingGame=random.randint(0,7)
matchingList=random.randint(0,3)
import time
import asyncio

intents = discord.Intents.all()

#add your prefix as an ! for your bot commands
bot = commands.Bot(command_prefix='!',intents=intents)


#print a message to the console when your bot is online
@bot.event
async def on_connect():
  print("**********************")
  print("DISCORD BOT IS WORKING")
  print("**********************")

#When you call this function and your name, the bot will respond by saying "hi NAME"
@bot.command()
async def tylerName(ctx,name):
  await ctx.reply("Hey, " + name + ", how's life?")

#adds two numbers
@bot.command()
async def tylerAdd(ctx,numb,numb1):
  sum = int(numb)+int(numb1)
  await ctx.reply(str(numb) + " + " + str(numb1) + " = " + str(sum))

#subtracts two numbers
@bot.command()
async def tylerSubtract(ctx,numb,numb1):
  diff = int(numb)-int(numb1)
  await ctx.reply(str(numb) + " - " + str(numb1) + " = " + str(diff))

#multiplies two numbers
@bot.command()
async def tylerMultiply(ctx,numb,numb1):
  product = int(numb)*int(numb1)
  await ctx.reply(str(numb) + "*" + str(numb1) + " = " + str(product))

#divides two numbers
@bot.command()
async def tylerDivide(ctx,numb,numb1):
  quotient = int(numb)/int(numb1)
  await ctx.reply(str(numb) + "/" + str(numb1) + " = " + str(quotient))

#based on the time you've given, it will give you an appropriate greeting
@bot.command()
async def tylerTime(ctx,times: int,morning):
  if morning.lower() == "am":
    if times > 7:
      await ctx.reply("good morning!")
    else:
      await ctx.reply("good evening!")
  elif morning.lower() == "pm":
    if times >= 7:
      await ctx.reply("good evening!")
    else:
      await ctx.reply("good afternoon!")

#I don't really know what this one is supposed to do
@bot.command()
async def tylerMessage(ctx):
  await ctx.reply("The secret word is Hades")

#just a simple hello
@bot.command()
async def tyler(ctx):
  await ctx.reply("Hello from Tyler's Bot!")

#must have @bot.command() to register that it's a command
#a list of all commands
@bot.command()
async def commands(ctx):
  await ctx.reply("prefix is !. Commands are tyler, beautiful, eggs, puns, RPS(rock paper or scissors), caughtIn4K (person that was caught in 4K), eightBall(what you want to ask the eight ball), tylerTime(current time), tylerAdd(2 numbers), tylerSubtract(2 numbers), tylerMultiply(2 numbers), tylerDivide(2 numbers), tylerName(name)")

#you're looking very beautiful today
@bot.command()
async def beautiful(ctx,user):
  await ctx.reply(user + " is looking very beautiful today")

#I don't even know, it just makes a dumb egg joke
@bot.command()
async def eggs(ctx):
  await ctx.reply("You are an eggceptional person")

picList=["https://cdn.discordapp.com/attachments/1034301983697412118/1034931986936119378/image0.jpg","https://cdn.discordapp.com/attachments/1034301983697412118/1034932595315703848/image0.jpg","https://cdn.discordapp.com/attachments/764599162020429935/1035414305853681665/unknown.png","https://cdn.discordapp.com/attachments/764599162020429935/1035414448178995200/unknown.png","https://cdn.discordapp.com/attachments/764599162020429935/1035414532740366356/unknown.png","https://cdn.discordapp.com/attachments/764599162020429935/1035414613661057034/unknown.png","https://cdn.discordapp.com/attachments/764599162020429935/1035414797342212136/unknown.png","https://c.tenor.com/3wbD_zvy2mIAAAAC/cringe-comp-cringe.gif","https://media.discordapp.net/attachments/764599162020429935/1035415356933681162/unknown.png?width=1158&height=652"]

#prints a cringe compilation pic
@bot.command(aliases=["caughtin4k"])
async def caughtIn4K(ctx, user):
  global eightBallNum
  await ctx.send(picList[eightBallNum])
  await ctx.send(user + " has made it into my cringe compilation")
  eightBallNum=random.randint(0,8)

messageList=["Absolutely","I will not say anything without a lawyer present","HA! NO.","Pretty much","It's a 50/50 shot","You wish.","I believe it's possible","Idk man","not in a million billion years"]

#runs like an eight ball would
@bot.command(aliases=["8ball","8Ball"])
async def eightBall(ctx, question):
  global eightBallNum
  if question.lower() == "why" or question.lower() == "why?":
    await ctx.reply("because.")
  else:
    await ctx.reply(messageList[eightBallNum])
  eightBallNum=random.randint(0,8)

matchList=[":cherries: ",":strawberry: ",":apple: ",":peach: "]

@bot.command()
async def matching(ctx):
  global matchingGame
  global matchingList
  showArray=[":one:",":two:",":three:",":four:",":five:",":six","::seven:",":eight:"]
  array=["p ","p ","p ","p ","p ","p ","p ","p "]
  while array[matchingGame]=="p ":
    array[matchingGame]==matchList[matchingList]
    matchingGame=random.randint(0,7)
    matchingList=random.randint(0,3)

  row1=array[0]+array[1]+array[2]+array[3]
  row2=array[4]+array[5]+array[6]+array[7]
  showRow1=showArray[0]+showArray[1]+showArray[2]+showArray[3]
  showRow2=showArray[4]+showArray[5]+showArray[6]+showArray[7]
  await ctx.send(showRow1)
  await ctx.send(showRow2)
  await ctx.send(row1)
  await ctx.send(row2)

#use a Joke API to get a joke setup, wait a few seconds
#and deliver a punchline
@bot.command()
async def jokes(ctx):
  #variable to hold the url
  url="https://official-joke-api.appspot.com/random_joke"
  req=requests.get(url)
  #data variable that holods the json data that the api holds
  data = req.json()
  setup = data["setup"]
  punchline = data["punchline"]
  await ctx.reply(setup)
  #pauses bot but allows it to run other functions during that time
  time.asyncio.sleep(3)
  await ctx.send(punchline)

@bot.command()
async def weather(ctx,zip):
  #variable to hold the url
  my_secret_weather = os.environ['WeatherAPIkey']
  url="https://api.openweathermap.org/data/2.5/weather?zip=" + zip + ",us&appid=" + my_secret_weather
  req=requests.get(url)
  #data variable that holds the json data that the api holds
  data = req.json()

  w = data["weather"][0]["description"]
  temp=data["main"]["temp"]
  temp = (temp - 273.15)*9/5+32
  await ctx.reply(w + ", " + str(temp) + " degress F")

@bot.command()
async def yodaTranslate(ctx, phrase):
  newPhrase = phrase.replace(" ", "%20")
  url = "https://api.funtranslations.com/translate/yoda.json?text=" + newPhrase + "."
  data=requests.get(url).json()
  translated=data["contents"]["translated"]
  translatedLength = len(str(translated))
  newTranslatedLength = translatedLength-1
  newTranslated = str(translated) [0:newTranslatedLength]
  await ctx.reply(newTranslated)

@bot.command()
async def googleTranslate(ctx, phrase):
  my_secret = os.environ['googleTranslateKey']

  newPhrase = phrase.replace(" ", "%20")
  
  url = "https://google-translate1.p.rapidapi.com/language/translate/v2/detect"
  
  payload = "q=" + newPhrase
  headers = {
  	"content-type": "application/x-www-form-urlencoded",
  	"Accept-Encoding": "application/gzip",
  	"X-RapidAPI-Key": my_secret,
  	"X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
  }
  response = requests.request("POST", url, data=payload, headers=headers)
  data=response.json()
  # {"data":{"detections":[[{"confidence":1,"isReliable":false,"language":"en"}]]}}
  confidence = data["data"]["detections"][0][0]["confidence"]
  isReliable = data["data"]["detections"][0][0]["isReliable"]
  language = data["data"]["detections"][0][0]["language"]
  if isReliable == "false":
    isReliable == "it is not"
  else:
    isReliable == "it is"
  await ctx.reply(language.upper())
  await ctx.send("Confidence Level: " + str(confidence))
  await ctx.send(str(isReliable) + " reliable")
  print(response.text)

@bot.command()
async def art(ctx, pic):
  my_secret = os.environ['ArtKey']

  url = "https://dagpi.p.rapidapi.com/image/blur/"
  files = []
  for file in ctx.message.attachments:
        fp = dagipi()
        await file.save(fp)
        files.append(discord.File(fp, filename=file.filename, spoiler=file.is_spoiler()))

  
  headers = {
  	"Authorization": "apiKey",
  	"X-RapidAPI-Key": "9272b82816msh65747778e5c6cfdp1eb4f4jsnbbf89a3779a5",
  	"X-RapidAPI-Host": "dagpi.p.rapidapi.com"
  }
  
  response = requests.request("GET", url, headers=headers, params=fp)
  
  await ctx.send(files=response)

#it's rock paper scissors, baby!
@bot.command(aliases=["rockpaperscissors","rockPaperScissors","rps"])
async def RPS(ctx, move):
  global rps
  if rps == 0:
    #bot choose rock
    await ctx.reply(":rock:")
    if move.lower()=="rock":
      await ctx.send("Stalemate.")
    elif move.lower()=="paper":
      await ctx.send("You cheated.")
    elif move.lower()=="scissors":
      await ctx.send("That was a fair and unbiased fight")
    else:
      await ctx.reply("Rock, Paper, or Scissors. How hard is that to understand?")
  elif rps == 1:
    #bot choose paper
    await ctx.reply(":newspaper:")
    if move.lower()=="paper":
      await ctx.send("Stalemate.")
    elif move.lower()=="scissors":
      await ctx.send("You cheated.")
    elif move.lower()=="rock":
      await ctx.send("That was a fair and unbiased fight")
    else:
      await ctx.reply("Rock, Paper, or Scissors. How hard is that to understand?")
  else:
    # bot choose scissors
    await ctx.reply(":scissors:")
    if move.lower()=="scissors":
      await ctx.send("Stalemate.")
    elif move.lower()=="rock":
      await ctx.send("You cheated.")
    elif move.lower()=="paper":
      await ctx.send("That was a fair and unbiased fight")
    else:
      await ctx.reply("Rock, Paper, or Scissors. How hard is that to understand?")
  rps=random.randint(0,2)
  
#comedy gold
@bot.command()
async def puns(ctx):
  global num
  global time
  if num == 0:
    await ctx.reply("What did the triangle say to the circle?")
    time.sleep(2)
    await ctx.send("You're pointless.")
  elif num == 1:
    await ctx.reply("What did the cannibal get when he came to the party late?")
    time.sleep(2)
    await ctx.send("A cold shoulder.")
  elif num == 2:
    await ctx.reply("I heard two peanuts walked into a park...")
    time.sleep(2)
    await ctx.send("One was as-salted.")
  elif num == 3:
    await ctx.reply("A boiled egg in the morning is really hard to beat.")
  elif num == 4:
    await ctx.reply("I'm reading a book on anti-gravity, and it's impossible to put down.")
  elif num == 5:
    await ctx.reply("I'm glad I know sign language")
    time.sleep(2)
    await ctx.send("It's become quite handy.")
  elif num == 6:
    await ctx.reply("I forgot how to throw a boomerang...")
    time.sleep(2)
    await ctx.send("But it came back to me.")
  elif num == 7:
    await ctx.reply("When a clock is hungry,")
    time.sleep(2)
    await ctx.send("It goes back four seconds.")
  elif num == 8:
    await ctx.reply("I once heard a joke about amnesia...")
    time.sleep(2)
    await ctx.send("But I forget how it goes...")
  elif num == 9:
    await ctx.reply("When the power went out at school...")
    time.sleep(2)
    await ctx.send("The children were de-lighted.")
  elif num == 10:
    await ctx.reply("Those fish were shy...")
    time.sleep(2)
    await ctx.send("They were obviously coy.")
  elif num == 11:
    await ctx.reply("Those two men drinking battery acid will soon be charged.")
  elif num == 12:
    await ctx.reply("What is a pirate's favorite letter?")
    time.sleep(2)
    await ctx.send("'Tis the C!")
  elif num == 13:
    await ctx.reply("Did you hear about the midget psychic that escaped from prison?")
    time.sleep(2)
    await ctx.send("He's a small medium at large")
  elif num == 14:
    await ctx.reply("I'm inclined...")
    time.sleep(2)
    await ctx.send("To be laid back.")
  elif num == 15:
    await ctx.reply("Headline reads: **CARTOONIST FOUND DEAD AT HOME**")
    time.sleep(2)
    await ctx.send("**DETAILS ARE SKETCHY**")
  elif num == 16:
    await ctx.reply("The magician got frustrated and pulled his hare out.")
  elif num == 18:
    await ctx.reply("The frustrated cannibal threw up his hands.")
  elif num == 17:
    await ctx.reply("A criminal's best asset...")
    time.sleep(2)
    await ctx.send("Is his-lie-ability")
  elif num == 18:
    await ctx.reply("I didn't have the faintest idea...")
    time.sleep(2)
    await ctx.send("As to why I passed out.")
  elif num == 19:
    await ctx.reply("I heard about the guy who got hit in the head with a can of soda...")
    time.sleep(2)
    await ctx.send("He's lucky it was a soft drink.")
  elif num == 20:
    await ctx.reply("There was once a cross-eyed teacher...")
    time.sleep(2)
    await ctx.send("Who had issues controlling his pupils.")
    print(num)
  elif num == 21:
    await ctx.reply("Did you know diarreha is hereditary?")
    time.sleep(2)
    await ctx.send("It runs in your genes.")
  elif num == 22:
    await ctx.reply("It doesn't matter how much you push the envelope...")
    time.sleep(2)
    await ctx.send("It'll still be stationary.")
  elif num == 23:
    await ctx.reply("What did the Confederate soldiers use to eat off of?")
    time.sleep(2)
    await ctx.send("Civil ware.")
  elif num == 24:
    await ctx.reply("What did the Confederate soldiers used to drink with?")
    time.sleep(2)
    await ctx.send("Dixie Cups.")
  elif num == 25:
    await ctx.reply("A book just fell on my head...")
    time.sleep(2)
    await ctx.send("I only have my shelf to blame.")
  elif num == 26:
    await ctx.reply("Bakers trade bread recipes on a knead-to-know-basis")
  elif num == 27:
    await ctx.reply("A moon rock tastes better than an earthly rock...")
    time.sleep(2)
    await ctx.send("Because it's meteor.")
  elif num == 28:
    await ctx.reply("A backwards poet writes inverse.")
  elif num == 29:
    await ctx.reply("I used to be addicted to soap...")
    time.sleep(2)
    await ctx.send("But I'm clean now.")
  elif num == 30:
    await ctx.reply("3.14% of sailors are Pi Rates")
  elif num == 31:
    await ctx.reply("I stayed up all night wondering where the sun went...")
    time.sleep(2)
    await ctx.send("Then it dawned on me.")
  elif num == 32:
    await ctx.reply("Why did the scarecrow get a promotion?")
    time.sleep(2)
    await ctx.send("Because he was outstanding in his field.")
  elif num == 33:
    await ctx.reply("I tried to catch some fog earlier...")
    time.sleep(2)
    await ctx.send("I mist.")
  elif num == 34:
    await ctx.reply("Do you know what's not right?")
    time.sleep(2)
    await ctx.send("Left.")
  elif num == 35:
    await ctx.reply("What does a pirate say while eating sushi?")
    time.sleep(2)
    await ctx.send("Ahoy! Pass me some soy!")
  elif num == 36:
    await ctx.reply("People are making apocalypse jokes like there's no tomorrow.")
  elif num == 37:
    await ctx.reply("Wanna hear a joke about pizza?")
    time.sleep(2)
    await ctx.send("Nevermind, it was too cheesy.")
  elif num == 38:
    await ctx.reply("What did the green grape say to the purple grape?")
    time.sleep(2)
    await ctx.send("'Breathe, you idiot!'")
  elif num == 39:
    await ctx.reply("Why can't your nose be twelve inches long?")
    time.sleep(2)
    await ctx.send("Because then it'd be a foot.")
  lastNum=num
  while num==lastNum:
    num=random.randint(0,39)
  #saluting our fallen puns
  
  #What did the mermaid wear to her math class?
  #An algae bra.
    
  #What is the leading cause of divorce in long-term marriages?
  #A stalemate.
    
  #I walked into my sister's room and tripped on a bra
  #It was a booby trap.
    
  #It's not that the guy didn't know how to juggle...
  #It's that he didn't have the balls to do it.

#copy your bot token from discord developer
bot.run(my_secret)