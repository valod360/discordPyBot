#!/usr/local/bin/python
#coding=utf-8
#importation de discord
import os
import json
import discord
import random
import asyncio
import time
#ajout composant
from discord.ext import tasks, commands
from discord.utils import get
from discord.ext.commands import has_permissions, Greedy, MissingPermissions, check
from discord import User
import datetime
import json
import _sqlite3

money = {}

class argent(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def cmbargent(self, ctx, deteneur: discord.Member):
        membre = deteneur.mention
        id = deteneur.id
        with open('money.json') as json_file:
            data = json.load(json_file)
            await ctx.send('{} a {} $'.format(membre, data[f"{id}"]))

    @commands.command()
    async def rajou(self, ctx):
        membre = ctx.author.mention
        id = ctx.author.id

        with open('money.json', 'a') as f:
            json.dump(money, f, ensure_ascii=False, sort_keys = False, indent=2)

        if id not in money:
            money[id] = 100

        money[id] += 100

        await ctx.send('ajout de 100$ au compte de {}'.format(membre))




