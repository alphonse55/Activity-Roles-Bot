import discord
from discord.utils import get

client = discord.Client()
users = {}

somewhat_active = get(member.guild.roles, name="Somewhat Active")
active = get(member.guild.roles, name="Active")
very_active = get(member.guild.roles, name="very active")


def change_roles():

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
    for member in client.get_guild(746110570415128707).members:

        counter = 0
        for channel in member.guild.text_channels:
            async for message in channel.history(limit=1000):
                if message.author == member:
                    counter += 1
        users[member] = counter
        change_roles(member)

    print("Done")


async def on_message(message):
    users[message.author] += 1
    change_roles(message.author)


client.run("token")


# bloo = get(member.guild.roles, name="bloo")
#         print(str(member))
#         if str(member) == "?????#1044":
#             await member.remove_roles(bloo)
