#!/usr/local/bin/python
# coding=utf-8
# importation de discord
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
import morpion
import pendu
import argent
import mongo


#instance

bot = commands.Bot(command_prefix='$')
with open("insulte.txt") as file: #les insulte qui contien les mot blacklister
    insulte = [insulte.strip().lower() for insulte in file.readline()]

win = {}

bot.remove_command('help')

bot.add_cog(morpion.morpion(bot))
bot.add_cog(pendu.pendu(bot))
bot.add_cog(argent.argent(bot))
bot.add_cog(mongo.mongo(bot))


#pour voir quand le bot est pret allumer
@bot.event
async def on_ready():
    print("bot pret :paz:")
    await bot.change_presence(status=discord.Status.online,
            activity=discord.Game("$command"))



#event pour dire que le calcule est en cours
#@bot.event
#async def on_message(message):
    #if message.content == '$msgcounter':
    #    embed = discord.Embed(
    #        title= 'msgcounter',
    #        colour= discord.Colour.blue()
    #    )
    #    embed.set_footer(text='By Discounter for {} • {}:{}'.format(message.author, datetime.datetime.now().hour, datetime.datetime.now().minute))
    #    embed.set_author(name='Discounter', icon_url="https://cdn.discordapp.com/attachments/798536899215884288/798599051712397392/logo_4.png")
    #    embed.add_field(name='Counting in progress...please wait.', value="Don't worry, it can take some time. (~30mn for 500k messages)")
    #    await message.channel.send(embed=embed)





    #await bot.process_commands(message)



#la commande help
@bot.command()
async def command(ctx):
    embed = discord.Embed(
        colour= discord.Colour.dark_gray()
    )

    embed.set_footer(text='By Discounter for {} • {}:{}'.format(str(ctx.author), datetime.datetime.now().hour, datetime.datetime.now().minute))
    embed.set_author(name='Discounter', icon_url='https://cdn.discordapp.com/attachments/798536899215884288/798599051712397392/logo_4.png')
    embed.add_field(name='$command', value="Displays the help panel", inline=False)
    embed.add_field(name='$msgcounter', value="Lets you know how many messages there are in a channel (admin only)", inline=False)
    embed.add_field(name='$hot', value="Makes a coin flip to know if it's head or tail", inline=False)
    embed.add_field(name='$delete', value="Will delete the 10 last messages in a channel (admin only)", inline=False)
    embed.add_field(name='$purge', value="Will purge a channel of all its messages (admin only : be careful!)", inline=False)
    embed.add_field(name='$tictac', value="it will doo a tictactoe with your buddy")

    await ctx.send(embed=embed)

#pour le systeme de message
@bot.command()
@commands.has_permissions(administrator=True)
async def msgcounter(ctx, channel: discord.TextChannel=None):

    embed = discord.Embed(
        title='msgcounter' ,
        colour=discord.Colour.blue()
    )
    embed.set_footer(text='By Discounter for {} • {}:{}'.format(str(ctx.author), datetime.datetime.now().hour, datetime.datetime.now().minute))
    embed.set_author(name='Discounter', icon_url="https://cdn.discordapp.com/attachments/798536899215884288/798599051712397392/logo_4.png")
    embed.add_field(name='Counting in progress...please wait.', value="Don't worry, it can take some time. (~30mn for 500k messages)")
    await ctx.send(embed=embed)


    channel = channel or ctx.channel
    compte = 0
    async for _ in channel.history(limit=None):
        compte += 1
    # await ctx.send("Il y a {} messages dans {}".format(compte, channel.mention))

    embed = discord.Embed(
        title="msgcounter",
        colour=discord.Colour.blue()
    )
    embed.set_footer(text='By Discounter for {} • {}:{}'.format(str(ctx.author), datetime.datetime.now().hour, datetime.datetime.now().minute))
    embed.set_author(name='Discounter', icon_url="https://cdn.discordapp.com/attachments/798536899215884288/798599051712397392/logo_4.png")
    embed.add_field(name='Results', value=("There are {} messages in {}".format(compte, channel.mention)), inline=False)
    await ctx.send(embed=embed)






#pour le systeme de comptage mais avec mention
@bot.command()
async def hot(ctx):
    solution = ["pile", "face"]
    resultat = random.choice(solution)


    if resultat == "pile":
        embed = discord.Embed(
            title= "Head or Tail",
            colour= discord.Colour.orange()
        )
        embed.set_footer(text='By Discounter for {} • {}:{}'.format(str(ctx.author), datetime.datetime.now().hour, datetime.datetime.now().minute))
        embed.set_author(name='Discounter', icon_url="https://cdn.discordapp.com/attachments/798536899215884288/798599051712397392/logo_4.png")
        embed.add_field(name='results', value=("The coin is on Tail"), inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/799306434961342464/799306455592861696/piece_pile.png")
        await ctx.send(embed=embed)

    else:
        embed = discord.Embed(
            title= "Head or Tail",
            colour= discord.Colour.orange()
        )
        embed.set_footer(text='By Discounter for {} • {}:{}'.format(str(ctx.author), datetime.datetime.now().hour, datetime.datetime.now().minute))
        embed.set_author(name='Discounter', icon_url="https://cdn.discordapp.com/attachments/798536899215884288/798599051712397392/logo_4.png")
        embed.add_field(name='results', value=("The coin is on Head"), inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/799306434961342464/799306468062920764/piece_face.png")
        await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(administrator=True)
async def delete(ctx, amount = 11):
    await ctx.channel.purge(limit=amount)

@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def purge(ctx, amount=9999999):

    await ctx.send("Are you REALLY sure you want to purge the whole channel? Say 'yes' or 'no' if you still want or not to do so.")


    def check(m):

        return m.author.id == ctx.author.id

    reponse = await bot.wait_for('message', check=check)

    choisi = int(reponse.content)

    if choisi == "yes":
        await ctx.channel.purge(limit=amount)
    elif choisi == "no":
        await ctx.send("The channel was not purged.")

    else:
        await ctx.send("An error occured : the channel could not be purged.")






@bot.command()
async def win(ctx, joueur: discord.Member):
    joueur = joueur.mention
    await ctx.send(joueur[win])





#giver le token
token = "Nzk4MzQ2ODYyNjkxNDgzNjU4.X_zsdA.4Itg2FpjpFuJbMpD3f1Ep79K8I8"

print("lancement du bot... ")

#connection du bot
bot.run(token)















































