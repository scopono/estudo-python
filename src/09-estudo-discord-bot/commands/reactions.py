from discord.ext import commands

class Reactions(commands.Cog):
    """ Works with reactions (emojis)"""
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener() # faz parte do commands.cog, com os eventos precisando de um listener
    async def on_reaction_add(self, reaction, user):
        if reaction.emoji == "👍":
            role = user.guild.get_role(1112741771294822481)
            await user.add_roles(role)
        elif reaction.emoji == "💩":
            role = user.guild.get_role(1112741725908238439)
            await user.add_roles(role)

def setup(bot):
    return bot.add_cog(Reactions(bot))