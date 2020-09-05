import discord, sys, os
from discord.utils import get
from dotenv import load_dotenv

class Bot:
    #init bot
    def __init__(self):
        #load the token from the .env file
        #.env file should have one line that looks exactly like this, no quotes or anything (but obviously without the #):
        #DISCORD_TOKEN=the token
        load_dotenv()
        TOKEN = os.getenv('DISCORD_TOKEN')
        self.client = discord.Client()

        #basically all the counting and stuff is in here
        @self.client.event
        async def on_ready():
            #print startup message
            print(f"{self.client.user} has connected to Discord!")
            
            #setup
            self.guild = self.client.get_guild(746110570415128707)
            self.text_channels = self.guild.text_channels
            
            #put non-bot members into the self.members list
            self.members = []
            for member in self.guild.members:
                if member.bot == False:
                    self.members.append(member)
            
            #create message count dictionary
            self.message_count = {}
            for member in self.members:
                self.message_count[member] = 0
                
            #activity roles
            self.activity_roles = {}
            self.activity_roles["somewhat_active"] = get(self.guild.roles, name="Somewhat Active")
            self.activity_roles["active"] = get(self.guild.roles, name="Active")
            self.activity_roles["very_active"] = get(self.guild.roles, name="very active")
            
            #count messages
            #WIP WIP WIP WIP WIP
            #for channel in guild.text_channels:
                #async for message in channel.history(limit=None):
                    #if message.author == client.user:
                        
            
            #remove previous activity roles
            #for member in self.members:
                #await member.remove_roles(self.activity_roles["somewhat_active"], self.activity_roles["active"], self.activity_roles["very_active"])
            
            #assign roles based on number of messages
            #for member in self.members:
                #if message_count[member] >= 100 and message_count[member] < 500:
                    #member.add_roles(self.activity_roles["somewhat_active"])
                #elif message_count[member] >= 500 and message_count[member] < 1000:
                    #member.add_roles(self.activity_roles["active"])
                #elif message_count[member] >= 1000:
                    #member.add_roles(self.activity_roles["very_active"])
        
        #literally do nothing
        @self.client.event
        async def on_message(message):
            #message.channel.send()
            pass
        
        #run the bot
        self.client.run(TOKEN)

#create the bot
bot = Bot()
