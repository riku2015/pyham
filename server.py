#!/usr/bin/python

import sys
from log import log
from config import Config
from server_protocols import ServerProtocolFrn

# Server
# One server can use one or more different protocols at the same time.
# Same protocol can be used only once in one server.

class Server:
	def __init__(self, filename_config):
		self.filename_config = filename_config

		# Defaults if not given in config file:
		#

		# Read configuration:
		config = Config()
		config.load(filename_config)

		# Initialize protocol(s):

		# if config.parameters[frn]
		self.frn = ServerProtocolFrn("Titanix FRN server", "frn.titanix.net", 10024)
		# self.frn = ServerProtocolFrn(config.parameters[frn_port])
		self.frn.bind()
		# Frn protocol is now accepting connections

		# if config.parameters[eqso]
		# self.eqso = ProtocolEqso(self.server_port)
		# Eqso protocol is now accepting connections

		# if config.parameters[echolink]
		# self.echolink = ProtocolEcholink(self.server_port)
		# Echolink protocol is now accepting connections

		# if config.parameters[pyhamp]
		# self.pyhamp = ProtocolPyhamp(self.server_port)
		# Pyhamp protocol is now accepting connections

	def Run(self):
		log("Server started.")

	def Stop(self):
		log("Server stopped.")
