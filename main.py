import discord
from discord import Interaction, app_commands
import time
import json
import datetime
from abc import ABC
import asyncio
import dateutil.parser
import math
import sqlite3
import typing
import discord.ext
from discord.ext import commands
from datetime import date
from typing import Union
from emoji import UNICODE_EMOJI
today = date.today()


intents = discord.Intents.default()
intents.message_content = True
intents.members=True



bot=discord.ext.commands.Bot("!",activity = discord.Activity(type=discord.ActivityType.playing, name=f"DM to Contact mods"),intents=intents)

tree = bot.tree
from typing import Literal



@bot.event
async def on_ready():
    print(f'Connected as {bot.user}')
    app_commands=await tree.sync()
    for command in app_commands:
        print(command)

@bot.event
async def on_message(message):


    if not isinstance(message.channel, discord.DMChannel) or message.author.id == bot.user.id:
        return

    channel = bot.get_channel(999999999999999999)#Enter the channel ID you want to Send the DM messages 
    if not channel:
        return

    main_guild = bot.get_guild(999999999999999999)#Enter the Guild ID of the main server
    if not main_guild:
        author = message.author
    else:
        author = main_guild.get_member(message.author.id)
        if not author:
            author = message.author

    content = message.clean_content

    if message.attachments != None:
        files = message.attachments
        embed=discord.Embed(title=message.author,description=message.content)
        embed.set_thumbnail(url=message.author.avatar)
        embed.set_footer(text=message.author.id)
        await channel.send(embed=embed)
        await message.add_reaction('📬')

        for file in files:
            await channel.send(content=f">>> {message.author}(`{message.author.id}`)\n{file.url}")
    if message.attachments==None:
        if len(content[2000:]) > 0:
            embed = discord.Embed(title=None,description=content[2000:])
        else:
            embed = discord.Embed(title=None,description=message.content)
        embed.set_author(name=message.author.display_name)
        embed.timestamp = message.created_at
        embed.set_footer(text='User ID: {}'.format(author.id))
        embed.color = author.color

        embed.add_field(name="Message", value=content[:2000] or "blank")
        if len(content[2000:]) > 0:
            embed.add_field(name="(Continued)", value=content[1000:])

        await channel.send(content=f"{message.author.id}", embed=embed)

        try:
            await message.add_reaction('📬')
        except discord.ext.commands.errors.CommandInvokeError:
            await message.channel.send('📬')

@tree.command(description="Shows the Bot Latency")#Normal Ping command
async def ping(interaction: discord.Interaction):
  before = time.monotonic()
  before_ws = int(round(bot.latency * 1000, 1))
  await interaction.response.send_message(f"🏓Pong!! {round(bot.latency * 1000)}ms\n⌛WebSocket {before_ws}ms")





@tree.command(description="DM the users") 
@app_commands.checks.has_any_role(999999999999999999, 999999999999999999, 999999999999999999) #Enter the ROLE ID's you want to give access to the report command
@app_commands.describe(member="The guy who you want to DM",reason='Describe the issue',file="send some images here")
async def report(interaction:discord.Interaction,member:discord.Member,reason:str,file:discord.Attachment=None):
    await interaction.response.send_message("Sending the packets...")

    if interaction.guild.id==681336886891118688: #enter the Guild ID of the main server
                if file!=None:
                    await file.save("report.png",seek_begin=True, use_cached=False)
                embed=discord.Embed(title=f"📬 TICKET",color=0x000000,timestamp=datetime.datetime.utcnow(),description=f"**{reason}**")

                    
                if file!=None:
                            try:
                                await member.send(content=None,embed=embed,file=discord.File("report.png"))
                                l=[]
                                l.append(discord.File("report.png"))
                                await interaction.edit_original_message(content=f"I delivered the report to the user\n>>> **{reason}**",attachments=l)
            

                            except discord.Forbidden:
                                await interaction.edit_original_message(content="❌ | user has his DM's off")
                if file==None:
                            try:
                                await member.send(content=None,embed=embed)
                                await interaction.edit_original_message(content=f"I delivered the report to the user\n>>> **{reason}**")

                            except discord.Forbidden:
                                await interaction.edit_original_message(content="❌ | user has his DM's off")


@report.error
async def report_error(interaction: discord.Interaction,error: app_commands.Command.error):
        if isinstance(error, app_commands.BotMissingPermissions):
            message=f"❌ | I don't have the required permissions, please enable `{error.missing_permissions[0]}`"
            await interaction.response.send_message(message,ephemeral=True)


        elif isinstance(error, app_commands.MissingPermissions):
            message = f"❌ | You are missing the required permissions to run this command! {error.missing_permissions[0]}"
            await interaction.response.send_message(message,ephemeral=True)

        elif isinstance(error, app_commands.MissingAnyRole):
            message = f"❌ | You are missing the required roles to run this command!"
            await interaction.response.send_message(message,ephemeral=True)

        elif isinstance(error, app_commands.TransformerError):
            message = str(error)
            await interaction.response.send_message(message,ephemeral=True)

with open('config.json') as f:
    d=json.load(f)
    bot.run(d["token"])