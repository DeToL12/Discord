import discord
from discord.ext import commands

# Replace these with your actual values
TOKEN = 'MTExOTg1MzgxNDQ1NjAwODg4NQ.GlffYo.D7O5wvg4YIcz8tz9DYohdZ9rWAHVPONZrVu86Q'
GUILD_ID = 1322662016728432702  # Replace with your server's ID
ROLE_NAME = 'Friend'  # Replace with the role you want to assign

# Set up intents
intents = discord.Intents.default()
intents.members = True  # Required for on_member_join
intents.message_content = True  # Needed if using commands

# Create bot instance
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Bot is connected as {bot.user}')

@bot.event
async def on_member_join(member):
    if member.guild.id != GUILD_ID:
        return

    role = discord.utils.get(member.guild.roles, name=ROLE_NAME)
    if role:
        try:
            await member.add_roles(role)
            print(f'✅ Gave role "{ROLE_NAME}" to {member.name}')
        except discord.Forbidden:
            print('❌ Missing permissions to assign roles.')
    else:
        print(f'❌ Role "{ROLE_NAME}" not found.')

bot.run(TOKEN)
