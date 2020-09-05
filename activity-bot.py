import discord
from discord.utils import get
import csv
from datetime import datetime, date


client = discord.Client()

lol_date = datetime(2020, 7, 7)


async def lol_channel():
    channel = client.get_channel(708982721485078548)
    async for message in channel.history(after=lol_date, limit=None):
        if message.content != "lol":
            await message.delete()
            print(
                f"deleted message: {message.content} from {message.author} sent the {message.created_at}"
            )


with open("date.csv", "r") as date_file:
    csv_reader = csv.reader(date_file)
    for row in csv_reader:
        year = row[0]
        month = row[1]
        day = row[2]
        hour = row[3]
        minute = row[4]
        second = row[5]

date = datetime(
    int(year),
    int(month),
    int(day),
    int(hour),
    int(minute),
    int(second),
    0,
)

users = {}
with open("users.csv", "r") as date_file:
    csv_reader = csv.reader(date_file, delimiter=",")
    for line in csv_reader:
        users[int(line[0])] = int(line[1])
old = users.copy()


async def change_roles(
    member, counter, somewhat_active, active, very_active, hyper_active
):

    await member.remove_roles(somewhat_active, active, very_active, hyper_active)

    if counter >= 100 and counter < 500:
        await member.add_roles(somewhat_active)
    elif counter >= 500 and counter < 1000:
        await member.add_roles(active)
    elif counter >= 1000 and counter < 10000:
        await member.add_roles(very_active)
    elif counter >= 10000:
        await member.add_roles(hyper_active)


async def write(users_dict, Guild):
    with open("users.csv", "w") as users_file:
        csv_writer = csv.writer(users_file, delimiter=",")
        users_file.truncate(0)
        for ids in users_dict:
            name = Guild.get_member(ids)
            csv_writer.writerow([ids, users_dict[ids], name])


async def write_date():
    now = datetime.now()
    with open("date.csv", "r+") as date:
        writer = csv.writer(date)
        date.truncate(0)
        writer.writerow(
            [now.year, now.month, now.day, now.hour, now.minute, now.second]
        )


@client.event
async def on_ready():
    Guild = client.get_guild(708982504690024490)
    print("BOT is now online!")
    await lol_channel()
    somewhat_active = get(Guild.roles, name="Somewhat Active")
    active = get(Guild.roles, name="Active")
    very_active = get(Guild.roles, name="very active")
    hyper_active = get(Guild.roles, name="Hyper Active")
    for channel in Guild.text_channels:
        async for message in channel.history(after=date, limit=None):
            if not message.author.bot:
                member = Guild.get_member(message.author.id)
                if not message.author.id in users.keys():
                    users[message.author.id] = 0
                    old[message.author.id] = 0
                users[message.author.id] += 1
                print(
                    f"{message.author}: {users[message.author.id]} ({message.content})"
                )
    for ids in users.keys():
        if Guild.get_member(ids) != None:
            if (
                (
                    users[ids] >= 1000
                    and users[ids] < 10000
                    and not very_active in Guild.get_member(ids).roles
                )
                or (
                    users[ids] >= 500
                    and users[ids] < 1000
                    and not active in Guild.get_member(ids).roles
                )
                or (
                    users[ids] >= 100
                    and users[ids] < 500
                    and not somewhat_active in Guild.get_member(ids).roles
                )
                or (
                    users[ids] >= 10000
                    and not hyper_active in Guild.get_member(ids).roles
                )
            ):
                await change_roles(
                    Guild.get_member(ids),
                    users[ids],
                    somewhat_active,
                    active,
                    very_active,
                    hyper_active,
                )
                print(
                    f"Called change_roles for {Guild.get_member(ids)} who had {old[ids]} messages and now has {users[ids]} messages."
                )
            else:
                print(
                    f"Didn't call change_roles for {Guild.get_member(ids)} who had {old[ids]} and now has {users[ids]} messages."
                )
    await write(users, Guild)
    # print("wrote file")
    await write_date()
    # print("wrote date")

    await client.logout()


client.run("NzQ2MTA5NTg5ODI0NDcxMjAw.Xz7itA.4f-FuUC_OxsiA_wyAoXnispbLag")
