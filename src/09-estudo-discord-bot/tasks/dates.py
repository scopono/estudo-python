from discord import utils
from discord.ext import commands, tasks

class Dates(commands.Cog):
    """ Informs the time in a determinated period"""
    def __init__(self, bot):
        self.bot = bot

    @tasks.loop(hours=60)
    async def current_time(self):
        now = utils.datetime.datetime.now()
        now = now.strftime("%d/%m/%Y às %H:%M:%S") # string format time
        channel = self.bot.get_channel(1111997040906469429)
        await channel.send("Data atual: " + now)

def setup(bot):
    return bot.add_cog(Dates(bot))