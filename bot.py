import discord 
from discord.ext import commands
from discord import app_commands


from dotenv import load_dotenv
import os

from method import data_querying
load_dotenv()

BOT_TOKEN = "Your token"
CHANNEL_ID = your_id

# sets ! as symbol denoting start of the command
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())



@bot.event
async def on_ready():
    print("bot is running")
    try:
        synced= await bot.tree.sync()
        print(f"synced {len(synced)} command(s)")
    except Exception as e:
        print(e)
    
  
@bot.tree.command(name="faq")
@app_commands.describe(query= "Ask you queries?")
async def faq(interaction: discord.Interaction,query:str):
    
    
    await interaction.response.defer()

    response = await data_querying(query)
    print(response)
    await interaction.followup.send(f"hey {interaction.user.mention},  {response}",ephemeral=True)
    
bot.run(BOT_TOKEN) 
