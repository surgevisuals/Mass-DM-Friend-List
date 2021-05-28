import discord

client = discord.Client()

@client.event
async def on_connect():
  for user in client.user.friends:
    try:
      await user.send('your message here')
      print(f"messaged: {user.name}")
    except:
       print(f"couldnt message: {user.name}")

client.run('your token here', bot=False)