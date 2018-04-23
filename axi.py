import discord
from discord.ext import commands
initial_cogs = {}


class NabBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=["/"], description='Mission: Destroy all humans.', pm_help=True,
                         formatter=NabHelpFormat())
        self.remove_command("help")
        self.command_list = []
        self.members = {}

    async def on_ready(self):
        """Called when the bot is ready."""
        print('Logged in as')
        print(self.user)
        print(self.user.id)
        print('------')
        
        
 if __name__ == "__main__":

    print("Loading cogs...")
    for cog in initial_cogs:
        try:
            nabbot.load_extension(cog)
            print("Cog {} loaded successfully.".format(cog))
        except Exception as e:
            print('Cog {} failed to load:'.format(cog))
            traceback.print_exc(limit=-1)

    try:
        print("Attempting login...")
        axi.run('NDI2MDEzMTk4MzQ1NTY4MjY2.Db-p-w.xgsAn3RfRYlVz_9RBWrq4uglzvs')
    except discord.errors.LoginFailure:
        print("Invalid token. Edit token.txt to fix it.")
        input("\nPress any key to continue...")
        quit()
