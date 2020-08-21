import discord
from discord.utils import get

# from dotenv import load_dotenv

client = discord.Client()
users = {}
Guild = client.get_guild(708982504690024490)

# load_dotenv()
# TOKEN = os.getenv('DISCORD_TOKEN')
# self.client = discord.Client()
TOKEN = "token"


async def change_roles(member, counter):
    somewhat_active = get(member.guild.roles, name="Somewhat Active")
    active = get(member.guild.roles, name="Active")
    very_active = get(member.guild.roles, name="very active")

    if counter >= 100 and counter < 500:
        await member.add_roles(somewhat_active)
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

    for channel in Guild.text_channels:
        async for message in channel.history:
            users[message.author] += 1
    for member in client.guild.members:
        change_roles(member, users[member])

    print("Done")


async def on_message(message):
    users[message.author] += 1
    change_roles(message.author, users[message.author])


client.run(TOKEN)


# bloo = get(member.guild.roles, name="bloo")
#         print(str(member))
#         if str(member) == "?????#1044":
#             await member.remove_roles(bloo)
