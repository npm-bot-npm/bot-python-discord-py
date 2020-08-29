import discord
import asyncio
import random


client = discord.Client()

@client.event
async def on_ready():
    print('BOT ONLINE - OLÁ, MUNDO!')
    print(client.user.name)
    print(client.user.id)


@client.event
async def on_message(message):
    if message.content.lower().startswith('py.help'):
        await message.channel.send("**<a:Alarme:748963775797002361> | Comandos Úteis:** \n"
        "**``py.historia`` | <a:5564_Loading_Color:748968183633018950>**")

    if message.content.lower().startswith('py.historia'):
        await message.channel.send("**<:Python:748879725954465792>| ``Historia do Python`` \n \n <:725358947019522139:748902341154963486> | ``Criador: Guido van Rossum``** \n \n"
        "**<:738072941283246132:748902324008648806> | ``Por quê, Python?`` \n O nome Python teve a sua origem no grupo humorístico britânico Monty Python, \n criador do programa Monty Python's Flying Circus, \n embora muitas pessoas façam associação com o réptil do mesmo nome \n (em português, píton ou pitão). \n SAIBA MAIS: https://pt.wikipedia.org/wiki/Python** \n \n"
        "**<:725358946461810809:748940508327444540> | ``Lançado em: 1991``** \n \n"
        "**<:741084451727212554:748899528475934811> | ``Gerenciado pela organização Python Software Foundation``** \n \n"
        "**<:738072941513670760:748940579429154817> | ``Versão Atual: 3.8.5 | E pode baixado em: www.python.org``** \n \n"
        "** ``Saiba mais:`` https://pt.wikipedia.org/wiki/Python**")



client.run('NzQ4NjkyMDc5NTU0ODU1MDYz.X0hH1Q.ZuPT0OuWJk_SFHiko9MW-HJqcTI')
