import discord
import requests
import json
import random

def get_meme():
  response = requests.get('https://meme-api.com/gimme/catmemes')
  json_data = json.loads(response.text)
  return json_data['url']
def get_pkm():
  response = requests.get("https://meme-api.com/gimme/pokemon")
  json_data = json.loads(response.text)
  return json_data['url']
def how_r_u():
  reply = ["im okay", "could be better", "im having a good day", "i need a hug"]
  response = random.choice(reply)
  return response
  print(random.choice)

class MyClient(discord.Client):
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))
  async def on_message(self, message):
    if message.author == self.user:
      return

    if message.content.startswith('$hello'):
      await message.channel.send('Hello, darling!')
    if message.content.startswith('$meme'):
      await message.channel.send(get_meme())
    if message.content.startswith("$pkm"):
      await message.channel.send(get_pkm())
    if message.content.startswith("$feeling"):
      await message.channel.send(how_r_u())

intents = discord.Intents.default()
intents.message_content = True
