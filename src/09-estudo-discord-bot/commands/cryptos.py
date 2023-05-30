from discord.ext import commands
import requests

class Cryptos(commands.Cog):
    """ Works with cryptocurrency"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="Verifica o preço de um par na binance. Argumentos: moeda, base") # Se um nome customizado não for passado, o comando vai ser executado através do nome da função.
    async def binance(self, ctx, coin, base):
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

def setup(bot):
    return bot.add_cog(Cryptos(bot))