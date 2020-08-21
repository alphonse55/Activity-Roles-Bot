import discord, sys, os
from dotenv import load_dotenv

class Bot:
    def __init__(self):
        load_dotenv()
        TOKEN = os.getenv('DISCORD_TOKEN')
        self.client = discord.Client()
        self.last_response = None

        @self.client.event
        async def on_ready():
            print(f"{self.client.user} has connected to Discord!")
            self.guild = self.client.guilds[0]
            
        @self.client.event
        async def on_message(message):
            response = await self.get_response(message)
            if not response == False:
                self.last_response = await message.channel.send(response)
                
        @self.client.event
        async def on_member_join(member):
            if member.bot() == True:
                return
            else
                return
            
        self.client.run(TOKEN)

    async def get_response(self, message):
        if message.author == self.client.user:
            return False
        if message.content == "ping":
            return message.author.mention + " pong"
        for mentioned_member in message.mentions:
            if mentioned_member.id == self.client.user.id:
                return "WHAT MORTAL DARETH MENTION MY NAME?"

bot = Bot()
