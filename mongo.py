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
import pymongo
from pymongo import MongoClient

class mongo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def rajout(self, ctx):
        mongo_url = "mongodb+srv://valod:Fritzies360@cluster0.o4q6e.mongodb.net/money?retryWrites=true&w=majority&authSource=admin"
        cluster = MongoClient(mongo_url)
        db = cluster["money"]
        collection = db["new"]
        author = ctx.author.mention
        author_id = ctx.author.id
        guild_id = ctx.guild.id
        ping_cm = {"command":1}
        ping_cmm = {"_id":author_id}
        insertion = {"_id":author_id, "Argent": 100}

        if collection.find_one(ping_cmm) == None:
            collection.insert_one(insertion)
        else:
            collection.update({"_id": author_id}, {"$inc": {"Argent": 100}})






        await ctx.channel.send("rajout de 100$ sur le compte de {}".format(author))


    @commands.command()
    async def cmb(self, ctx):
        mongo_url = "mongodb+srv://valod:Fritzies360@cluster0.o4q6e.mongodb.net/money?retryWrites=true&w=majority&authSource=admin"
        cluster = MongoClient(mongo_url)
        autheur = ctx.author.mention
        db = cluster["money"]
        collection = db["new"]
        author_id = ctx.author.id
        guild_id = ctx.guild.id
        ping_cm = {"command": 1}
        ping_cmm = collection.find_one({"_id": author_id})
        await ctx.send('{} tu possede {}$ sur ton compte'.format(autheur, ping_cmm['Argent']))