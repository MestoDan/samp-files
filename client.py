#==========ИМПОРТЫ==========#

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
import keep_alive

#==========ПЕРЕМЕННЫЕ==========#

owner_id = 431150587334361098
intents = discord.Intents.default()
intents.members = True
intents.guilds = True
client = commands.Bot(command_prefix="f?", intents=intents, activity=discord.Activity(type=discord.ActivityType.watching, name="f?help | Версия: 0.1.6"))
client.remove_command("help")

#==========COGS==========#

@client.command(aliases=['LOAD'])
@commands.is_owner()
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")
    emb = discord.Embed(title=".load", description='Cog загружен', color=0x000000)
    emb.set_author(name="SAMP Files", url="https://samp-files.ttpoctou7pok.repl.co/")
    await ctx.send(embed=emb)

@client.command(aliases=['UNLOAD'])
@commands.is_owner()
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    emb = discord.Embed(title=".unload", description='Cog выгружен', color=0x000000)
    emb.set_author(name="SAMP Files", url="https://samp-files.ttpoctou7pok.repl.co/")
    await ctx.send(embed=emb)

@client.command(aliases=['RELOAD'])
@commands.is_owner()
async def reload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    client.load_extension(f"cogs.{extension}")
    emb = discord.Embed(title=".reload" ,description='Cog перезагружен', color=0x000000)
    emb.set_author(name="SAMP Files", url="https://samp-files.ttpoctou7pok.repl.co/")
    await ctx.send(embed=emb)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

#==========ИНИЦИАЛИЗАЦИЯ .db==========#

async def initialize():
    await client.wait_until_ready()
    sampdb = await aiosqlite.connect("reactData.db")
    await sampdb.execute("CREATE TABLE IF NOT EXISTS ServerList (user_added int, ip text, port int, opisanie text, PRIMARY KEY (user_added, ip, opisanie))")
    await sampdb.commit()

#==========КОД==========#

@client.event
async def on_ready():
    print('Бот загружен как {0.user}'.format(client))
    print('Автор Ykpauneu#1625')
    print('---')

@client.command()
async def help(ctx):
    embed=discord.Embed(title="f?help", description="Список команд бота", color=0xffa500)
    embed.set_author(name="SAMP Files", url="https://samp-files.ttpoctou7pok.repl.co/")
    embed.add_field(name="f?gta", value="Ссылка на GTA San Andreas [1.0]", inline=True) # +
    embed.add_field(name="f?samp", value="Ссылка на SA:MP [0.3.7-R1]", inline=True) # +
    embed.add_field(name="f?cleo", value="Ссылка на CLEO Library [v4.1.0]", inline=True) # +
    embed.add_field(name="f?sfuscs", value="Ссылка на SAMPFUNCS [5.4.1]", inline=True) # +
    embed.add_field(name="f?moonloader", value="Ссылка на MoonLoader [v.026.5-beta]", inline=True) # +
    embed.add_field(name="f?asiloader", value="Ссылка на Asi Loader [1.3]", inline=True) # +
    embed.add_field(name="f?add", value="Добавляет Ваш сервер в общий список", inline=True) # +
    embed.add_field(name="f?slist", value="Список серверов", inline=True) # +
    embed.add_field(name="f?addhelp", value="Помощь по команде f?add", inline=True) # +
    embed.set_footer(text="Автор бота - Ykpauneu#1625") # +
    await ctx.send(embed=embed)

@client.command()
async def addhelp(ctx):
    embed=discord.Embed(title=".addhelp", color=0xffa500)
    embed.set_author(name="SAMP Files", url="https://samp-files.ttpoctou7pok.repl.co/")
    embed.set_thumbnail(url="https://i.imgur.com/ArmoJMR.png")
    embed.add_field(name="1.", value="Введите IP Сервера (без :port)", inline=False)
    embed.add_field(name="2.", value="Напишите port через пробел ", inline=False)
    embed.add_field(name="3.", value="Напишите название сервера", inline=False)
    embed.add_field(name="Образец:", value="f?add revo.samp-rp.ru 7777 Samp-Rp.Ru", inline=False)
    embed.set_footer(text="Сервера, которые Вы ввели в f?add будут видны везде, где есть бот SAMP Files")
    await ctx.send(embed=embed)

