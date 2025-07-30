import discord
from discord.ext import commands
import os
import requests
import json

# Bot token (keep this secure!)
# Set your token as an environment variable: export DISCORD_TOKEN='your_token_here'
TOKEN = os.getenv('DISCORD_TOKEN') or 'YOUR_BOT_TOKEN_HERE'

# Create bot instance with message content intent
# Meme API function
def get_meme():
    response = requests.get('https://meme-api.com/gimme')
    json_data = json.loads(response.text)
    return json_data['url']

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.content.startswith('$hello'):
        await message.channel.send('Hello World!')
    
    # This line is important - it allows commands to still work
    await bot.process_commands(message)

@bot.command()
async def hello(ctx):
    await ctx.send('Hello!')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

@bot.command()
async def meme(ctx):
    """Sends a random meme from the meme API"""
    try:
        meme_url = get_meme()
        embed = discord.Embed(title="Random Meme 🎭", color=0x00ff00)
        embed.set_image(url=meme_url)
        embed.set_footer(text="Powered by meme-api.com")
        await ctx.send(embed=embed)
    except Exception as e:
        await ctx.send(f"Sorry, couldn't fetch a meme right now! Error: {str(e)}")

# Run the bot
if __name__ == '__main__':
    if TOKEN == 'YOUR_BOT_TOKEN_HERE':
        print("Please set your Discord bot token!")
        print("Either set the DISCORD_TOKEN environment variable or replace 'YOUR_BOT_TOKEN_HERE' with your actual token.")
    else:
        bot.run(TOKEN)