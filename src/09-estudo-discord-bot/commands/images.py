import discord
from discord.ext import commands
from discord import app_commands
MY_GUILD = discord.Object(id=1111997040906469426)

class Images(commands.Cog):
    """ Works with images"""
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="foto", description="Envia uma foto aleatório do picsum. Argumentos: Altura e Largura")
    async def get_random_image(self, interaction:discord.Interaction, altura:str, largura:str):
        url_image = f"https://picsum.photos/{altura}/{largura}"

        embed_image = discord.Embed(
            title = "Resultado da busca de imagem",
            description = "PS: A busca é totalmente aleatória",
            color = 0x0000FF
        )

        embed_image.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar)
        embed_image.set_footer(text="Feito por " + self.bot.user.name, icon_url=self.bot.user.avatar)

        embed_image.add_field(name="API", value="Usamos a API do https://picsum.photos")
        embed_image.add_field(name="Parâmetros", value="{altura}/{largura}")

        embed_image.add_field(name="Exemplo", value=url_image, inline=False)
        embed_image.set_image(url=url_image)

        await interaction.response.send_message(embed=embed_image)

def setup(bot):
    return bot.add_cog(Images(bot), guilds=[MY_GUILD])