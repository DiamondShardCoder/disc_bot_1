import discord

client = discord.Client()

ID = Enter your ID without strings

@client.event
async def on_member_join(member):
    for channel in member.guild.channels:
        if str(channel) == "general":
            await channel.send(f"""Welcome to the server MF {member.mention}""")

@client.event
async def on_message(message):
    id = client.get_guild(ID)
    commands = ["! hello", "! hi", "! sup", "! users"]
    swear_words = ["fuck", "Fuck", "pussy", "bitch", "cunt", "MF", "Bitch"]
    for swear_word in swear_words:
        if message.content.find(swear_word) != -1:
            await message.channel.send("SWORE!")
    if message.content.find("!hello") != -1:
        await message.channel.send("Hello MF")
    elif message.content.find("!sup") != -1:
        await message.channel.send("Wazzup Bitch")
    elif message.content.find("!hi") != -1:
        await message.channel.send("Heyy")
    elif message.content == "!users":
        await message.channel.send(f"""# of Members: {id.member_count}""")
    elif message.content.find("nigga") != -1:
        await message.channel.send("Now you are being a racist!")
    elif message.content.find("u wank?") != -1:
        await message.channel.send("As many times as my hand can take it")
    elif message.content.find("baba tunde") != -1:
        await message.channel.send("Its my name!")


    elif message.content.find("!commands") != -1:
        for command in commands:
            await message.channel.send(command)

client.run("TOKEN HERE")
