#!/usr/bin/python

import wx

from log import log
from client_gui import WindowMain
# from client_gui import WindowSettings	# For some reason it works without this
from config import Config

# Client
# Client with command interface

class Client:
	def __init__(self, filename_config):
		self.filename_config = filename_config

		# Read configuration:
		self.config = Config()
		self.config.load(filename_config)

	def run(self):
		pass

# ClientWx
# Client with wxWidgets GUI

class ClientWx(Client):
	def __init__(self, filename_config, makeconsole):
		Client.__init__(self, filename_config)
		
		# Create wxwidgets application:
		if makeconsole:
			self.app = wx.App(self)		# With separate log console window
		else:
			self.app = wx.App(None)		# Without separate log console window
		self.mainwindow = WindowMain(parent = None)
		self.mainwindow.set_main(self)
		#self.mainwindow = Mainwindow(parent=self)
		self.mainwindow.comboBox_Preset.Append(self.config.parameters["autoconnect_preset"])

		# Update parameters in mainwindow:
		# mainwindow.comboBox_Room = self.config.parameters[room]
		self.mainwindow.textCtrl_Callsign.SetValue(self.config.parameters["callsign"])
		self.mainwindow.textCtrl_Description.SetValue(self.config.parameters["description"])
		# mainwindow.choice_Speaker = self.config.parameters[device_speaker]
		# mainwindow.choice_Mic = self.config.parameters[device_mic]

		# Get available sound devices:
			# get_audiodevices()
		# Put them into choice widgets:
			# self.mainwindow.choice_Speaker.Append()
			# self.mainwindow.choice_Mic.Append()

	def run(self):
		log("Starting client.")
		# Show main window:
		self.mainwindow.Show()
		# Execute GUI:
		self.app.MainLoop()


import terminalgui

# ClientCurses
# Client with Curses TUI

# Commands:
# connect, disconnect, nick, description, talkon, talkoff, set, get, join, part, save

class ClientCurses:
	def __init__(self, filename):
		line = ""

		while line != "quit":
			line = input("Prompt: ")
			# TODO: parse command
			#print (line)