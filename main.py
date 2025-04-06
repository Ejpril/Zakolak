import discord
from discord.ext import commands
from discord import app_commands

GUILD_ID = discord.Object(id=1358019972902686852)

class Client(commands.Bot):
    async def on_ready(self):
        print(f'no kurwa siema jestm {self.user}')

        try:
            guild = discord.Object(id=) # id dev serwera 
            synced = await self.tree.sync(guild=guild)
            print(f"Zsynchronizowano {len(synced)} komend do {guild.id}")
        except Exception as e:
            print(f"Synchronizacja wyjebana: {e}")

intents = discord.Intents.default()
intents.message_content = True
client = Client(command_prefix="!", intents=intents)

@client.tree.command(name="elo", description="no elo", guild=GUILD_ID)
async def sayHello(interaction: discord.Interaction):
    await interaction.response.send_message("sieeema")


client.run('') # token
