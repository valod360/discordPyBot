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



class pendu(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



 

