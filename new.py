import os
import discord
from discord.ext import commands

TOKEN = os.getenv("TOKEN")  # Load token from env variable

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot connected as {bot.user}")

@bot.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name="Member")  # Change role name as needed
    if role:
        await member.add_roles(role)
        print(f"Assigned role to {member.name}")

bot.run(TOKEN)
