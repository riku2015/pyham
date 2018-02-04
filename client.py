#!/usr/bin/python

import wx

from log import log
from client_gui import Mainwindow
from client_gui import Settingswindow
from config import Config
from client_protocols import ClientProtocolFrn
from testcode import get_audiodevices

class Client:
	def __init__(self, filename_config):
		self.filename_config = filename_config

		# Create wxwidgets application:
		#self.app = wx.App(self)	# With separate log console window
		self.app = wx.App(None)		# Without separate log console window
		self.mainwindow = Mainwindow(parent=None)

		# Read configuration:
		self.config = Config()
		self.config.load(filename_config)

		# TODO:
			# Update parameters in mainwindow:
				# mainwindow.comboBox_Room = self.config.parameters[room]
				# mainwindow.choise_Callsign = self.config.parameters[callsign]
				# mainwindow.textCtrl_Description = self.config.parameters[description]
				# mainwindow.choice_Speaker = self.config.parameters[device_speaker]
				# mainwindow.choice_Mic = self.config.parameters[device_mic]

				# Set audio device names to choive_Speaker and choice_Mic
					# self.mainwindow.choice_Speaker.setlabel(get_audiodevices())

			# Update parameters in settingswindow:
				# settingswindow.choise_Preset = self.config.parameters[]
				# settingswindow.choise_Room = self.config.parameters[]
				# settingswindow.checkBox_Autosave = self.config.parameters[]
				# settingswindow.choice_Speaker = self.config.parameters[device_speaker]
				# settingswindow.choice_Mic = self.config.parameters[device_mic]

	def Run(self):
		log("Starting client.")
		# Show main window:
		self.mainwindow.Show()
		# Execute GUI:
		self.app.MainLoop()

	def connect(self):
		pass
