import discord

def match_embed(room_id, password, map_name):
    embed = discord.Embed(title="🎮 BGMI MATCH ROOM", color=0xff0000)
    embed.add_field(name="Room ID", value=room_id)
    embed.add_field(name="Password", value=password)
    embed.add_field(name="Map", value=map_name)
    return embed
