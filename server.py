#!/usr/bin/python

from pyham import log, Config, ProtocolPyhamp, ProtocolEqso, ProtocolEcholink, ProtocolFrn

# Server
# One server can use one or more different protocols at the same time.
# Same protocol can be used only once in one server.
#
# TODO: Data logger

class Server:
	def __init__(self, filename_config):
		# Defaults if not given in config file:
		self.server_name = "myhamserver"
		self.server_port = 10024
		self.server_protocol = "FRN"	# TODO: support multiple protocols simultaneously
		self.rooms = []

		# Read config:
		config = Config()
		config.load(filename_config)

		# Initialize protocol(s):
		self.frn = ProtocolFrn(self.server_port)
		#self.eqso = ProtocolEqso(self.server_port)
		#self.echolink = ProtocolEcholink(self.server_port)
		#self.pyhamp = ProtocolPyhamp(self.server_port)

		log("Binding to port " + str(self.server_port) + " as '" + self.server_name + "' using " + self.server_protocol + " protocol.")

	def Run(self):
		log("Server started.")
		pass

	def Stop(self):
		log("Server stopped.")
		pass
