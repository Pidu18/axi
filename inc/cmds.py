import discord
from discord.ext import commands
import random
import async

class Cmds:
 def _init_(self):
  self.bot=bot
  
 @commands.command(pass_context=True)
 async def ping(self):
  await self.bot.say("Pong")
  
def setup(bot):
 bot.add_cog(Cmds(bot))
  
