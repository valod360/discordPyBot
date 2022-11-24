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



class morpion(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def tictac(self, ctx, joueur: discord.Member):
        joueur1 = ctx.author.mention
        joueur1C = ctx.author.id
        joueur2 = joueur.mention
        joueur2C = joueur.id
        emoji1 = '1️⃣'
        emoji1_croix = False
        emoji1_cercle = False
        emoji2 = '2️⃣'
        emoji2_croix = False
        emoji2_cercle = False
        emoji3 = '3️⃣'
        emoji3_croix = False
        emoji3_cercle = False
        emoji4 = '4️⃣'
        emoji4_croix = False
        emoji4_cercle = False
        emoji5 = '5️⃣'
        emoji5_croix = False
        emoji5_cercle = False
        emoji6 = '6️⃣'
        emoji6_croix = False
        emoji6_cercle = False
        emoji7 = '7️⃣'
        emoji7_croix = False
        emoji7_cercle = False
        emoji8 = '8️⃣'
        emoji8_croix = False
        emoji8_cercle = False
        emoji9 = '9️⃣'
        emoji9_croix = False
        emoji9_cercle = False
        cercle = '⭕'
        cercle_chiffre = 0
        croix = '❌'
        croix_chiffre = 0


        # si on joue contre soient meme
        if joueur1C == joueur2C or joueur2C == joueur1C:
            await ctx.send("you don't have the right to play against you")
            continuer_partie = False
        else:

            await ctx.send(
                "{} challenged {} to a Tic-Tac-Toe game ! It's {} that has to play first. Write 0 when you want to end the game.".format(
                    joueur1, joueur2, joueur1))

            await ctx.send(f"{emoji1} {emoji2} {emoji3}\n"
                           f"{emoji4} {emoji5} {emoji6}\n"
                           f"{emoji7} {emoji8} {emoji9}")

            await ctx.send(f"{joueur1} You have to start the game.")

            i = 1

            continuer_partie = True



            while continuer_partie:

                while i == 1:

                    def check(m):
                        return m.author.id == ctx.author.id

                    reponse = await self.bot.wait_for('message', check=check)

                    choix = str(reponse.content)

                    # if choix > 9:
                    # await ctx.send("Pick a number under 9.")
                    # continue
                    # if choix < 0:
                    # await ctx.send("You cannot pick a number below 0.")
                    # continue



                    # pour la repetition de croix
                    if choix == '1' and emoji1 == croix:
                        await ctx.send("You cannot put a cross there. You gotta pick again {}".format(joueur1))
                        continue

                    if choix == '2' and emoji2 == croix:
                        await ctx.send("You cannot put a cross there. You gotta pick again {}".format(joueur1))
                        continue

                    if choix == '3' and emoji3 == croix:
                        await ctx.send("You cannot put a cross there. You gotta pick again {}".format(joueur1))
                        continue

                    if choix == '4' and emoji4 == croix:
                        await ctx.send("You cannot put a cross there. You gotta pick again {}".format(joueur1))
                        continue

                    if choix == '5' and emoji5 == croix:
                        await ctx.send("You cannot put a cross there. You gotta pick again {}".format(joueur1))
                        continue

                    if choix == '6' and emoji6 == croix:
                        await ctx.send("You cannot put a cross there. You gotta pick again {}".format(joueur1))
                        continue

                    if choix == '7' and emoji7 == croix:
                        await ctx.send("You cannot put a cross there. You gotta pick again {}".format(joueur1))
                        continue

                    if choix == '8' and emoji8 == croix:
                        await ctx.send("You cannot put a cross there. You gotta pick again {}".format(joueur1))
                        continue

                    if choix == '9' and emoji9 == croix:
                        await ctx.send("You cannot put a cross there. You gotta pick again {}".format(joueur1))
                        continue

                    # pour la repetion des cerlcle

                    if choix == '1' and emoji1 == cercle:
                        await ctx.send("You cannot put a cross there. You gotta pick again {}".format(joueur1))
                        continue

                    if choix == '2' and emoji2 == cercle:
                        await ctx.send("You cannot put a cross there. You gotta pick again {}".format(joueur1))
                        continue

                    if choix == '3' and emoji3 == cercle:
                        await ctx.send("You cannot put a cross there. You gotta pick again {}".format(joueur1))
                        continue

                    if choix == '4' and emoji4 == cercle:
                        await ctx.send("You cannot put a cross there. You gotta pick again {}".format(joueur1))
                        continue

                    if choix == '5' and emoji5 == cercle:
                        await ctx.send("You cannot put a cross there. You gotta pick again {}".format(joueur1))
                        continue

                    if choix == '6' and emoji6 == cercle:
                        await ctx.send("You cannot put a cross there. You gotta pick again {}".format(joueur1))
                        continue

                    if choix == '7' and emoji7 == cercle:
                        await ctx.send("You cannot put a cross there. You gotta pick again {}".format(joueur1))
                        continue

                    if choix == '8' and emoji8 == cercle:
                        await ctx.send("You cannot put a cross there. You gotta pick again {}".format(joueur1))
                        continue

                    if choix == '9' and emoji9 == cercle:
                        await ctx.send("You cannot put a cross there. You gotta pick again {}".format(joueur1))
                        continue

                    # le joueur veux mettre fin a la partie

                    if choix == '0':
                        await ctx.send("The game ended.")
                        i = 0
                        continuer_partie = False

                    # pour le match null
                    if croix_chiffre == 5:
                        await ctx.send("It's a draw !")
                        i = 0
                        continuer_partie = False

                    if cercle_chiffre == 5:
                        await ctx.send("It's a draw !")
                        i = 0
                        continuer_partie = False

                    # le tableau de joueur croix
                    if choix == '1':
                        emoji1 = croix
                        await ctx.send(f"{emoji1} {emoji2} {emoji3}\n"
                                       f"{emoji4} {emoji5} {emoji6}\n"
                                       f"{emoji7} {emoji8} {emoji9}")
                        i = i + 1
                        croix_chiffre = croix_chiffre + 1
                        emoji1_croix = True
                        # pour la win du joueur 1
                        if emoji1_croix and emoji2_croix and emoji3_croix == True:
                            await ctx.send("felicitation a {} qui a gagner la game".format(joueur1))
                            continuer_partie = False
                            joueur1[win] = joueur1[win] + 1
                            continue

                        if emoji3_croix and emoji6_croix and emoji9_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji7_croix and emoji8_croix and emoji9_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji1_croix and emoji4_croix and emoji7_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji4_croix and emoji5_croix and emoji6_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji2_croix and emoji5_croix and emoji8_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji1_croix and emoji5_croix and emoji9_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji3_croix and emoji5_croix and emoji7_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        # pour le vaiceur du joueur 2

                        if emoji1_cercle and emoji2_cercle and emoji3_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji3_cercle and emoji6_cercle and emoji9_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji7_cercle and emoji8_cercle and emoji9_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji1_cercle and emoji4_cercle and emoji7_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji4_cercle and emoji5_cercle and emoji6_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji2_cercle and emoji5_cercle and emoji8_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji1_cercle and emoji5_cercle and emoji9_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji3_cercle and emoji5_cercle and emoji7_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        # pour le match null
                        if croix_chiffre == 5:
                            await ctx.send("It's a draw !")
                            i = 0
                            continuer_partie = False

                        if cercle_chiffre == 5:
                            await ctx.send("It's a draw !")
                            i = 0
                            continuer_partie = False

                        if i == 2:
                            await ctx.send("It's your turn, {}.".format(joueur2))
                        else:
                            continuer_partie = False

                    if choix == '2':
                        emoji2 = croix
                        await ctx.send(f"{emoji1} {emoji2} {emoji3}\n"
                                       f"{emoji4} {emoji5} {emoji6}\n"
                                       f"{emoji7} {emoji8} {emoji9}")

                        i = i + 1
                        emoji2_croix = True

                        croix_chiffre = croix_chiffre + 1
                        # pour la win du joueur 1
                        if emoji1_croix and emoji2_croix and emoji3_croix == True:
                            await ctx.send("felicitation a {} qui a gagner la game".format(joueur1))
                            continuer_partie = False
                            joueur1[win] = joueur1[win] + 1
                            continue

                        if emoji3_croix and emoji6_croix and emoji9_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji7_croix and emoji8_croix and emoji9_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji1_croix and emoji4_croix and emoji7_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji4_croix and emoji5_croix and emoji6_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji2_croix and emoji5_croix and emoji8_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji1_croix and emoji5_croix and emoji9_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji3_croix and emoji5_croix and emoji7_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        # pour le vaiceur du joueur 2

                        if emoji1_cercle and emoji2_cercle and emoji3_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji3_cercle and emoji6_cercle and emoji9_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji7_cercle and emoji8_cercle and emoji9_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji1_cercle and emoji4_cercle and emoji7_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji4_cercle and emoji5_cercle and emoji6_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji2_cercle and emoji5_cercle and emoji8_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji1_cercle and emoji5_cercle and emoji9_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji3_cercle and emoji5_cercle and emoji7_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        # pour le match null
                        if croix_chiffre == 5:
                            await ctx.send("It's a draw !")
                            i = 0
                            continuer_partie = False

                        if cercle_chiffre == 5:
                            await ctx.send("It's a draw !")
                            i = 0
                            continuer_partie = False

                        if i == 2:
                            await ctx.send("It's your turn, {}.".format(joueur2))
                        else:
                            continuer_partie = False

                    if choix == '3':
                        emoji3 = croix
                        await ctx.send(f"{emoji1} {emoji2} {emoji3}\n"
                                       f"{emoji4} {emoji5} {emoji6}\n"
                                       f"{emoji7} {emoji8} {emoji9}")

                        i = i + 1
                        croix_chiffre = croix_chiffre + 1
                        emoji3_croix = True
                        # pour la win du joueur 1
                        if emoji1_croix and emoji2_croix and emoji3_croix == True:
                            await ctx.send("felicitation a {} qui a gagner la game".format(joueur1))
                            continuer_partie = False
                            joueur1[win] = joueur1[win] + 1
                            continue

                        if emoji3_croix and emoji6_croix and emoji9_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji7_croix and emoji8_croix and emoji9_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji1_croix and emoji4_croix and emoji7_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji4_croix and emoji5_croix and emoji6_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji2_croix and emoji5_croix and emoji8_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji1_croix and emoji5_croix and emoji9_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji3_croix and emoji5_croix and emoji7_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        # pour le vaiceur du joueur 2

                        if emoji1_cercle and emoji2_cercle and emoji3_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji3_cercle and emoji6_cercle and emoji9_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji7_cercle and emoji8_cercle and emoji9_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji1_cercle and emoji4_cercle and emoji7_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji4_cercle and emoji5_cercle and emoji6_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji2_cercle and emoji5_cercle and emoji8_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji1_cercle and emoji5_cercle and emoji9_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji3_cercle and emoji5_cercle and emoji7_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        # pour le match null
                        if croix_chiffre == 5:
                            await ctx.send("It's a draw !")
                            i = 0
                            continuer_partie = False

                        if cercle_chiffre == 5:
                            await ctx.send("It's a draw !")
                            i = 0
                            continuer_partie = False

                        if i == 2:
                            await ctx.send("It's your turn, {}.".format(joueur2))
                        else:
                            continuer_partie = False

                    if choix == '4':
                        emoji4 = croix
                        await ctx.send(f"{emoji1} {emoji2} {emoji3}\n"
                                       f"{emoji4} {emoji5} {emoji6}\n"
                                       f"{emoji7} {emoji8} {emoji9}")

                        i = i + 1
                        croix_chiffre = croix_chiffre + 1
                        emoji4_croix = True
                        # pour la win du joueur 1
                        if emoji1_croix and emoji2_croix and emoji3_croix == True:
                            await ctx.send("felicitation a {} qui a gagner la game".format(joueur1))
                            continuer_partie = False
                            joueur1[win] = joueur1[win] + 1
                            continue

                        if emoji3_croix and emoji6_croix and emoji9_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji7_croix and emoji8_croix and emoji9_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji1_croix and emoji4_croix and emoji7_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji4_croix and emoji5_croix and emoji6_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji2_croix and emoji5_croix and emoji8_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji1_croix and emoji5_croix and emoji9_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji3_croix and emoji5_croix and emoji7_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        # pour le vaiceur du joueur 2

                        if emoji1_cercle and emoji2_cercle and emoji3_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji3_cercle and emoji6_cercle and emoji9_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji7_cercle and emoji8_cercle and emoji9_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji1_cercle and emoji4_cercle and emoji7_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji4_cercle and emoji5_cercle and emoji6_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji2_cercle and emoji5_cercle and emoji8_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji1_cercle and emoji5_cercle and emoji9_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji3_cercle and emoji5_cercle and emoji7_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        # pour le match null
                        if croix_chiffre == 5:
                            await ctx.send("It's a draw !")
                            i = 0
                            continuer_partie = False

                        if cercle_chiffre == 5:
                            await ctx.send("It's a draw !")
                            i = 0
                            continuer_partie = False

                        if i == 2:
                            await ctx.send("It's your turn, {}.".format(joueur2))
                        else:
                            continuer_partie = False

                    if choix == '5':
                        emoji5 = croix
                        await ctx.send(f"{emoji1} {emoji2} {emoji3}\n"
                                       f"{emoji4} {emoji5} {emoji6}\n"
                                       f"{emoji7} {emoji8} {emoji9}")

                        i = i + 1
                        croix_chiffre = croix_chiffre + 1
                        emoji5_croix = True
                        # pour la win du joueur 1
                        if emoji1_croix and emoji2_croix and emoji3_croix == True:
                            await ctx.send("felicitation a {} qui a gagner la game".format(joueur1))
                            continuer_partie = False
                            joueur1[win] = joueur1[win] + 1
                            continue

                        if emoji3_croix and emoji6_croix and emoji9_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji7_croix and emoji8_croix and emoji9_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji1_croix and emoji4_croix and emoji7_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji4_croix and emoji5_croix and emoji6_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji2_croix and emoji5_croix and emoji8_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji1_croix and emoji5_croix and emoji9_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji3_croix and emoji5_croix and emoji7_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        # pour le vaiceur du joueur 2

                        if emoji1_cercle and emoji2_cercle and emoji3_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji3_cercle and emoji6_cercle and emoji9_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji7_cercle and emoji8_cercle and emoji9_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji1_cercle and emoji4_cercle and emoji7_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji4_cercle and emoji5_cercle and emoji6_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji2_cercle and emoji5_cercle and emoji8_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji1_cercle and emoji5_cercle and emoji9_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji3_cercle and emoji5_cercle and emoji7_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        # pour le match null
                        if croix_chiffre == 5:
                            await ctx.send("It's a draw !")
                            i = 0
                            continuer_partie = False

                        if cercle_chiffre == 5:
                            await ctx.send("It's a draw !")
                            i = 0
                            continuer_partie = False

                        if i == 2:
                            await ctx.send("It's your turn, {}.".format(joueur2))
                        else:
                            continuer_partie = False

                    if choix == '6':
                        emoji6 = croix
                        await ctx.send(f"{emoji1} {emoji2} {emoji3}\n"
                                       f"{emoji4} {emoji5} {emoji6}\n"
                                       f"{emoji7} {emoji8} {emoji9}")

                        i = i + 1
                        croix_chiffre = croix_chiffre + 1
                        emoji6_croix = True
                        # pour la win du joueur 1
                        if emoji1_croix and emoji2_croix and emoji3_croix == True:
                            await ctx.send("felicitation a {} qui a gagner la game".format(joueur1))
                            continuer_partie = False
                            joueur1[win] = joueur1[win] + 1
                            continue

                        if emoji3_croix and emoji6_croix and emoji9_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji7_croix and emoji8_croix and emoji9_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji1_croix and emoji4_croix and emoji7_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji4_croix and emoji5_croix and emoji6_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji2_croix and emoji5_croix and emoji8_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji1_croix and emoji5_croix and emoji9_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji3_croix and emoji5_croix and emoji7_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        # pour le vaiceur du joueur 2

                        if emoji1_cercle and emoji2_cercle and emoji3_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji3_cercle and emoji6_cercle and emoji9_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji7_cercle and emoji8_cercle and emoji9_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji1_cercle and emoji4_cercle and emoji7_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji4_cercle and emoji5_cercle and emoji6_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji2_cercle and emoji5_cercle and emoji8_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji1_cercle and emoji5_cercle and emoji9_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji3_cercle and emoji5_cercle and emoji7_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        # pour le match null
                        if croix_chiffre == 5:
                            await ctx.send("It's a draw !")
                            i = 0
                            continuer_partie = False

                        if cercle_chiffre == 5:
                            await ctx.send("It's a draw !")
                            i = 0
                            continuer_partie = False

                        if i == 2:
                            await ctx.send("It's your turn, {}.".format(joueur2))
                        else:
                            continuer_partie = False

                    if choix == '7':
                        emoji7 = croix
                        await ctx.send(f"{emoji1} {emoji2} {emoji3}\n"
                                       f"{emoji4} {emoji5} {emoji6}\n"
                                       f"{emoji7} {emoji8} {emoji9}")

                        i = i + 1
                        croix_chiffre = croix_chiffre + 1
                        emoji7_croix = True
                        # pour la win du joueur 1
                        if emoji1_croix and emoji2_croix and emoji3_croix == True:
                            await ctx.send("felicitation a {} qui a gagner la game".format(joueur1))
                            continuer_partie = False
                            joueur1[win] = joueur1[win] + 1
                            continue

                        if emoji3_croix and emoji6_croix and emoji9_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji7_croix and emoji8_croix and emoji9_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji1_croix and emoji4_croix and emoji7_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji4_croix and emoji5_croix and emoji6_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji2_croix and emoji5_croix and emoji8_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji1_croix and emoji5_croix and emoji9_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji3_croix and emoji5_croix and emoji7_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        # pour le vaiceur du joueur 2

                        if emoji1_cercle and emoji2_cercle and emoji3_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji3_cercle and emoji6_cercle and emoji9_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji7_cercle and emoji8_cercle and emoji9_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji1_cercle and emoji4_cercle and emoji7_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji4_cercle and emoji5_cercle and emoji6_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji2_cercle and emoji5_cercle and emoji8_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji1_cercle and emoji5_cercle and emoji9_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji3_cercle and emoji5_cercle and emoji7_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        # pour le match null
                        if croix_chiffre == 5:
                            await ctx.send("It's a draw !")
                            i = 0
                            continuer_partie = False

                        if cercle_chiffre == 5:
                            await ctx.send("It's a draw !")
                            i = 0
                            continuer_partie = False

                        if i == 2:
                            await ctx.send("It's your turn, {}.".format(joueur2))
                        else:
                            continuer_partie = False

                    if choix == '8':
                        emoji8 = croix
                        await ctx.send(f"{emoji1} {emoji2} {emoji3}\n"
                                       f"{emoji4} {emoji5} {emoji6}\n"
                                       f"{emoji7} {emoji8} {emoji9}")

                        i = i + 1
                        croix_chiffre = croix_chiffre + 1
                        emoji8_croix = True
                        # pour la win du joueur 1
                        if emoji1_croix and emoji2_croix and emoji3_croix == True:
                            await ctx.send("felicitation a {} qui a gagner la game".format(joueur1))
                            continuer_partie = False
                            joueur1[win] = joueur1[win] + 1
                            continue

                        if emoji3_croix and emoji6_croix and emoji9_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji7_croix and emoji8_croix and emoji9_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji1_croix and emoji4_croix and emoji7_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji4_croix and emoji5_croix and emoji6_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji2_croix and emoji5_croix and emoji8_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji1_croix and emoji5_croix and emoji9_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji3_croix and emoji5_croix and emoji7_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        # pour le vaiceur du joueur 2

                        if emoji1_cercle and emoji2_cercle and emoji3_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji3_cercle and emoji6_cercle and emoji9_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji7_cercle and emoji8_cercle and emoji9_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji1_cercle and emoji4_cercle and emoji7_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji4_cercle and emoji5_cercle and emoji6_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji2_cercle and emoji5_cercle and emoji8_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji1_cercle and emoji5_cercle and emoji9_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji3_cercle and emoji5_cercle and emoji7_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        # pour le match null
                        if croix_chiffre == 5:
                            await ctx.send("It's a draw !")
                            i = 0
                            continuer_partie = False

                        if cercle_chiffre == 5:
                            await ctx.send("It's a draw !")
                            i = 0
                            continuer_partie = False

                        if i == 2:
                            await ctx.send("It's your turn, {}.".format(joueur2))
                        else:
                            continuer_partie = False

                    if choix == '9':
                        emoji9 = croix
                        await ctx.send(f"{emoji1} {emoji2} {emoji3}\n"
                                       f"{emoji4} {emoji5} {emoji6}\n"
                                       f"{emoji7} {emoji8} {emoji9}")

                        i = i + 1

                        croix_chiffre = croix_chiffre + 1
                        emoji9_croix = True
                        # pour la win du joueur 1
                        if emoji1_croix and emoji2_croix and emoji3_croix == True:
                            await ctx.send("felicitation a {} qui a gagner la game".format(joueur1))
                            continuer_partie = False
                            joueur1[win] = joueur1[win] + 1
                            continue

                        if emoji3_croix and emoji6_croix and emoji9_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji7_croix and emoji8_croix and emoji9_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji1_croix and emoji4_croix and emoji7_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji4_croix and emoji5_croix and emoji6_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji2_croix and emoji5_croix and emoji8_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji1_croix and emoji5_croix and emoji9_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji3_croix and emoji5_croix and emoji7_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        # pour le vaiceur du joueur 2

                        if emoji1_cercle and emoji2_cercle and emoji3_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji3_cercle and emoji6_cercle and emoji9_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji7_cercle and emoji8_cercle and emoji9_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji1_cercle and emoji4_cercle and emoji7_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji4_cercle and emoji5_cercle and emoji6_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji2_cercle and emoji5_cercle and emoji8_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji1_cercle and emoji5_cercle and emoji9_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji3_cercle and emoji5_cercle and emoji7_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        # pour le match null
                        if croix_chiffre == 5:
                            await ctx.send("It's a draw !")
                            i = 0
                            continuer_partie = False

                        if cercle_chiffre == 5:
                            await ctx.send("It's a draw !")
                            i = 0
                            continuer_partie = False

                        if i == 2:
                            await ctx.send("It's your turn, {}.".format(joueur2))
                        else:
                            continuer_partie = False





                    else:
                        continue

                while i == 2:

                    def check(m):
                        return m.author.id == joueur.id

                    reponse = await self.bot.wait_for('message', check=check)

                    choix2 = str(reponse.content)

                    # pour la repetition de cercle
                    if choix2 == '1' and emoji1 == cercle:
                        await ctx.send("You cannot put a circle there. You gotta pick again {}".format(joueur2))
                        continue

                    if choix2 == '2' and emoji2 == cercle:
                        await ctx.send("You cannot put a circle there. You gotta pick again {}".format(joueur2))
                        continue

                    if choix2 == '3' and emoji3 == cercle:
                        await ctx.send("You cannot put a circle there. You gotta pick again {}".format(joueur2))
                        continue

                    if choix2 == '4' and emoji4 == cercle:
                        await ctx.send("You cannot put a circle there. You gotta pick again {}".format(joueur2))
                        continue

                    if choix2 == '5' and emoji5 == cercle:
                        await ctx.send("You cannot put a circle there. You gotta pick again {}".format(joueur2))
                        continue

                    if choix2 == '6' and emoji6 == cercle:
                        await ctx.send("You cannot put a circle there. You gotta pick again {}".format(joueur2))
                        continue

                    if choix2 == '7' and emoji7 == cercle:
                        await ctx.send("You cannot put a circle there. You gotta pick again {}".format(joueur2))
                        continue

                    if choix2 == '8' and emoji8 == cercle:
                        await ctx.send("You cannot put a circle there. You gotta pick again {}".format(joueur2))
                        continue

                    if choix2 == '9' and emoji9 == cercle:
                        await ctx.send("You cannot put a circle there. You gotta pick again {}".format(joueur2))
                        continue

                        # pour la repetion de croix

                    if choix2 == '1' and emoji1 == croix:
                        await ctx.send("You cannot put a circle there. You gotta pick again {}".format(joueur2))
                        continue

                    if choix2 == '2' and emoji2 == croix:
                        await ctx.send("You cannot put a circle there. You gotta pick again {}".format(joueur2))
                        continue

                    if choix2 == '3' and emoji3 == croix:
                        await ctx.send("You cannot put a circle there. You gotta pick again {}".format(joueur2))
                        continue

                    if choix2 == '4' and emoji4 == croix:
                        await ctx.send("You cannot put a circle there. You gotta pick again {}".format(joueur2))
                        continue

                    if choix2 == '5' and emoji5 == croix:
                        await ctx.send("You cannot put a circle there. You gotta pick again {}".format(joueur2))
                        continue

                    if choix2 == '6' and emoji6 == croix:
                        await ctx.send("You cannot put a circle there. You gotta pick again {}".format(joueur2))
                        continue

                    if choix2 == '7' and emoji7 == croix:
                        await ctx.send("You cannot put a circle there. You gotta pick again {}".format(joueur2))
                        continue

                    if choix2 == '8' and emoji8 == croix:
                        await ctx.send("You cannot put a circle there. You gotta pick again {}".format(joueur2))
                        continue

                    if choix2 == '9' and emoji9 == croix:
                        await ctx.send("You cannot put a circle there. You gotta pick again {}".format(joueur2))
                        continue

                    # if choix2 > 9:
                    # await ctx.send("Pick a number below 9.")

                    # elif choix2 < 0:
                    # await ctx.send("You cannot pick a number under 0.")

                    if choix2 == '0':
                        await ctx.send("The game ended.")
                        i = 0
                        continuer_partie = False

                        # pour le match null
                    if croix_chiffre == 5:
                        await ctx.send("It's a draw !")
                        i = 0
                        continuer_partie = False

                    if cercle_chiffre == 5:
                        await ctx.send("It's a draw !")
                        i = 0
                        continuer_partie = False

                    if choix2 == '1':
                        emoji1 = cercle
                        await ctx.send(f"{emoji1} {emoji2} {emoji3}\n"
                                       f"{emoji4} {emoji5} {emoji6}\n"
                                       f"{emoji7} {emoji8} {emoji9}")

                        i = i - 1
                        cercle_chiffre = cercle_chiffre + 1
                        emoji1_cercle = True
                        # pour la win du joueur 1
                        if emoji1_croix and emoji2_croix and emoji3_croix == True:
                            await ctx.send("felicitation a {} qui a gagner la game".format(joueur1))
                            continuer_partie = False
                            joueur1[win] = joueur1[win] + 1
                            continue

                        if emoji3_croix and emoji6_croix and emoji9_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji7_croix and emoji8_croix and emoji9_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji1_croix and emoji4_croix and emoji7_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji4_croix and emoji5_croix and emoji6_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji2_croix and emoji5_croix and emoji8_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji1_croix and emoji5_croix and emoji9_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji3_croix and emoji5_croix and emoji7_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        # pour le vaiceur du joueur 2

                        if emoji1_cercle and emoji2_cercle and emoji3_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji3_cercle and emoji6_cercle and emoji9_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji7_cercle and emoji8_cercle and emoji9_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji1_cercle and emoji4_cercle and emoji7_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji4_cercle and emoji5_cercle and emoji6_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji2_cercle and emoji5_cercle and emoji8_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji1_cercle and emoji5_cercle and emoji9_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji3_cercle and emoji5_cercle and emoji7_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        # pour le match null
                        if croix_chiffre == 5:
                            await ctx.send("It's a draw !")
                            i = 0
                            continuer_partie = False

                        if cercle_chiffre == 5:
                            await ctx.send("It's a draw !")
                            i = 0
                            continuer_partie = False

                        # pour le match null
                        if croix_chiffre == 5:
                            await ctx.send("It's a draw !")
                            i = 0
                            continuer_partie = False

                        if cercle_chiffre == 5:
                            await ctx.send("It's a draw !")
                            i = 0
                            continuer_partie = False

                        if i == 1:
                            await ctx.send("It's your turn, {}.".format(joueur1))
                        else:
                            continuer_partie = False

                    if choix2 == '2':
                        emoji2 = cercle
                        await ctx.send(f"{emoji1} {emoji2} {emoji3}\n"
                                       f"{emoji4} {emoji5} {emoji6}\n"
                                       f"{emoji7} {emoji8} {emoji9}")

                        i = i - 1

                        cercle_chiffre = cercle_chiffre + 1
                        emoji2_cercle = True
                        await ctx.send("It's your turn, {}.".format(joueur1))

                    if choix2 == '3':
                        emoji3 = cercle
                        await ctx.send(f"{emoji1} {emoji2} {emoji3}\n"
                                       f"{emoji4} {emoji5} {emoji6}\n"
                                       f"{emoji7} {emoji8} {emoji9}")

                        i = i - 1
                        cercle_chiffre = cercle_chiffre + 1
                        emoji3_cercle = True
                        # pour la win du joueur 1
                        if emoji1_croix and emoji2_croix and emoji3_croix == True:
                            await ctx.send("felicitation a {} qui a gagner la game".format(joueur1))
                            continuer_partie = False
                            joueur1[win] = joueur1[win] + 1
                            continue

                        if emoji3_croix and emoji6_croix and emoji9_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji7_croix and emoji8_croix and emoji9_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji1_croix and emoji4_croix and emoji7_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji4_croix and emoji5_croix and emoji6_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji2_croix and emoji5_croix and emoji8_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji1_croix and emoji5_croix and emoji9_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji3_croix and emoji5_croix and emoji7_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        # pour le vaiceur du joueur 2

                        if emoji1_cercle and emoji2_cercle and emoji3_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji3_cercle and emoji6_cercle and emoji9_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji7_cercle and emoji8_cercle and emoji9_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji1_cercle and emoji4_cercle and emoji7_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji4_cercle and emoji5_cercle and emoji6_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji2_cercle and emoji5_cercle and emoji8_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji1_cercle and emoji5_cercle and emoji9_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji3_cercle and emoji5_cercle and emoji7_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        # pour le match null
                        if croix_chiffre == 5:
                            await ctx.send("It's a draw !")
                            i = 0
                            continuer_partie = False

                        if cercle_chiffre == 5:
                            await ctx.send("It's a draw !")
                            i = 0
                            continuer_partie = False

                        if i == 1:
                            await ctx.send("It's your turn, {}.".format(joueur1))
                        else:
                            continuer_partie = False

                    if choix2 == '4':
                        emoji4 = cercle
                        await ctx.send(f"{emoji1} {emoji2} {emoji3}\n"
                                       f"{emoji4} {emoji5} {emoji6}\n"
                                       f"{emoji7} {emoji8} {emoji9}")

                        i = i - 1
                        cercle_chiffre = cercle_chiffre + 1
                        emoji4_cercle = True
                        # pour la win du joueur 1
                        if emoji1_croix and emoji2_croix and emoji3_croix == True:
                            await ctx.send("felicitation a {} qui a gagner la game".format(joueur1))
                            continuer_partie = False
                            joueur1[win] = joueur1[win] + 1
                            continue

                        if emoji3_croix and emoji6_croix and emoji9_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji7_croix and emoji8_croix and emoji9_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji1_croix and emoji4_croix and emoji7_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji4_croix and emoji5_croix and emoji6_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji2_croix and emoji5_croix and emoji8_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji1_croix and emoji5_croix and emoji9_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji3_croix and emoji5_croix and emoji7_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        # pour le vaiceur du joueur 2

                        if emoji1_cercle and emoji2_cercle and emoji3_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji3_cercle and emoji6_cercle and emoji9_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji7_cercle and emoji8_cercle and emoji9_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji1_cercle and emoji4_cercle and emoji7_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji4_cercle and emoji5_cercle and emoji6_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji2_cercle and emoji5_cercle and emoji8_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji1_cercle and emoji5_cercle and emoji9_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji3_cercle and emoji5_cercle and emoji7_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        # pour le match null
                        if croix_chiffre == 5:
                            await ctx.send("It's a draw !")
                            i = 0
                            continuer_partie = False

                        if cercle_chiffre == 5:
                            await ctx.send("It's a draw !")
                            i = 0
                            continuer_partie = False

                        if i == 1:
                            await ctx.send("It's your turn, {}.".format(joueur1))
                        else:
                            continuer_partie = False

                    if choix2 == '5':
                        emoji5 = cercle
                        await ctx.send(f"{emoji1} {emoji2} {emoji3}\n"
                                       f"{emoji4} {emoji5} {emoji6}\n"
                                       f"{emoji7} {emoji8} {emoji9}")

                        i = i - 1

                        cercle_chiffre = cercle_chiffre + 1
                        emoji5_cercle = True
                        # pour la win du joueur 1
                        if emoji1_croix and emoji2_croix and emoji3_croix == True:
                            await ctx.send("felicitation a {} qui a gagner la game".format(joueur1))
                            continuer_partie = False
                            joueur1[win] = joueur1[win] + 1
                            continue

                        if emoji3_croix and emoji6_croix and emoji9_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji7_croix and emoji8_croix and emoji9_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji1_croix and emoji4_croix and emoji7_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji4_croix and emoji5_croix and emoji6_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji2_croix and emoji5_croix and emoji8_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji1_croix and emoji5_croix and emoji9_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji3_croix and emoji5_croix and emoji7_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        # pour le vaiceur du joueur 2

                        if emoji1_cercle and emoji2_cercle and emoji3_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji3_cercle and emoji6_cercle and emoji9_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji7_cercle and emoji8_cercle and emoji9_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji1_cercle and emoji4_cercle and emoji7_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji4_cercle and emoji5_cercle and emoji6_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji2_cercle and emoji5_cercle and emoji8_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji1_cercle and emoji5_cercle and emoji9_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji3_cercle and emoji5_cercle and emoji7_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        # pour le match null
                        if croix_chiffre == 5:
                            await ctx.send("It's a draw !")
                            i = 0
                            continuer_partie = False

                        if cercle_chiffre == 5:
                            await ctx.send("It's a draw !")
                            i = 0
                            continuer_partie = False

                        if i == 1:
                            await ctx.send("It's your turn, {}.".format(joueur1))
                        else:
                            continuer_partie = False

                    if choix2 == '6':
                        emoji6 = cercle
                        await ctx.send(f"{emoji1} {emoji2} {emoji3}\n"
                                       f"{emoji4} {emoji5} {emoji6}\n"
                                       f"{emoji7} {emoji8} {emoji9}")

                        i = i - 1

                        cercle_chiffre = cercle_chiffre + 1
                        emoji6_cercle = True
                        # pour la win du joueur 1
                        if emoji1_croix and emoji2_croix and emoji3_croix == True:
                            await ctx.send("felicitation a {} qui a gagner la game".format(joueur1))
                            continuer_partie = False
                            joueur1[win] = joueur1[win] + 1
                            continue

                        if emoji3_croix and emoji6_croix and emoji9_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji7_croix and emoji8_croix and emoji9_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji1_croix and emoji4_croix and emoji7_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji4_croix and emoji5_croix and emoji6_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji2_croix and emoji5_croix and emoji8_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji1_croix and emoji5_croix and emoji9_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji3_croix and emoji5_croix and emoji7_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        # pour le vaiceur du joueur 2

                        if emoji1_cercle and emoji2_cercle and emoji3_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji3_cercle and emoji6_cercle and emoji9_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji7_cercle and emoji8_cercle and emoji9_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji1_cercle and emoji4_cercle and emoji7_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji4_cercle and emoji5_cercle and emoji6_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji2_cercle and emoji5_cercle and emoji8_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji1_cercle and emoji5_cercle and emoji9_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji3_cercle and emoji5_cercle and emoji7_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        # pour le match null
                        if croix_chiffre == 5:
                            await ctx.send("It's a draw !")
                            i = 0
                            continuer_partie = False

                        if cercle_chiffre == 5:
                            await ctx.send("It's a draw !")
                            i = 0
                            continuer_partie = False
                        if i == 1:
                            await ctx.send("It's your turn, {}.".format(joueur1))
                        else:
                            continuer_partie = False

                    if choix2 == '7':
                        emoji7 = cercle
                        await ctx.send(f"{emoji1} {emoji2} {emoji3}\n"
                                       f"{emoji4} {emoji5} {emoji6}\n"
                                       f"{emoji7} {emoji8} {emoji9}")

                        i = i - 1

                        cercle_chiffre = cercle_chiffre + 1
                        emoji7_cercle = True
                        # pour la win du joueur 1
                        if emoji1_croix and emoji2_croix and emoji3_croix == True:
                            await ctx.send("felicitation a {} qui a gagner la game".format(joueur1))
                            continuer_partie = False
                            joueur1[win] = joueur1[win] + 1
                            continue

                        if emoji3_croix and emoji6_croix and emoji9_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji7_croix and emoji8_croix and emoji9_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji1_croix and emoji4_croix and emoji7_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji4_croix and emoji5_croix and emoji6_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji2_croix and emoji5_croix and emoji8_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji1_croix and emoji5_croix and emoji9_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji3_croix and emoji5_croix and emoji7_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        # pour le vaiceur du joueur 2

                        if emoji1_cercle and emoji2_cercle and emoji3_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji3_cercle and emoji6_cercle and emoji9_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji7_cercle and emoji8_cercle and emoji9_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji1_cercle and emoji4_cercle and emoji7_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji4_cercle and emoji5_cercle and emoji6_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji2_cercle and emoji5_cercle and emoji8_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji1_cercle and emoji5_cercle and emoji9_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji3_cercle and emoji5_cercle and emoji7_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        # pour le match null
                        if croix_chiffre == 5:
                            await ctx.send("It's a draw !")
                            i = 0
                            continuer_partie = False

                        if cercle_chiffre == 5:
                            await ctx.send("It's a draw !")
                            i = 0
                            continuer_partie = False

                        if i == 1:
                            await ctx.send("It's your turn, {}.".format(joueur1))
                        else:
                            continuer_partie = False

                    if choix2 == '8':
                        emoji8 = cercle
                        await ctx.send(f"{emoji1} {emoji2} {emoji3}\n"
                                       f"{emoji4} {emoji5} {emoji6}\n"
                                       f"{emoji7} {emoji8} {emoji9}")

                        i = i - 1

                        cercle_chiffre = cercle_chiffre + 1
                        emoji8_cercle = True
                        # pour la win du joueur 1
                        if emoji1_croix and emoji2_croix and emoji3_croix == True:
                            await ctx.send("felicitation a {} qui a gagner la game".format(joueur1))
                            continuer_partie = False
                            joueur1[win] = joueur1[win] + 1
                            continue

                        if emoji3_croix and emoji6_croix and emoji9_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji7_croix and emoji8_croix and emoji9_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji1_croix and emoji4_croix and emoji7_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji4_croix and emoji5_croix and emoji6_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji2_croix and emoji5_croix and emoji8_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji1_croix and emoji5_croix and emoji9_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji3_croix and emoji5_croix and emoji7_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        # pour le vaiceur du joueur 2

                        if emoji1_cercle and emoji2_cercle and emoji3_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji3_cercle and emoji6_cercle and emoji9_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji7_cercle and emoji8_cercle and emoji9_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji1_cercle and emoji4_cercle and emoji7_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji4_cercle and emoji5_cercle and emoji6_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji2_cercle and emoji5_cercle and emoji8_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji1_cercle and emoji5_cercle and emoji9_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji3_cercle and emoji5_cercle and emoji7_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        # pour le match null
                        if croix_chiffre == 5:
                            await ctx.send("It's a draw !")
                            i = 0
                            continuer_partie = False

                        if cercle_chiffre == 5:
                            await ctx.send("It's a draw !")
                            i = 0
                            continuer_partie = False
                        if i == 1:
                            await ctx.send("It's your turn, {}.".format(joueur1))
                        else:
                            continuer_partie = False

                    if choix2 == '9':
                        emoji9 = cercle
                        await ctx.send(f"{emoji1} {emoji2} {emoji3}\n"
                                       f"{emoji4} {emoji5} {emoji6}\n"
                                       f"{emoji7} {emoji8} {emoji9}")

                        i = i - 1

                        cercle_chiffre = cercle_chiffre + 1
                        emoji9_cercle = True
                        # pour la win du joueur 1
                        if emoji1_croix and emoji2_croix and emoji3_croix == True:
                            await ctx.send("felicitation a {} qui a gagner la game".format(joueur1))
                            continuer_partie = False
                            joueur1[win] = joueur1[win] + 1
                            continue

                        if emoji3_croix and emoji6_croix and emoji9_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji7_croix and emoji8_croix and emoji9_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji1_croix and emoji4_croix and emoji7_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji4_croix and emoji5_croix and emoji6_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji2_croix and emoji5_croix and emoji8_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji1_croix and emoji5_croix and emoji9_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji3_croix and emoji5_croix and emoji7_croix == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur1))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        # pour le vaiceur du joueur 2

                        if emoji1_cercle and emoji2_cercle and emoji3_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji3_cercle and emoji6_cercle and emoji9_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji7_cercle and emoji8_cercle and emoji9_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji1_cercle and emoji4_cercle and emoji7_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji4_cercle and emoji5_cercle and emoji6_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji2_cercle and emoji5_cercle and emoji8_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji1_cercle and emoji5_cercle and emoji9_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        if emoji3_cercle and emoji5_cercle and emoji7_cercle == True:
                            await ctx.send("Congratulations to {} for winning the game.".format(joueur2))
                            continuer_partie = False
                            joueur2[win] = joueur2[win] + 1
                            continue

                        # pour le match null
                        if croix_chiffre == 5:
                            await ctx.send("It's a draw !")
                            i = 0
                            continuer_partie = False

                        if cercle_chiffre == 5:
                            await ctx.send("It's a draw !")
                            i = 0
                            continuer_partie = False

                        if i == 1:
                            await ctx.send("It's your turn, {}.".format(joueur1))
                        else:
                            continuer_partie = False


                    else:
                        continue

    @tictac.error
    async def on_command_error(error, ctx):
        # detection d'erreur
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("You must mention at least one friend to play with.")