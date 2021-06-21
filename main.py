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

#==========ПЕРЕМЕННЫЕ==========#

owner_id = 431150587334361098
intents = discord.Intents.default()
intents.members = True
intents.guilds = True
client = commands.Bot(command_prefix="f?", intents=intents)
client.remove_command("help")

#==========COGS==========#

@client.command(aliases=['LOAD'])
@commands.is_owner()
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")
    emb = discord.Embed(title=".load", description='Cog загружен', color=0x000000)
    emb.set_author(name="SAMP Files")
    await ctx.send(embed=emb)

@client.command(aliases=['UNLOAD'])
@commands.is_owner()
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    emb = discord.Embed(title=".unload", description='Cog выгружен', color=0x000000)
    emb.set_author(name="SAMP Files")
    await ctx.send(embed=emb)

@client.command(aliases=['RELOAD'])
@commands.is_owner()
async def reload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    client.load_extension(f"cogs.{extension}")
    emb = discord.Embed(title=".reload" ,description='Cog перезагружен', color=0x000000)
    emb.set_author(name="SAMP Files")
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
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"f?help | 0.1.9 | {len(client.guilds)}/100"))

@client.command()
@commands.guild_only()
async def help(ctx):
    embed=discord.Embed(title="f?help", description="Список команд бота", color=0xffa500)
    embed.set_author(name="SAMP Files")
    embed.add_field(name="f?gta", value="Ссылка на GTA San Andreas", inline=True) # +
    embed.add_field(name="f?samp", value="Ссылка на SA:MP", inline=True) # +
    embed.add_field(name="f?cleo", value="Ссылка на CLEO Library", inline=True) # +
    embed.add_field(name="f?sfuscs", value="Ссылка на SAMPFUNCS", inline=True) # +
    embed.add_field(name="f?moonloader", value="Ссылка на MoonLoader", inline=True) # +
    embed.add_field(name="f?asiloader", value="Ссылка на Asi Loader", inline=True) # +
    embed.add_field(name="f?add", value="Добавляет Ваш сервер в общий список", inline=True) # +
    embed.add_field(name="f?slist", value="Список серверов", inline=True) # +
    embed.add_field(name="f?delete", value="Удаление Вашего сервера из списка", inline=True)
    embed.add_field(name="f?addhelp", value="Помощь по команде f?add", inline=True) # +
    embed.set_footer(text="Автор бота - Ykpauneu#1625") # +
    await ctx.send(embed=embed)

@client.command()
@commands.guild_only()
async def addhelp(ctx):
    embed=discord.Embed(title=".addhelp", color=0xffa500)
    embed.set_author(name="SAMP Files")
    embed.set_thumbnail(url="https://i.imgur.com/ArmoJMR.png")
    embed.add_field(name="1.", value="Введите IP Сервера (без :port)", inline=False)
    embed.add_field(name="2.", value="Напишите port через пробел ", inline=False)
    embed.add_field(name="3.", value="Напишите название сервера", inline=False)
    embed.add_field(name="Образец:", value="f?add revo.samp-rp.ru 7777 Samp-Rp.Ru", inline=False)
    embed.set_footer(text="Сервера, которые Вы ввели в f?add будут видны везде, где есть бот SAMP Files")
    await ctx.send(embed=embed)

@client.command()
@commands.guild_only()
async def gta(ctx):
    embed=discord.Embed(title="f?gta", url="https://thelastgame.ru/grand-theft-auto-san-andreas/", description="Ссылка на GTA San Andreas", color=0xffa500)
    embed.set_author(name="SAMP Files")
    await ctx.send(embed=embed)

@client.command()
@commands.guild_only()
async def samp(ctx):
    embed=discord.Embed(title="f?samp", url="https://sa-mp.com/download.php", description="Ссылка на SA:MP", color=0xffa500)
    embed.set_author(name="SAMP Files")
    await ctx.send(embed=embed)

@client.command()
@commands.guild_only()
async def cleo(ctx):
    embed=discord.Embed(title="f?cleo", url="https://cleo.li/ru/index.html", description="Ссылка на CLEO Library", color=0xffa500)
    embed.set_author(name="SAMP Files")
    await ctx.send(embed=embed)

@client.command()
@commands.guild_only()
async def asiloader(ctx):
    embed=discord.Embed(title="f?asiloader", url="https://libertycity.ru/files/gta-san-andreas/84312-silents-asi-loader-1.3.html", description="Ссылка на Asi Loader")
    embed.set_author(name="SAMP Files")
    await ctx.send(embed=embed)

