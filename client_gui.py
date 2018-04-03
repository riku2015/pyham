#!/usr/bin/python

# client windows

# TODO:
# - Scalable widgets (different font size for low res & high res etc.)

import wx
from log import log
from audio import *
from client_protocols import *
from client_gui_fbp import FrameMain, FrameSettings

from testcode import *

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
		self.settingswindow = None
		self.Bind(EVT_ErrorAudiostreamer, self.OnRecordError)
		self.audiostreamer = Audiostreamer(self)
		self.recorder = Recorder(self)

	def push_ptt(self, event):
		try:
			log("PTT button pushed down, recording audio to server...")

			# Set PTT button color to red:
			self.button_Ptt.SetBackgroundColour(wx.Colour(216, 186, 200))
			self.button_Ptt.SetLabel("Recording...")

			# Record and stream audio to server:
			self.recorder = Recorder(self)
			self.recorder.running = True
			self.recorder.start()
			self.audiostreamer = Audiostreamer(self)
			self.audiostreamer.running = True
			self.audiostreamer.start()

		except Exception, e:
			log('Error while streaming recording: ' + str(e))

	def release_ptt(self, event):
		try:
			log("PTT button released, end recording to server.")

			self.audiostreamer.running = False
			# Set PTT button color to green:
			self.button_Ptt.SetBackgroundColour(wx.Colour(186, 216, 200))
			self.button_Ptt.SetLabel("Push To Talk")

			# Stop recording thread:
			self.audiostreamer.stop()
			self.recorder.stop()

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
		# Connect to room
		log("Room changed.")

	def choose_Preset( self, event ):
		# TODO: Update text fields when preset selected
		#self.textCtrl_Server.SetValue(self.config.parameters["presets"])
		#self.textCtrl_Port.SetValue(self.config.parameters["presets"])
		#self.choice_Protocol
		pass

	def click_connect(self, event):
		try:
			# Connect to server
			# (disconnect current connection before trying to make a new connection)
			
			if self.button_Connect.GetLabel() == "Connect":
				# Make connection:
				protocol = self.choice_Protocol.GetSelection()
				if protocol == 0:
					self.protocol = ClientProtocolEcholink(self.textCtrl_Server.GetValue(), int(self.textCtrl_Port.GetValue()))
				elif protocol == 1:
					self.protocol = ClientProtocolEqso(self.textCtrl_Server.GetValue(), int(self.textCtrl_Port.GetValue()))
				elif protocol == 2:
					self.protocol = ClientProtocolFrn(self.textCtrl_Server.GetValue(), int(self.textCtrl_Port.GetValue()))
				elif protocol == 3:
					self.protocol = ClientProtocolPyhamp(self.textCtrl_Server.GetValue(), int(self.textCtrl_Port.GetValue()))
				self.protocol.connect()
				self.protocol.send("")
				
				# If successfully connected:
				#play_sound("sound.wav")
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
		if not self.settingswindow:
			# Closes automatically when main window closes:
			self.settingswindow = Settingswindow(self)
			# Persistent when main window closes:
			#self.settingswindow = Settingswindow(None)
		self.settingswindow.Show()

	def volume_speaker(self, event):
		log("Speaker volume: " + str(self.slider_Speaker.Value))
	
	def volume_mic(self, event):
		log("Mic volume: " + str(self.slider_Mic.Value))

	def choose_speaker(self, event):
		log("Speaker device changed to " + str(self.choice_Speaker.GetSelection()) + ".")

	def choose_mic(self, event):
		log("Mic device changed to " + str(self.choice_Mic.GetSelection()) + ".")

	def OnRecordError(self, evt):
		# Set PTT button color to green:
		self.button_Ptt.SetBackgroundColour(wx.Colour(186, 216, 200))
		self.button_Ptt.SetLabel("Push To Talk")
