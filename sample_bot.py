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
            self.text_channels = self.guild.text_channels
            self.members = self.guild.members
            
            #create message count dictionary
            self.message_count = {}
            for member in self.members:
                message_count[member] = 0
                
            #activity roles
            self.activity_roles = {}
            self.activity_roles["somewhat_active"] = get(self.guild.roles, name="Somewhat Active")
            self.activity_roles["active"] = get(self.guild.roles, name="Active")
            self.activity_roles["very_active"] = get(self.guild.roles, name="very active")
            
            #remove previous activity roles
            for member in self.members:
                await member.remove_roles(self.activity_roles["somewhat_active"], self.activity_roles["active"], self.activity_roles["very_active"])
            
            #count messages
            #WIP WIP WIP WIP WIP
            for channel in guild.text_channels:
                async for message in channel.history(limit=None):
                    if message.author == client.user:
                        
                        
            #assign roles based on number of messages
            for member in self.members:
                if message_count[member] >= 100 and message_count[member] < 500:
                    member.add_roles(self.activity_roles["somewhat_active"])
                elif message_count[member] >= 500 and message_count[member] < 1000:
                    member.add_roles(self.activity_roles["active"])
                elif message_count[member] >= 1000:
                    member.add_roles(self.activity_roles["very_active"])
        
        #literally do nothing
        @self.client.event
        async def on_message(message):
            #message.channel.send(response)
        
        #run the bot
        self.client.run(TOKEN)

#create the bot
bot = Bot()
