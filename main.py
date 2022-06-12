from pydoc import cli 
import sys
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.all()

client = commands.Bot(command_prefix="?",intents = intents, help_command=None)

@client.event
async def on_ready():
    print("Current Version:-", sys.version)
    print("finished...")

@client.command()
@commands.has_permissions(manage_roles=True)
async def asignRole(ctx, roleId : discord.Role):
    server = client.get_guild(SERVER_ID)
    role2 = discord.utils.get(server.roles, id = ROLE_ID) #Role, which gets asigned to all people with the pinged role
    print("Role asigned to: ")
    for guild in client.guilds:
        for member in guild.members:
            if roleId in member.roles:
                print(member.name)
                await member.add_roles(role2)  

client.run("TOKEN")
