#if you are running another bot remember to go to https://uptimerobot.com/dashboard#793018487 and change the url for Pigeon Bot
import keep_alive
import os
import nacl
from discord.ext import commands,tasks
import youtube_dl
from youtube_dl import YoutubeDL
my_secret = os.environ['TOKEN']
import discord
import requests
import json
import random
num=random.randint(0,39)
rps=random.randint(0,2)
eightBallNum=random.randint(0,8)
matchingGame=random.randint(0,7)
matchingList=random.randint(0,3)
import time
import asyncio
import pafy
from discord import FFmpegPCMAudio, PCMVolumeTransformer
FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options': '-vn'}


intents = discord.Intents.all()
client = discord.Client(intents=intents)

#add your prefix as an ! for your bot commands
bot = commands.Bot(command_prefix='!pidge ',intents=intents)

#print a message to the console when your bot is online
@bot.event
async def on_connect():
  print("**********************")
  print("DISCORD BOT IS WORKING")
  print("**********************")

helpCommand=commands.DefaultHelpCommand(no_category='Commands')
  
#When you call this function and your name, the bot will respond by saying "hi NAME"
@bot.command(brief="name(name): greets the user, and asks them how their day is")
async def name(ctx,name):
  await ctx.reply("Hey, " + name + ", how's your day going?")

#adds two numbers
@bot.command(brief="add(number number): adds two numbers together")
async def add(ctx,numb,numb1):
  sum = int(numb)+int(numb1)
  await ctx.reply(str(numb) + " + " + str(numb1) + " = " + str(sum))

#subtracts two numbers
@bot.command(brief="subtract(number number): subtracts two numbers")
async def subtract(ctx,numb,numb1):
  diff = int(numb)-int(numb1)
  await ctx.reply(str(numb) + " - " + str(numb1) + " = " + str(diff))

#multiplies two numbers
@bot.command(brief="multiply(number number): multiplies two numbers together")
async def multiply(ctx,numb,numb1):
  product = int(numb)*int(numb1)
  await ctx.reply(str(numb) + "*" + str(numb1) + " = " + str(product))

#divides two numbers
@bot.command(brief="divide(number number): divides two numbers")
async def divide(ctx,numb,numb1):
  quotient = int(numb)/int(numb1)
  await ctx.reply(str(numb) + "/" + str(numb1) + " = " + str(quotient))

#based on the time you've given, it will give you an appropriate greeting
@bot.command(brief="whatTime(time): Gives an appropriate response based on the current time")
async def whatTime(ctx,times: int,morning):
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
@bot.command(brief="I don't remember what this one does, please just ignore it")
async def message(ctx):
  await ctx.reply("The secret word is Hades")

#just a simple hello
@bot.command(brief="gives a hello")
async def hello(ctx):
  await ctx.reply("Hello from Tyler's Bot!")

#you're looking very beautiful today
@bot.command(brief="beautiful(person): tells person that they're looking beautiful today")
async def beautiful(ctx,user):
  await ctx.reply(user + " is looking very beautiful today")

#I don't even know, it just makes a dumb egg joke
@bot.command(brief="This just tells one terrible egg pun")
async def eggs(ctx):
  await ctx.reply("You are an eggceptional person")

picList=["https://cdn.discordapp.com/attachments/1034301983697412118/1034931986936119378/image0.jpg","https://cdn.discordapp.com/attachments/1034301983697412118/1034932595315703848/image0.jpg","https://cdn.discordapp.com/attachments/764599162020429935/1035414305853681665/unknown.png","https://cdn.discordapp.com/attachments/764599162020429935/1035414448178995200/unknown.png","https://cdn.discordapp.com/attachments/764599162020429935/1035414532740366356/unknown.png","https://cdn.discordapp.com/attachments/764599162020429935/1035414613661057034/unknown.png","https://cdn.discordapp.com/attachments/764599162020429935/1035414797342212136/unknown.png","https://c.tenor.com/3wbD_zvy2mIAAAAC/cringe-comp-cringe.gif","https://media.discordapp.net/attachments/764599162020429935/1035415356933681162/unknown.png?width=1158&height=652"]

#prints a cringe compilation pic
@bot.command(aliases=["caughtin4k"],brief="caughtIn4K(person): adds a person to the bot's cringe compilation, no, this is not stored anywhere and you may not view it.")
async def caughtIn4K(ctx, user):
  global eightBallNum
  await ctx.send(picList[eightBallNum])
  await ctx.send(user + " has made it into my cringe compilation")
  eightBallNum=random.randint(0,8)

