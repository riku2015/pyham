#!/usr/bin/python

import wx

import sys
from log import log
from config import Config
from server_protocols import *
from server_gui import Mainwindow

# Server
# Server with no user interface
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
		# self.frn = ServerProtocolFrn(config.parameters[frn_name, frn_address, frn_port])

		# if config.parameters[eqso]
		self.eqso = ServerProtocolEqso("Suomen eQSO", "eqso.titanix.net", 5000)
		# Eqso protocol is now accepting connections

		# if config.parameters[echolink]
		self.echolink = ServerProtocolEcholink("localhost echolink", "localhost", 5200)
		# Echolink protocol is now accepting connections

		# if config.parameters[pyhamp]
		self.pyhamp = ServerProtocolPyhamp("localhost pyhamp", "localhost", 2000)
		# Pyhamp protocol is now accepting connections

	def Run(self):
		log("Starting server.")
		self.frn.run()		# Frn protocol is now accepting connections
		self.echolink.run()	# Frn protocol is now accepting connections
		self.eqso.run()		# Frn protocol is now accepting connections
		self.pyhamp.run()	# Frn protocol is now accepting connections

	def Stop(self):
		log("Server stopped.")

# ServerWx
# Server with wxWidgets GUI

class ServerWx(Server):
	def __init__(self, filename_config):
		Server.__init__(self, filename_config)
		# Create wxwidgets application:
		#self.app = wx.App(self)	# With separate log console window
		self.app = wx.App(None)		# Without separate log console window
		self.mainwindow = Mainwindow(parent=None)

	def Run(self):
		log("Starting server (wx).")
		self.frn.run()		# Frn protocol is now accepting connections
		self.echolink.run()	# Frn protocol is now accepting connections
		self.eqso.run()		# Frn protocol is now accepting connections
		self.pyhamp.run()	# Frn protocol is now accepting connections
		# Show main window:
		self.mainwindow.Show()
		# Execute GUI:
		self.app.MainLoop()

	def Stop(self):
		log("Server (wx) stopped.")
