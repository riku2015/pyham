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

		# Read configuration and give default values if absent:
		self.config = Config(
			parameters = {
				"config_version": "0.10",
				"presets": [],
				"autoconnect": "on",
				"autoconnect_preset": "",
				"autoconnect_room": "",
				"callsign": "Nick",
				"description": "",
				"device_speaker": "default",
				"device_mic": "default",
				"device_ptt": "ui",
				"soundfile_roger": "../audio/roger.wav",
				"soundfile_connect": "../audio/connect.wav",
				"soundfile_disconnect": "../audio/disconnect.wav",
				"recorder_path": "../recordings",
				"recorder_format": "wav",
				"record_roger": "on",
				"record_connect": "on",
				"record_disconnect": "on",
				"overlap": "discard",
				"play_roger": "on",
				"play_connect": "on",
				"play_disconnect": "on",
				"transmit_roger": "on",
				"volume_speaker": "50",
				"volume_mic": "50",
				"volume_roger": "50",
				"volume_connect": "50",
				"volume_disconnect": "50"
			}
		)
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
# get, set, connect, disconnect, talkon, talkoff, join, part, save
# Parameters:
# nick, description
# TODO: one or two letter aliases for commands

class ClientCurses(Client):
	def __init__(self, filename):
		line = ""

		while line != "quit":
			error = False
			line = input("Prompt: ")
			# Parse command:
			l = line.split(" ")		# TODO: may have multiple spaces, tabs etc.
			if l[0] == "get":
				if len(l[1]) < 1:
					error = True
			elif l[0] == "set":
				if len(l[1]) < 1:
					error = True
			elif l[0] == "connect":
				pass
			elif l[0] == "disconnect":
				pass
			elif l[0] == "talkon":
				pass
			elif l[0] == "talkoff":
				pass
			elif l[0] == "join":
				if len(l[1]) < 1:
					error = True
			elif l[0] == "part":
				pass
			elif l[0] == "save":
				pass
			if error:
				print ("Syntax error")
