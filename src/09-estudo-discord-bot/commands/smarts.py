from discord.ext import commands
from discord import app_commands
import discord
MY_GUILD = discord.Object(id=1111997040906469426)

class Smarts(commands.Cog):
    """ A lot of Smart Commands """
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="calcular", description="Calcula o valor de uma expressão. Argumento: Expressão")
    async def calculate_expression(self, interaction: discord.Interaction, expression:str): # *expression para ele aceitar pegar os diversos argumentos e colocar em uma tupla
        expression = "".join(expression)
        response = eval(expression)

        await interaction.response.send_message("A resposta é: " + str(response))

def setup(bot):
    return bot.add_cog(Smarts(bot), guilds=[MY_GUILD])