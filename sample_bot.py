import discord, sys, os
from discord.utils import get
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
            
            self.guild = self.client.get_guild(746110570415128707)
            self.members = self.guild.members
            
            self.activity_roles = {}
            self.activity_roles["somewhat_active"] = get(self.guild.roles, name="Somewhat Active")
            self.activity_roles["active"] = get(self.guild.roles, name="Active")
            self.activity_roles["very_active"] = get(self.guild.roles, name="very active")
            
            #iterate through members; first, remove all previous activity roles; second, traverse their message history and count their messages
            for member in self.members:
                await member.remove_roles(self.activity_roles["somewhat_active"], self.activity_roles["active"], self.activity_roles["very_active"])
                
                message_counter = 0
                for message in member.history
        
        #literally do nothing
        @self.client.event
        async def on_message(message):
            #message.channel.send(response)
        
        #run the bot
        self.client.run(TOKEN)

#create the bot
bot = Bot()
