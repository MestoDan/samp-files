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
import nekos
import sys
from samp_client.client import SampClient

#==========КОД==========#

class ErrorsCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            return

        elif isinstance(error, commands.MissingRequiredArgument):
            emb = discord.Embed(title='Ошибка',description = "Отсутствует требуемый аргумент (`commands.MissingRequiredArgument`)", color=0xff0000)
            emb.set_author(name="SAMP Files")
            await ctx.send(embed = emb)

        elif isinstance(error, commands.MissingPermissions):
            emb = discord.Embed(title='Ошибка',description = "Отсутствует разрешение (`commands.MissingPermissions`)", color=0xff0000)
            emb.set_author(name="SAMP Files")
            await ctx.send(embed = emb)

        elif isinstance(error, commands.DisabledCommand):
            emb = discord.Embed(title='Ошибка',description = "Команда отключена (`commands.DisabledCommand`)", color=0xff0000)
            emb.set_author(name="SAMP Files")
            await ctx.send(embed = emb)

        elif isinstance(error, commands.UserInputError):
            emb = discord.Embed(title='Ошибка',description = "Команда неправильно введена (`commands.UserInputError`)", color=0xff0000)
            emb.set_author(name="SAMP Files")
            await ctx.send(embed = emb)

        elif isinstance(error, commands.CheckFailure):
            emb = discord.Embed(title='Ошибка',description = "Отсутствуют необходимые права (`commands.CheckFailure`)", color=0xff0000)
            emb.set_author(name="SAMP Files")
            await ctx.send(embed = emb)

        elif isinstance(error, commands.BadArgument):
            emb = discord.Embed(title='Ошибка',description = "Неправильный аргумент (`commands.BadArgument`)", color=0xff0000)
            emb.set_author(name="SAMP Files")
            await ctx.send(embed = emb)

#==========ЗАГРУЗКА==========#

def setup(client):      
    client.add_cog(ErrorsCog(client))
    print("ErrorsCog - загружен")

#==========КОНЕЦ==========#