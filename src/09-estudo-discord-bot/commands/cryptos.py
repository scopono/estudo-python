from discord.ext import commands
import discord
import requests
from discord import app_commands
MY_GUILD = discord.Object(id=1111997040906469426)

class Cryptos(commands.Cog):
    """ Works with cryptocurrency"""
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(description="Verifica o preço de um par na binance. Argumentos: moeda, base") # Se um nome customizado não for passado, o comando vai ser executado através do nome da função.
    async def binance(self, interaction: discord.Interaction, coin:str, base:str):
        try: # vai tentar executar um trecho de código
            response = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={coin.upper()}{base.upper()}")

            data = response.json() # json ⇒ formato de arquivo para representar e armazenar dados, parecido com o dicionário
            price = data.get("price") # "0.008372200"

            if price:
                await interaction.response.send_message(f"O valor do par {coin}/{base} é {price}")
            else:
                await interaction.response.send_message(f"O par {coin}/{base} é inválido.")
        except Exception as error: # vai ser executado caso o python não consiga executar o try
            await interaction.response.send_message("Erro no sistema!")
            print(error)

def setup(bot):
    return bot.add_cog(Cryptos(bot), guilds=[MY_GUILD])