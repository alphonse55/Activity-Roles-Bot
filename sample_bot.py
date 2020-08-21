import discord, sys, os
from dotenv import load_dotenv

class Bot:
    #init bot
    def __init__(self):
        load_dotenv()
        TOKEN = os.getenv('DISCORD_TOKEN')
        self.client = discord.Client()

        #get the channels and users and stuff
        @self.client.event
        async def on_ready():
            print(f"{self.client.user} has connected to Discord!")
            self.guild = self.client.guilds[0]
        
        #literally do nothing
        @self.client.event
        async def on_message(message):
            #message.channel.send(response)
        
        #run the bot
        self.client.run(TOKEN)

#create the bot
bot = Bot()
