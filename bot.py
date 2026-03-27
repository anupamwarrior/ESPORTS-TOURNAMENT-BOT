import discord
from discord.ext import commands
from discord import app_commands
from config import TOKEN, ADMIN_ROLE
from rooms import generate_room
from maps import next_map
from slots import assign_slots
from embeds import match_embed

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)
tree = bot.tree

def is_admin(interaction):
    return any(role.name == ADMIN_ROLE for role in interaction.user.roles)

@tree.command(name="start_match")
async def start_match(interaction: discord.Interaction):
    if not is_admin(interaction):
        await interaction.response.send_message("❌ Admin only")
        return

    room_id, password = generate_room()
    map_name = next_map()
    slots = assign_slots()

    embed = match_embed(room_id, password, map_name)
    await interaction.response.send_message(embed=embed)

@bot.event
async def on_ready():
    await tree.sync()
    print("ULTRA SYSTEM READY")

bot.run(TOKEN)
