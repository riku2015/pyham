#!/usr/bin/python

from log import log
from config import Config
from server_protocols import *
from server_gui import WindowMain
# from server_gui import WindowStats	# For some reason it works without this
# from server_gui import WindowSettings	# For some reason it works without this

# One server can use one or more different protocols at the same time.
# Only one instance of a certain protocol can be used within one server at the same time.

# Server
# Server with command interface

class Server:
	def __init__(self, filename_config):
		self.filename_config = filename_config

		# Defaults if not given in config file:
		# TODO

		# Read configuration and give default values if absent:
		self.config = Config(
			parameters = {
				"config_version": "0.10",
				"autosave": "off",
				"device_speaker": "",
				"device_mic": "",
				"device_ptt": "",
				"volume_speaker": "50",
				"volume_mic": "50",
				"volume_roger": "50",
				"volume_connect": "50",
				"volume_disconnect": "50",
				"recorder_path": "../recordings",
				"recorder_format": "wav",
				"overlap": "discard",
				"pyham_enabled": "off",
				"pyham_name": "",
				"pyham_port": "2000",
				"eqso_enabled": "off",
				"eqso_name": "",
				"eqso_port": "5000",
				"frn_enabled": "off",
				"frn_name": "",
				"frn_port": "10024",
				"echolink_enabled": "off",
				"echolink_name": "",
				"echolink_port": "5198",
				"rooms": "[]",
				"max_connections": "-1",
				"allowed_hosts": "[]",
				"allowed_ips": "[]",
				"banned_hosts": "[]",
				"banned_ips": "[]"
			}
		)
		self.config.load(filename_config)

		# Initialize protocol(s):

		if self.config.parameters["frn_enabled"]:
			self.frn = ServerProtocolFrn(self.config.parameters["frn_name"], self.config.parameters["frn_port"])

		if self.config.parameters["eqso_enabled"]:
			self.eqso = ServerProtocolEqso(self.config.parameters["eqso_name"], self.config.parameters["eqso_port"])

		if self.config.parameters["echolink_enabled"]:
			self.echolink = ServerProtocolEcholink(self.config.parameters["echolink_name"], self.config.parameters["echolink_port"])

		if self.config.parameters["pyham_enabled"]:
			self.pyham = ServerProtocolPyham(self.config.parameters["pyham_name"], self.config.parameters["pyham_port"])

	def run(self):
		log("Starting server.")
		if self.config.parameters["frn_enabled"] == "on":
			self.frn.run()			# Frn protocol is now accepting connections
		if self.config.parameters["echolink_enabled"] == "on":
			self.echolink.run()		# Echolink protocol is now accepting connections
		if self.config.parameters["eqso_enabled"] == "on":
			self.eqso.run()			# Eqso protocol is now accepting connections
		if self.config.parameters["pyham_enabled"] == "on":
			self.pyham.run()		# Pyham protocol is now accepting connections

	def stop(self):
		log("Server stopped.")

import terminalgui

# ServerCurses
# Server with Curses TUI

# Commands:
# get, set, start, stop, ban, unban, createroom, deleteroom, save
# Parameters:
#

class ServerCurses(Server):
	def __init__(self, filename):
		line = ""

		while line != "quit":
			line = input("Prompt: ")

import wx

# ServerWx
# Server with wxWidgets GUI

class ServerWx(Server):
	def __init__(self, filename_config, makeconsole):
		Server.__init__(self, filename_config)
		# Create wxwidgets application:
		if makeconsole:
			self.app = wx.App(self)	# With separate log console window
		else:
			self.app = wx.App(None)		# Without separate log console window
		self.mainwindow = WindowMain(parent=None)
		self.mainwindow.set_main(self)

	def run(self):
		log("Starting server (wx).")
		if self.config.parameters["frn_enabled"] == "on" and self.frn.run():
			self.mainwindow.staticText_FrnState.SetLabel("Running")			# Frn protocol is now accepting connections
		if self.config.parameters["echolink_enabled"] == "on" and self.echolink.run():
			self.mainwindow.staticText_EcholinkState.SetLabel("Running")	# Echolink protocol is now accepting connections
		if self.config.parameters["eqso_enabled"] == "on" and self.eqso.run():
			self.mainwindow.staticText_EqsoState.SetLabel("Running")		# Eqso protocol is now accepting connections
		if self.config.parameters["pyham_enabled"] == "on" and self.pyham.run():
			self.mainwindow.staticText_PyhamState.SetLabel("Running")		# Pyham protocol is now accepting connections

		# Update main window text fields:
		self.mainwindow.textCtrl_EqsoName.SetValue(self.config.parameters["eqso_name"])
		self.mainwindow.textCtrl_EqsoPort.SetValue(self.config.parameters["eqso_port"])
		self.mainwindow.textCtrl_EcholinkName.SetValue(self.config.parameters["echolink_name"])
		self.mainwindow.textCtrl_EcholinkPort.SetValue(self.config.parameters["echolink_port"])
		self.mainwindow.textCtrl_FrnName.SetValue(self.config.parameters["frn_name"])
		self.mainwindow.textCtrl_FrnPort.SetValue(self.config.parameters["frn_port"])
		self.mainwindow.textCtrl_PyhamName.SetValue(self.config.parameters["pyham_name"])
		self.mainwindow.textCtrl_PyhamPort.SetValue(self.config.parameters["pyham_port"])
		# Disable Apply buttons until user changes the values:
		self.mainwindow.button_EqsoApply.Enable(False)
		self.mainwindow.button_EcholinkApply.Enable(False)
		self.mainwindow.button_FrnApply.Enable(False)
		self.mainwindow.button_PyhamApply.Enable(False)
		# Show main window:
		self.mainwindow.Show()
		# Execute GUI:
		self.app.MainLoop()

	def stop(self):
		log("Server (wx) stopped.")
