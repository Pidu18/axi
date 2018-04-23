import discord
from discord.ext import commands
import random
import async

class CMDS():
    def __init__(self, bot):
        self.bot = bot
  
    @commands.command(pass_context=True)
    async def ping(self):
        await self.bot.say("Pong")

    @commands.command(pass_context=True)
    async def gay(self, ctx, user: discord.Member = None):
    	gay = random.randint(1, 100)
    	if user is None:
    		await self.bot.say("{}, you are {}'%' gay".format(ctx.message.author.mention, gay))
    	else:
    		await self.bot.say("{} is {}'%' gay".format(user.mention, gay))

  
def setup(bot):
    bot.add_cog(CMDS(bot))
