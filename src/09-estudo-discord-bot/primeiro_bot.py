import discord
from discord.ext import commands, tasks
from discord import utils
from discord.ext.commands.errors import MissingRequiredArgument, CommandNotFound

import requests

from decouple import config

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(intents=intents, command_prefix="!")

@bot.event
async def on_ready(): # async → Fala para a função executar de maneira assíncrona, podendo ser executado enquanto outras funções são processadas
    print(f"Estou pronto! Estou conectado como {bot.user}")
    # current_time.start()

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if "palavrão" in message.content:
        await message.channel.send(
            f"Por favor, {message.author.name}, não ofenda os demais usuários!"
            )
        await message.delete() # Para continuar a função assíncrona, ele vai esperar deletar a mensagem para depois prosseguir

    await bot.process_commands(message)

@bot.event
async def on_reaction_add(reaction, user):
    if reaction.emoji == "👍":
        role = user.guild.get_role(1112741771294822481)
        await user.add_roles(role)
    elif reaction.emoji == "💩":
        role = user.guild.get_role(1112741725908238439)
        await user.add_roles(role)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error,MissingRequiredArgument):
        await ctx.send("Favor enviar todos os argumentos. Digite !help para ver os parâmetros de todos os comandos.")
    elif isinstance(error,CommandNotFound):
        await ctx.send("O comando não existe. Digite !help para ver os parâmetros de todos os comandos.")
    else:
        raise error
    
@bot.command(name="oi")
async def send_hello(ctx): # ctx - Contexto da função, ou seja, o usuário, o canal de texto, o conteúdo da mensagem etc
    name = ctx.author.name
    response = "Olá, " + name
    await ctx.send(response)

@bot.command(name="foto", help="Envia uma foto aleatório do picsum. Argumentos: Altura e Largura")
async def get_random_image(ctx, altura, largura):
    url_image = f"https://picsum.photos/{altura}/{largura}"

    embed_image = discord.Embed(
        title = "Resultado da busca de imagem",
        description = "PS: A busca é totalmente aleatória",
        color = 0x0000FF
    )

    embed_image.set_author(name=bot.user.name, icon_url=bot.user.avatar)
    embed_image.set_footer(text="Feito por " + bot.user.name, icon_url=bot.user.avatar)

    embed_image.add_field(name="API", value="Usamos a API do https://picsum.photos")
    embed_image.add_field(name="Parâmetros", value="{altura}/{largura}")

    embed_image.add_field(name="Exemplo", value=url_image, inline=False)
    embed_image.set_image(url=url_image)

    await ctx.send(embed=embed_image)

@bot.command(name="calcular", help="Calcula o valor de uma expressão. Argumento: Expressão")
async def calculate_expression(ctx, *expression): # *expression para ele aceitar pegar os diversos argumentos e colocar em uma tupla
    # "*separador*".join(*lista*) - Pega todos os elementos de uma lista e colocar eles em uma única string, podendo conter um separador ou não.
    expression = "".join(expression)
    # eval() → Pega um trecho de código ou expressão matemática e manda o valor final daquilo passado pra ela.
    # Usar o eval é perigoso, porque a pessoa pode passar uma mensagem para encerrar a aplicação ou pegar o banco de dados, por exemplo
    response = eval(expression)
    # response → Necessário transformar em string porque ele vai pegar o valor final e dar um real, o que impossibilita a concatenação de strings.
    await ctx.send("A resposta é: " + str(response))

@bot.command(help="Verifica o preço de um par na binance. Argumentos: moeda, base") # Se um nome customizado não for passado, o comando vai ser executado através do nome da função.
async def binance(ctx, coin, base):
    try: # vai tentar executar um trecho de código
        response = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={coin.upper()}{base.upper()}")

        data = response.json() # json ⇒ formato de arquivo para representar e armazenar dados, parecido com o dicionário
        price = data.get("price") # "0.008372200"

        if price:
            await ctx.send(f"O valor do par {coin}/{base} é {price}")
        else:
            await ctx.send(f"O par {coin}/{base} é inválido.")
    except Exception as error: # vai ser executado caso o python não consiga executar o try
        await ctx.send("Erro no sistema!")
        print(error)

@bot.command(name="segredo", help="Envia um segredo no privado. Não requer um argumento.")
async def secret(ctx):
    try:
        await ctx.author.send("nteste")
        await ctx.author.send("teste1")
        await ctx.author.send("teste2")
    except discord.errors.Forbidden:
        await ctx.send(
        "Não posso te contar o segredo, habilite receber mensagens de qualquer pessoa do servidor (Opções > Privacidade)"
        )

@tasks.loop(seconds=60)
async def current_time():
    now = utils.datetime.datetime.now()
    now = now.strftime("%d/%m/%Y às %H:%M:%S") # string format time

    channel = bot.get_channel(1111997040906469429)

    await channel.send("Data atual: " + now)

TOKEN = config("TOKEN_SECRETO")
bot.run(TOKEN)

