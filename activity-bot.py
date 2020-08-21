import discord
from discord.utils import get

client = discord.Client()


@client.event
async def on_ready():
    for member in client.get_guild(746110570415128707).members:
        somewhat_active = get(member.guild.roles, name="somewhat active")
        active = get(member.guild.roles, name="Active")
        very_active = get(member.guild.roles, name="very active")
        if not very_active in member.roles:
            counter = 0
            for channel in member.guild.text_channels:
                async for message in channel.history(limit=1000):
                    if message.author == member:
                        counter += 1
                if counter >= 100 and counter < 500:
                    await member.add_role(somewhat_active)
                elif counter >= 500 and counter < 1000:
                    if somewhat_active in member.roles:
                        await member.remove_roles(somewhat_active)
                    await member.add_roles(active)
                elif counter >= 500 and counter < 1000:
                    if active in member.roles:
                        await member.remove_roles(active)
                    await member.add_roles(very_active)
        bloo = get(member.guild.roles, name="bloo")
        # print(str(member))
        # if str(member) == "?????#1044":
        #     await member.remove_roles(bloo)
    print("Done")


client.run("NzQ2MTA5NTg5ODI0NDcxMjAw.Xz7itA.xOnyvc-kpgw7kNEWN5csenXoIok")