@client.command()
@commands.guild_only()
async def moonloader(ctx):
    embed=discord.Embed(title="f?moonloader", url="https://www.blast.hk/threads/13305/", description="Ссылка на MoonLoader")
    embed.set_author(name="SAMP Files")
    await ctx.send(embed=embed)

@client.command()
@commands.guild_only()
async def sfuscs(ctx):
    embed=discord.Embed(title="f?sfuscs", url="https://www.blast.hk/threads/17/", description="Ссылка на SAMPFUNCS")
    embed.set_author(name="SAMP Files")
    await ctx.send(embed=embed)

@client.command()
@commands.is_owner()
async def guilds(ctx):
    for i in client.guilds:
        await ctx.send(f"\n{i}\n")

@client.command()
@commands.guild_only()
async def add(ctx, ip, port, *, opisanie):
    if len(opisanie) > 25:
        emb = discord.Embed(title='Ошибка',description = "Укажите меньше 25 символов", color=0xff0000)
        emb.set_author(name="SAMP Files")
        await ctx.send(embed = emb)
        return
    else:
        try:
            sampdb = await aiosqlite.connect("reactData.db")
            await sampdb.execute('INSERT OR ROLLBACK INTO ServerList (user_added, ip, port, opisanie) VALUES (?,?,?,?)', (ctx.author.name, ip, port, opisanie))
            await sampdb.commit()
            embed=discord.Embed(title="f?add", color=0xffa500)
            embed.set_author(name="SAMP Files")
            embed.add_field(name="IP:", value=ip, inline=True)
            embed.add_field(name="Port:", value=port, inline=True)
            embed.add_field(name="Описание:", value=opisanie, inline=True)
            await ctx.send(embed=embed)
        except:
            emb = discord.Embed(title='Ошибка',description = "Ip/Описание уже есть в списке", color=0xff0000)
            emb.set_author(name="SAMP Files")
            await ctx.send(embed = emb)

@client.command()
@commands.guild_only()
async def slist(ctx):
    sampdb = await aiosqlite.connect("reactData.db")
    index = 0
    embed=discord.Embed(title="Список серверов:", description="", color=0xffa500)
    embed.set_author(name="SAMP Files")
    msg = await ctx.send(embed=embed)
    async with sampdb.execute(f"SELECT user_added, ip, port, opisanie FROM ServerList") as cursor:
        async for entry in cursor:
            index += 1
            user_added, ip, port, opisanie = entry
            embed.description += f"{user_added} | {ip}:{port} | {opisanie}\n"
        await msg.edit(embed=embed)

@client.command()
@commands.guild_only()
async def delete(ctx)
    sampdb = await aiosqlite.connect("reactData.db")
    try:
        await sampdb.execute("DELETE FROM ServerList WHERE user_added = ?", (ctx.author.id))
        embed=discord.Embed(title="f?delete", color=0xffa500)
        embed.set_author(name="SAMP Files")
        embed.add_field(name="Пользователь:", value=ctx.author.mention, inline=True)
        embed.add_field(name="Статус:", value="Сервер удалён из списка", inline=True)
        await ctx.send(embed=embed)
    except:
        emb = discord.Embed(title='Ошибка',description = "Вы не добавляли сервер", color=0xff0000)
        emb.set_author(name="SAMP Files")
        await ctx.send(embed = emb)

@client.command()
@commands.guild_only()
@commands.is_owner()
async def deletemod(ctx, *, inputip)
    sampdb = await aiosqlite.connect("reactData.db")
    try:
        await sampdb.execute("DELETE FROM ServerList WHERE ip = ?", (inputip))
        embed=discord.Embed(title="f?delete", color=0xffa500)
        embed.set_author(name="SAMP Files")
        embed.add_field(name="Статус:", value="Сервер удалён из списка", inline=True)
        await ctx.send(embed=embed)
    except:
        emb = discord.Embed(title='Ошибка',description = "Этого сервера нет в списке", color=0xff0000)
        emb.set_author(name="SAMP Files")
        await ctx.send(embed = emb)


#==========КЛИЕНТ==========#

client.loop.create_task(initialize())
client.run("")
asyncio.run(sampdb.close())

#==========КОНЕЦ==========#