messageList=["Absolutely","I will not say anything without a lawyer present","HA! NO.","Pretty much","It's a 50/50 shot","You wish.","I believe it's possible","Idk man","not in a million billion years"]

#runs like an eight ball would
@bot.command(aliases=["8ball","8Ball"],brief="eightBall(question): asks the 8 ball a question")
async def eightBall(ctx, question):
  global eightBallNum
  if question.lower() == "why" or question.lower() == "why?":
    await ctx.reply("because.")
  else:
    await ctx.reply(messageList[eightBallNum])
  eightBallNum=random.randint(0,8)

##########################################################################################
# MUSIC SECTION
##########################################################################################

@bot.command()
async def join(ctx):
  print("1")
  if ctx.author.voice is None:
    print("2")
    await ctx.reply("You're not in a voice channel.")
  
  if ctx.voice_client is None:
    print("3")
    channel=ctx.author.voice.channel
    await channel.connect()
    await ctx.reply("Connected.")
  else:  
    print("4")
    channel=ctx.author.voice.channel
    await ctx.voice_client.move_to(channel)

  
@bot.command()
async def play(ctx,url):
  voice_client = ctx.message.guild.voice_client
  await ctx.reply("Queueing...")
  youtube_dl_opts={'format':"bestaudio"}
#with statement is essentially meant to make code easier to read, functions as a thing=thing
  with YoutubeDL(youtube_dl_opts) as ydl:
    info_dict = ydl.extract_info(url, download=False)
    audio = info_dict["url"]
    print(audio)
    source = FFmpegPCMAudio(audio.url, **FFMPEG_OPTIONS)
  await ctx.reply("Playing video")
  voice_client.play(source)
  
@bot.command()
async def leave(ctx):
  # server = ctx.message.guild
  voice_client = ctx.message.guild.voice_client
  #voice_client = client.voice_client_in(server)
  if voice_client:
      await voice_client.disconnect()
      print("Bot left the voice channel")
  else:
      print("Bot was not in channel")

##########################################################################################
# MUSIC END
##########################################################################################

#use a Joke API to get a joke setup, wait a few seconds
#and deliver a punchline
@bot.command(brief="Uses a joke API to give a terrible pun")
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
  await asyncio.sleep(1)
  await ctx.send(punchline)

@bot.command(brief="weather(zipcode): uses API to tell the Weather")
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

@bot.command(brief="yodaTranslate(phrase): Garbles a phrase into Yoda speech")
async def yodaTranslate(ctx, phrase):
  newPhrase = phrase.replace(" ", "%20")
  url = "https://api.funtranslations.com/translate/yoda.json?text=" + newPhrase + "."
  data=requests.get(url).json()
  translated=data["contents"]["translated"]
  translatedLength = len(str(translated))
  newTranslatedLength = translatedLength-1
  newTranslated = str(translated) [0:newTranslatedLength]
  await ctx.reply(newTranslated)

@bot.command(brief="urbanDictionary(word): searches Urban Dictionary for a word.")
async def urbanDictionary(ctx, definition):
  
  url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"
  
  querystring = {"term":definition}
  
  headers = {
  	"X-RapidAPI-Key": "bdca7e9380msha693b4ffe3ff886p1447adjsn2074e3f0feb5",
  	"X-RapidAPI-Host": "mashape-community-urban-dictionary.p.rapidapi.com"
  }
  response = requests.request("GET", url, headers=headers, params=querystring)
  data=response.json()
  definition = data["list"][0]["definition"]
  example = data["list"][0]["example"]
  definition = cleanUp(definition)
  example = cleanUp(example)
  await ctx.reply(definition)
  await ctx.send("Example: ")
  await ctx.send(example)

def cleanUp(phrase):
  newDef = phrase.replace("[", "")
  definition = newDef.replace("]", "")
  return definition
  
