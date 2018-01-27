#!/usr/bin/python

import wx
import wave
import pyaudio
from log import log
from client_gui_fbp import FrameMain, FrameSettings
from tests import get_devices

class Settingswindow(FrameSettings):
	def __init__(self,parent):
		# Initialize parent class:
		FrameSettings.__init__(self,parent)

	def click_ok( self, event ):
		# Apply changes
		# Close window
		self.Close()
	
	def click_save( self, event ):
		log("Save settings.")
	
	def click_cancel( self, event ):
		# Close window
		self.Close()

from tests import Test_Audiorecorder

class Mainwindow(FrameMain):
	def __init__(self,parent):
		# Initialize parent class:
		FrameMain.__init__(self,parent)

		# Get available sound devices:
		#print get_devices()
		# Put them into comboBoxes:
		# self.comboBox_Speaker.
		# self.comboBox_Mic

	def push_ptt(self,event):
		try:
			# Set PTT button color to red:
			self.button_Ptt.SetBackgroundColour(wx.Colour(216, 186, 200))
			self.button_Ptt.SetLabel("Recording...")
			log("PTT button pushed down, recording audio to server...")

			# Record sound:
			#recorder = Test_Audiorecorder()
			#recorder.rec()

			# Stream using current protocol:
			#

			# TODO:
			# Keep recording and streaming until PTT button released.
			# Do not get stuck in a loop here. (threading?)

		except Exception:
			log('Error')

	def release_ptt(self,event):
		try:
			log("PTT button released, end recording to server.")
			# Set PTT button color to green:
			self.button_Ptt.SetBackgroundColour(wx.Colour(186, 216, 200))
			self.button_Ptt.SetLabel("Push To Talk")
			# Roger beep
		except Exception:
			log('Error')

	def click_load(self,event):
		try:
			# Load preset
			log('Load preset.')
		except Exception:
			log('Error')

	def click_delete(self,event):
		try:
			# Delete preset
			dialog_delete = wx.MessageDialog(None, 'Delete preset?', 'Confirm delete', wx.YES_NO | wx.ICON_QUESTION)
			result = dialog_delete.ShowModal()
			if result == wx.ID_YES:
				log('Delete preset.')
		except Exception:
			log('Error')

	def click_save(self,event):
		try:
			# Save preset
			log('Save preset.')
		except Exception:
			log('Error')

	def click_connect(self,event):
		try:
			# Connect to server

			# If successfull, disable connect button and enable disconnect button:
			self.button_Connect.Disable()
			self.button_Disconnect.Enable()

			# If successfull, play sound:
			CHUNK = 1024
			wave_test = wave.open("sound.wav", 'rb')
			audio_test = pyaudio.PyAudio()
			stream_test = audio_test.open(format=audio_test.get_format_from_width(wave_test.getsampwidth()), channels=wave_test.getnchannels(), rate=wave_test.getframerate(), output=True)
			data_test = wave_test.readframes(CHUNK)
			while data_test != '':
				stream_test.write(data_test)
				data_test = wave_test.readframes(CHUNK)
			stream_test.stop_stream()
			stream_test.close()
			audio_test.terminate()
		except Exception:
			log('Error')

	def click_disconnect(self,event):
		try:
			log("Disconnect from server.")
			# Enable connect button and disable disconnect button:
			self.button_Connect.Enable()
			self.button_Disconnect.Disable()
		except Exception:
			log('Error')

	def click_send(self,event):
		try:
			log("Send to server.")
		except Exception:
			log('Error')

	def click_settings(self,event):
		try:
			self.settingswindow = Settingswindow(None)
			self.settingswindow.Show()
		except Exception:
			pass

	def volume_speaker( self, event ):
		log("Speaker volume: " + str(self.slider_Speaker.Value))
	
	def volume_mic( self, event ):
		log("Mic volume: " + str(self.slider_Mic.Value))
