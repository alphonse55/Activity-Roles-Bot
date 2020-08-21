import discord
from discord.utils import get
from dotenv import load_dotenv

client = discord.Client()
users = {}

somewhat_active = get(member.guild.roles, name="Somewhat Active")
active = get(member.guild.roles, name="Active")
very_active = get(member.guild.roles, name="very active")

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
self.client = discord.Client()


def change_roles(member, counter):

    if counter >= 100 and counter < 500:
        await member.add_role(somewhat_active)
    elif counter >= 500 and counter < 1000:
        if somewhat_active in member.roles:
            await member.remove_roles(somewhat_active)
        await member.add_roles(active)
    elif counter >= 1000:
        if active in member.roles:
            await member.remove_roles(active)
        await member.add_roles(very_active)


@client.event
async def on_ready():
        for channel in member.guild.text_channels:
            async for message in channel.history:
                if message.author == member:
                    users[member]+=1
        for members in client.guild.members:
            change_roles(member, counter)

    print("Done")


async def on_message(message):
    users[message.author] += 1
    change_roles(message.author, counter)


client.run(TOKEN)


# bloo = get(member.guild.roles, name="bloo")
#         print(str(member))
#         if str(member) == "?????#1044":
#             await member.remove_roles(bloo)
