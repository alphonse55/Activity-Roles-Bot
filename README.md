# Activity-Roles-Bot

>DISCLAIMER: This bot is written very badly, since it was my first project with discord.py and was designed to work as fast as possible.

Anyways, here is what it does:

The general goal was to actualize the roles of the server members depending on the number of messages they had. 
To do this, we wanted to go through all messages and increment the message counter of the author of that message, and later check if they had earned a new role.

We soon realised however, that it was API abuse to go though the whole channel history everytime we ran the bot, so we implemented a database with the user ID and the corresponding message counter.

When the bot starts, the database gets transformed into a dictionary and the last saved date (in another csv file) gets tranformed in a datetime object.
It then goes through every messages after that date and increments the counters of the authors by the number of new messsages they wrote and calls a function called 'change_roles' if the current role doesn't correspond to the counter. 
This function actualizes the role of the user.

If you want to use it for your server, just create a new discord application [here](https://discord.com/developers/applications) and put your token in the last file.
