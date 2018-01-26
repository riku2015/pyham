#!/usr/bin/python

import wx

from pyham import log, Config
#from pyham import ProtocolPyhamp, ProtocolEqso, ProtocolEcholink, ProtocolFrn
from client_gui import Mainwindow

# Defaults if not given in config file:
server_name = "frn.titanix.net"
server_port = 10024
server_protocol = "frn"

class Client:
	def __init__(self, filename_config):
		# Create wxwidgets application:
		self.app = wx.App(False)
		self.mainwindow = Mainwindow(parent=None)

	def Run(self):
		log("Starting client.")
		# Show main window:
		self.mainwindow.Show()
		# Execute GUI:
		self.app.MainLoop()

	def Stop(self):
		log("Client stopped.")
