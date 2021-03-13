# Половина import не нужны, кидал их сюда  с YUSB


import discord
from discord.ext import commands
import requests
import sqlite3
from discord.ext.commands import Bot
from discord import Game
from discord import Embed
import time
import asyncio
from discord import utils
from discord import Activity, ActivityType
from discord.ext.commands import errors
import datetime
import random
import json
import math
import os
import aiosqlite
import aiofiles
import aiohttp
import pytz
from datetime import datetime
import nekos


client = commands.Bot(command_prefix="f?")
client.remove_command("help")

@client.event
async def on_ready():
    print('Бот загружен как {0.user}'.format(client))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="f?help"))
    print('Статус работает')
    print('Автор Ykpauneu#1625')
    print('---')




@client.command()
async def help(ctx):
	embed=discord.Embed(title="f?help", description="Список команд бота", color=0xffa500)
	embed.set_author(name="SAMP Files")
	embed.add_field(name="f?gta", value="Ссылка на GTA San Andreas [1.0]", inline=True) # +
	embed.add_field(name="f?samp", value="Ссылка на SA:MP [0.3.7-R1]", inline=True) # +
	embed.add_field(name="f?cleo", value="Ссылка на CLEO Library [v4.1.0]", inline=True) # +
	embed.add_field(name="f?sfuscs", value="Ссылка на SAMPFUNCS [5.4.1]", inline=True) # +
	embed.add_field(name="f?moonloader", value="Ссылка на MoonLoader [v.026.5-beta]", inline=True) # +
	embed.add_field(name="f?asiloader", value="Ссылка на Asi Loader [1.3]", inline=True) # +
	embed.set_footer(text="Автор бота - Ykpauneu#1625 / Версия - 0.1c") # +
	await ctx.send(embed=embed)

@client.command()
async def gta(ctx):
	embed=discord.Embed(title="f?gta", url="https://thelastgame.ru/grand-theft-auto-san-andreas/", description="Ссылка на GTA San Andreas [1.0]", color=0xffa500)
	embed.set_author(name="SAMP Files")
	await ctx.send(embed=embed)


@client.command()
async def samp(ctx):
	embed=discord.Embed(title="f?samp", url="https://disk.yandex.ru/d/TDL7kJxUHzCuaQ", description="Ссылка на SA:MP [0.3.7-R1]", color=0xffa500)
	embed.set_author(name="SAMP Files")
	await ctx.send(embed=embed)

@client.command()
async def cleo(ctx):
	embed=discord.Embed(title="f?cleo", url="https://disk.yandex.ru/d/RChk4J2no2LvaA", description="Ссылка на CLEO Library [v4.1.0]", color=0xffa500)
	embed.set_author(name="SAMP Files")
	await ctx.send(embed=embed)

@client.command()
async def asiloader(ctx):
	embed=discord.Embed(title="f?asiloader", url="https://disk.yandex.ru/d/O8Tgr2tVo--c9g", description="Ссылка на Asi Loader [1.3]")
	embed.set_author(name="SAMP Files")
	await ctx.send(embed=embed)

@client.command()
async def moonloader(ctx):
	embed=discord.Embed(title="f?moonloader", url="https://disk.yandex.ru/d/kN-uMUyHP--3SA", description="Ссылка на MoonLoader [v.026.5-beta]")
	embed.set_author(name="SAMP Files")
	await ctx.send(embed=embed)

@client.command()
async def sfuscs(ctx):
	embed=discord.Embed(title="f?sfuscs", url="https://disk.yandex.ru/d/Gc97XIIRHKz-fQ", description="Ссылка на SAMPFUNCS [5.4.1]")
	embed.set_author(name="SAMP Files")
	await ctx.send(embed=embed)








client.run("TOKEN HERE")