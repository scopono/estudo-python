from discord.ext import commands

class Smarts(commands.Cog):
    """ A lot of Smart Commands """
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="calcular", help="Calcula o valor de uma expressão. Argumento: Expressão")
    async def calculate_expression(self, ctx, *expression): # *expression para ele aceitar pegar os diversos argumentos e colocar em uma tupla
        expression = "".join(expression)
        response = eval(expression)

        await ctx.send("A resposta é: " + str(response))

def setup(bot):
    return bot.add_cog(Smarts(bot))