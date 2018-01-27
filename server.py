#!/usr/bin/python

import socket
from log import log
from config import Config

# Server
# One server can use one or more different protocols at the same time.
# Same protocol can be used only once in one server.
#
# TODO: Data logger

# ServerConnection
# This class is used within the server program

class ServerConnection:
	def __init__(self):
		self.__binded = False

	def bind(self):
		#log("Binding to port " + str(self.__port) + " as '" + self.__name + "' using " + self.server_protocol + " protocol.")
		self.__binded = True

	def unbind(self):
		self.__binded = False

	def isbinded(self):
		return self.__binded

class ServerProtocol(ServerConnection):
	def __init__(self, port):
		self.__port = port

# ProtocolPyhamp

class ServerProtocolPyhamp(ServerProtocol):
	def __init__(self, port):
		#super().__init__(port)
		pass

	def connect(self):
		pass

	def send(self):
		pass

# ProtocolEqso

class ServerProtocolEqso(ServerProtocol):
	def __init__(self, port):
		#super().__init__(port)
		pass

	def connect(self):
		pass

	def send(self):
		pass

# ProtocolEcholink

class ServerProtocolEcholink(ServerProtocol):
	def __init__(self, port):
		#super().__init__(port)
		pass

	def connect(self):
		pass

	def send(self):
		pass

# ProtocolFrn
# http://freeradionetwork.eu/frnprotocol.htm
# Default port: 10024

class ServerProtocolFrn(ServerProtocol):
	#def __init__(self, address, port):
	#	self.address = address
	#	self.port = port

	def __init__(self):
		#super().__init__()
		self.address = "frn.titanix.net"
		self.port = 10024
		self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	def connect(self):
		log("Incoming connecting to server " + self.address + " at port " + str(self.port) + ".")
		#log("Connected.")

	def disconnect(self):
		self.__socket.send("\x03") #lahetetaan random kakkaa servulle.. ei vie tie millai disconectataan
		log("Disconnected.")

	def send(self, data):
		#self.__socket.send(data)
		pass

class Server:
	def __init__(self, filename_config):
		self.filename_config = filename_config
		# Defaults if not given in config file:

		# Read configuration:
		config = Config()
		config.load(filename_config)

		# Initialize protocol(s):
		# if config.parameters[frn]
		self.frn = ServerProtocolFrn()
		self.frn.bind()
		# Frn protocol is now accepting connections

		# TODO:
			#self.eqso = ProtocolEqso(self.server_port)
			# Eqso protocol is now accepting connections

			#self.echolink = ProtocolEcholink(self.server_port)
			# Echolink protocol is now accepting connections

			#self.pyhamp = ProtocolPyhamp(self.server_port)
			# Pyhamp protocol is now accepting connections

	def Run(self):
		log("Server started.")

	def Stop(self):
		log("Server stopped.")
