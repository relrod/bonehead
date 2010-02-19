from Morse import Morse
class CommandHandler:
   def __init__(self, bot):
      self.bot = bot
      self.commands = {"hi" : cmd_hello, "morsetolatin" : cmd_morsetolatin}

   def addcommand(self, command, function):
      commands[command] = function

   def handlecmd(self, channel, command):
      if self.commands.has_key(command.split(" ")[0]):
         self.bot.msg(channel, self.commands[command.split(" ")[0]](command.split(" ")[1:])) #All commands have to return a string 
      else:
         return


def cmd_hello(foo):
   return "HI!"

def cmd_morsetolatin(morse):
   return Morse.morsetolatin(morse)