@client.command()
async def gta(ctx):
    embed=discord.Embed(title="f?gta", url="https://thelastgame.ru/grand-theft-auto-san-andreas/", description="Ссылка на GTA San Andreas [1.0]", color=0xffa500)
    embed.set_author(name="SAMP Files", url="https://samp-files.ttpoctou7pok.repl.co/")
    await ctx.send(embed=embed)

@client.command()
async def samp(ctx):
    embed=discord.Embed(title="f?samp", url="https://disk.yandex.ru/d/TDL7kJxUHzCuaQ", description="Ссылка на SA:MP [0.3.7-R1]", color=0xffa500)
    embed.set_author(name="SAMP Files", url="https://samp-files.ttpoctou7pok.repl.co/")
    await ctx.send(embed=embed)

@client.command()
async def cleo(ctx):
    embed=discord.Embed(title="f?cleo", url="https://disk.yandex.ru/d/RChk4J2no2LvaA", description="Ссылка на CLEO Library [v4.1.0]", color=0xffa500)
    embed.set_author(name="SAMP Files", url="https://samp-files.ttpoctou7pok.repl.co/")
    await ctx.send(embed=embed)

@client.command()
async def asiloader(ctx):
    embed=discord.Embed(title="f?asiloader", url="https://disk.yandex.ru/d/O8Tgr2tVo--c9g", description="Ссылка на Asi Loader [1.3]")
    embed.set_author(name="SAMP Files", url="https://samp-files.ttpoctou7pok.repl.co/")
    await ctx.send(embed=embed)

@client.command()
async def moonloader(ctx):
    embed=discord.Embed(title="f?moonloader", url="https://disk.yandex.ru/d/kN-uMUyHP--3SA", description="Ссылка на MoonLoader [v.026.5-beta]")
    embed.set_author(name="SAMP Files", url="https://samp-files.ttpoctou7pok.repl.co/")
    await ctx.send(embed=embed)

@client.command()
async def sfuscs(ctx):
    embed=discord.Embed(title="f?sfuscs", url="https://disk.yandex.ru/d/Gc97XIIRHKz-fQ", description="Ссылка на SAMPFUNCS [5.4.1]")
    embed.set_author(name="SAMP Files", url="https://samp-files.ttpoctou7pok.repl.co/")
    await ctx.send(embed=embed)

@client.command()
@commands.is_owner()
async def guilds(ctx):
    for i in client.guilds:
        await ctx.send(f"\n{i}\n")

@client.command()
async def add(ctx, ip, port, opisanie):
    sampdb = await aiosqlite.connect("reactData.db")
    await sampdb.execute('INSERT INTO ServerList (user_added, ip, port, opisanie) VALUES (?,?,?,?)', (ctx.author.id, ip, port, opisanie))
    await sampdb.commit()
    embed=discord.Embed(title="f?add", color=0xffa500)
    embed.set_author(name="SAMP Files", url="https://samp-files.ttpoctou7pok.repl.co/")
    embed.add_field(name="IP:", value=ip, inline=True)
    embed.add_field(name="Port:", value=port, inline=True)
    embed.add_field(name="Описание:", value=opisanie, inline=True)
    await ctx.send(embed=embed)

@client.command()
async def slist(ctx):
    sampdb = await aiosqlite.connect("reactData.db")
    index = 0
    embed=discord.Embed(title="Список серверов:", description="", color=0xffa500)
    embed.set_author(name="SAMP Files", url="https://samp-files.ttpoctou7pok.repl.co/")
    msg = await ctx.send(embed=embed)
    async with sampdb.execute(f"SELECT user_added, ip, port, opisanie FROM ServerList ORDER BY ip") as cursor:
        async for entry in cursor:
            index += 1
            user_added, ip, port, opisanie = entry
            user_name = ctx.guild.get_member(user_added)
            embed.description += f"{index}. Добавил - {user_name} | IP - {ip}:{port} | Описание - {opisanie}\n"
        await msg.edit(embed=embed)

#==========КЛИЕНТ==========#

keep_alive.keep_alive()
client.loop.create_task(initialize())
client.run("YOUR TOKEN")
asyncio.run(sampdb.close())

#==========КОНЕЦ==========#