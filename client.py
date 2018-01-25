#!/usr/bin/python

import wx

from pyham import log, Config, ProtocolPyhamp, ProtocolEqso, ProtocolEcholink, ProtocolFrn
from tests import ClientConnection_Eqso
from client_gui import Mainwindow

# Defaults if not given in config file:
server_name = "frn.titanix.net"
server_port = 10024
server_protocol = "frn"

class Client:
	def __init__(self, filename_config):

		# Create wxwidgets application:
		app = wx.App(False)
		mainwindow = Mainwindow(parent=None)

		# Show main window:
		mainwindow.Show()

		# Execute GUI:
		app.MainLoop()
