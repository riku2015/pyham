#!/usr/bin/python

import wx
import wave
import pyaudio
from log import log
from client_gui_fbp import FrameMain, FrameSettings
from testcode import play_testsound
from client_protocols import ClientProtocolFrn, ClientProtocolPyhamp
#from testcode import Test_Audiorecorder

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

		except Exception, e:
			log('Error while streaming recording: ' + str(e))

	def release_ptt(self, event):
		try:
			log("PTT button released, end recording to server.")
			# Set PTT button color to green:
			self.button_Ptt.SetBackgroundColour(wx.Colour(186, 216, 200))
			self.button_Ptt.SetLabel("Push To Talk")
			# Roger beep
		except Exception, e:
			log('Error: ' + str(e))

	def click_load(self, event):
		try:
			# Load preset
			log('Load preset.')
		except Exception, e:
			log('Error while loading preset: ' + str(e))

	def click_delete(self, event):
		try:
			# Delete preset
			dialog_delete = wx.MessageDialog(None, 'Delete preset?', 'Confirm delete', wx.YES_NO | wx.ICON_QUESTION)
			result = dialog_delete.ShowModal()
			if result == wx.ID_YES:
				log('Delete preset.')
		except Exception, e:
			log('Error while deleting preset: \n + str(e)')

	def click_save(self,event):
		try:
			# Save preset
			log('Save preset.')
		except Exception, e:
			log('Error while saving preset: ' + str(e))

	def choose_room(self, event):
		log("Room changed.")

	def click_connect(self, event):
		try:
			# Connect to server
			# (disconnect current connection before trying to make a new connection)
			
			if self.button_Connect.GetLabel() == "Connect":
				# Make connection:
				self.frn = ClientProtocolFrn("frn.titanix.net", 10024)
				self.frn.connect()
				self.frn.send("")
				#self.pyhamp = ClientProtocolPyhamp("localhost", 1000)
				#self.pyhamp.connect()
				# client.connect()
				
				# If successfully connected:
				play_testsound()
				self.button_Connect.SetLabel("Disconnect")
			else:
				# If successfully disconnected:
				self.button_Connect.SetLabel("Connect")
				log("Disconnected.")
			
			
			#log("Connected to server.")
			#log("Disconnect from server.")
		except Exception, e:
			log('Error while connecting to server: ' + str(e))
			#log('Error while disconnecting from server: ' + str(e))

	def click_send(self, event):
		try:
			log("Send to server.")
		except Exception, e:
			log('Error while sending to server: ' + str(e))

	def click_settings(self, event):
		self.settingswindow = Settingswindow(None)
		self.settingswindow.Show()

	def volume_speaker(self, event):
		log("Speaker volume: " + str(self.slider_Speaker.Value))
	
	def volume_mic(self, event):
		log("Mic volume: " + str(self.slider_Mic.Value))

	def choose_speaker(self, event):
		log("Speaker device changed to " + str(self.choice_Speaker.GetSelection()) + ".")

	def choose_mic(self, event):
		log("Mic device changed to " + str(self.choice_Mic.GetSelection()) + ".")