@bot.command()
async def art(ctx):
  list=["a", "b", "c",   "d",   "e",   "f",   "g",   "h",   "i",   "j",   "k",   "l",   "m",   "n",   "o",   "p",   "q",   "r",   "s",   "t",   "u",   "v",   "x",   "y",   "z",   "-",   "/",   "_",   "1",   "2",   "3,",   "4,",   "5,",   "6,",   "7,",   "8,",   "9", "0", ",", ":"]
  my_secret = os.environ['ArtKey']


  message=ctx.message
  for attachment in message.attachments:
    img = attachment.url
 #Save to disk and create discord file object

  url = "https://api.apilayer.com/face_pixelizer?url?url=" + img
 
  payload= {}
  headers = {
  "X-RapidAPI-Key": 'ArtKey',
  }


  response = requests.request("GET", url, headers=headers, data=payload)
  request= response.text
  request2=""
  for char in request:
    if char in list:
      request2 += char
  await ctx.reply(request2[7:])

#it's rock paper scissors, baby!
@bot.command(aliases=["rockpaperscissors","rockPaperScissors","rps"],brief="RPS(rock, paper, or scissors): it's Rock Paper Scissors")
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
@bot.command(brief="Gives the best puns known to man.")
async def puns(ctx):
  global num
  global time
  if num < 31:
    setup = punchline(num,1)
    await ctx.reply(setup)
    await asyncio.sleep(1)
    payoff = punchline(num,2)
    await ctx.send(payoff)
  else:
    singlePun = singularJoke(num%8)
    await ctx.reply(singlePun)
  lastNum=num
  while num==lastNum:
    num=random.randint(0,39)

def singularJoke(num):
  singleList=["A boiled egg in the morning is really hard to beat.","I'm reading a book on anti-gravity, and it's impossible to put down.","Those two men drinking battery acid will soon be charged.","The magician got frustrated and pulled his hare out.","The frustrated cannibal threw up his hands.","Bakers trade bread recipes on a knead-to-know-basis","A backwards poet writes inverse.","3.14% of sailors are Pi Rates","People are making apocalypse jokes like there's no tomorrow."]
  joke=singleList[num]
  return(joke)

def punchline(num,type):
  setup=["What did the triangle say to the circle?","What did the cannibal get when he came to the party late?","I heard two peanuts walked into a park...","I'm glad I know sign language","I forgot how to throw a boomerang...","When a clock is hungry,","I once heard a joke about amnesia...","Why can't your nose be twelve inches long?","What did the green grape say to the purple grape?","Wanna hear a joke about pizza?","What does a pirate say while eating sushi?","Do you know what's not right?","I tried to catch some fog earlier...","Why did the scarecrow get a promotion?","I stayed up all night wondering where the sun went...","I used to be addicted to soap...","A moon rock tastes better than an earthly rock...","A book just fell on my head...","What did the Confederate soldiers used to drink with?","What did the Confederate soldiers use to eat off of?","It doesn't matter how much you push the envelope...","Did you know diarreha is hereditary?","There was once a cross-eyed teacher...","I heard about the guy who got hit in the head with a can of soda...","I didn't have the faintest idea...","A criminal's best asset...","Headline reads: **CARTOONIST FOUND DEAD AT HOME**","I'm inclined...","Did you hear about the midget psychic that escaped from prison?","What is a pirate's favorite letter?","Those fish were shy...","When the power went out at school..."]
  payoff=["You're pointless.","A cold shoulder.","One was as-salted.","It's become quite handy.","But it came back to me.","It goes back four seconds.","But I forget how it goes...","Because then it'd be a foot.","'Breathe, you idiot!'","Nevermind, it was too cheesy.","Ahoy! Pass me some soy!","Left.","I mist.","Because he was outstanding in his field.","Then it dawned on me.","But I'm clean now.","Because it's meteor.","I only have my shelf to blame.","Dixie Cups.","Civil ware.","It'll still be stationary.","It runs in your genes.","Who had issues controlling his pupils.","He's lucky it was a soft drink.","As to why I passed out.","Is his-lie-ability","**DETAILS ARE SKETCHY**","To be laid back.","He's a small medium at large","'Tis the C!","They were obviously coy.","The children were de-lighted."]
  num1 = setup[num]
  num2 = payoff[num]
  if type==1:
    return(num1)
  else:
    return(num2)
  #saluting our fallen puns
  
  #What did the mermaid wear to her math class?
  #An algae bra.
    
  #What is the leading cause of divorce in long-term marriages?
  #A stalemate.
    
  #I walked into my sister's room and tripped on a bra
  #It was a booby trap.
    
  #It's not that the guy didn't know how to juggle...
  #It's that he didn't have the balls to do it.

keep_alive.keep_alive()
#copy your bot token from discord developer
bot.run(my_secret)