#!/usr/bin/env python
from twisted.words.protocols import irc
from twisted.internet import reactor, protocol
from twisted.python import log

import commandhandle

import time, sys

class MessageLogger:
   def __init__(self, file):
      self.file = file

   def log(self, message):
      timestamp = time.strftime("[%H:%M:%S]", time.localtime(time.time()))
      self.file.write("%s %s\n"  % (timestamp, message))
      self.file.flush()

   def close():
      self.file.close()

class BoneBot(irc.IRCClient):

   nickname = "bone"
   def connectionMade(self):
      irc.IRCClient.connectionMade(self)
      self.logger = MessageLogger(open(self.factory.filename, "a"))
      self.logger.log("[connected]")
      self.cmdhandle = commandhandle.CommandHandler(self)

   def connectionLost(self, reason):
      irc.IRCClient.connectionLost(self, reason)
      self.logger.log("[disconnected]")
      self.logger.close()

   #Callbacks

   def signedOn(self):
      self.join(self.factory.channel)

   def joined(self, channel):
      self.logger.log("[I joined %s]" % channel) 

   def privmsg(self, user, channel, msg):
      user = user.split("!")[0]
      self.logger.log("<%s> %s" % (user, msg))
      if msg.startswith(">"):
         reload(commandhandle)
         self.cmdhandle = commandhandle.CommandHandler(self)
         self.cmdhandle.handlecmd(channel, msg[1:])

   def action(self, user, channel, msg):
      user = user.split('!', 1)[0]
      self.logger.log("* %s %s", (user, msg))


class BoneBotFactory(protocol.ClientFactory):
   
   protocol = BoneBot

   def __init__(self, channel, filename):
      self.channel = channel
      self.filename = filename

   def clientConnectionLost(self, connector, reason):
      connector.connect()
   
   def clientConnectionFailed(self, connector, reason):
      print "connection failed:", reason
      reactor.stop()


if __name__ == "__main__":
   
   log.startLogging(sys.stdout)

   f = BoneBotFactory(sys.argv[1], sys.argv[2])
   
   reactor.connectTCP("irc.eighthbit.net", 6667, f)
   
   reactor.run()
