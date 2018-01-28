#!/usr/bin/python

import wx
import wave
import pyaudio
from log import log
from client_gui_fbp import FrameMain, FrameSettings
from tests import play_testsound
from client_protocols import ClientProtocolFrn
#from tests import Test_Audiorecorder

class Settingswindow(FrameSettings):
	def __init__(self,parent):
		FrameSettings.__init__(self,parent)

	def click_ok( self, event ):
		# Apply changes
		# Close window:
		self.Close()
	
	def click_save( self, event ):
		log("Save settings.")
	
	def click_cancel( self, event ):
		# Close window:
		self.Close()

class Mainwindow(FrameMain):
	def __init__(self,parent):
		FrameMain.__init__(self,parent)

		# Get available sound devices:
		# print get_devices()
		# Put them into comboBoxes:
		# self.comboBox_Speaker.
		# self.comboBox_Mic

	def push_ptt(self, event):
		try:
			log("PTT button pushed down, recording audio to server...")
			# Set PTT button color to red:
			self.button_Ptt.SetBackgroundColour(wx.Colour(216, 186, 200))
			self.button_Ptt.SetLabel("Recording...")

			# Record sound:
			# recorder = Test_Audiorecorder()
			# recorder.rec()

			# Stream using current protocol:
			#

			# TODO:
			# Keep recording and streaming until PTT button released.
			# Do not get stuck in a loop here. (threading?)

		except:
			log('Error: cannot stream recording.')

	def release_ptt(self, event):
		try:
			log("PTT button released, end recording to server.")
			# Set PTT button color to green:
			self.button_Ptt.SetBackgroundColour(wx.Colour(186, 216, 200))
			self.button_Ptt.SetLabel("Push To Talk")
			# Roger beep
		except:
			log('Error.')

	def click_load(self, event):
		try:
			# Load preset
			log('Load preset.')
		except:
			log('Error: cannot load preset.')

	def click_delete(self, event):
		try:
			# Delete preset
			dialog_delete = wx.MessageDialog(None, 'Delete preset?', 'Confirm delete', wx.YES_NO | wx.ICON_QUESTION)
			result = dialog_delete.ShowModal()
			if result == wx.ID_YES:
				log('Delete preset.')
		except:
			log('Error: cannot delete preset.')

	def click_save(self,event):
		try:
			# Save preset
			log('Save preset.')
		except:
			log('Error: cannot save preset.')

	def choose_room(self, event):
		log("Room changed.")

	def click_connect(self, event):
		#try:
			# Connect to server
			# (disconnect current connection before trying to make a new connection)
			
			# Test connection:
			self.frn = ClientProtocolFrn("frn.titanix.net", 10024)
			self.frn.connect()
			self.frn.send("")

			# If successfull, disable connect button and enable disconnect button:
			self.button_Connect.Disable()
			self.button_Disconnect.Enable()
			# client.connect()

			# If successfull, play sound:
			play_testsound()
		#except:
			log('Error: cannot connect to server.')

	def click_disconnect(self, event):
		try:
			log("Disconnect from server.")
			# Enable connect button and disable disconnect button:
			self.button_Connect.Enable()
			self.button_Disconnect.Disable()
		except:
			log('Error.')

	def click_send(self, event):
		try:
			log("Send to server.")
		except:
			log('Error: cannot send to server.')

	def click_settings(self, event):
		self.settingswindow = Settingswindow(None)
		self.settingswindow.Show()

	def volume_speaker(self, event):
		log("Speaker volume: " + str(self.slider_Speaker.Value))
	
	def volume_mic(self, event):
		log("Mic volume: " + str(self.slider_Mic.Value))

	def choose_speaker(self, event):
		log("Speaker device changed.")

	def choose_mic(self, event):
		log("Mic device changed.")
