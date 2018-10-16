#!/usr/bin/python

# client windows

import wx
from log import *
from audio import *
from client_protocols import *
from client_gui_fbp import FrameMain, FrameSettings

from testcode import *

class WindowSettings(FrameSettings):
	def __init__(self,parent):
		FrameSettings.__init__(self,parent)

	def set_main(self, main):
		# Used to access Client (parent) object's variables/functions
		self.main = main

	def click_recorderpath( self, event):
		with wx.DirDialog(self, "Choose recording folder", style=wx.DD_DIR_MUST_EXIST) as dirDialog:
			if dirDialog.ShowModal() == wx.ID_CANCEL:
				return
			self.textCtrl_RecordingPath.SetValue(dirDialog.GetPath())
		
	def click_fileroger( self, event ):
		with wx.FileDialog(self, "Choose sound file", wildcard="WAV files (*.wav)|*.wav", style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
			if fileDialog.ShowModal() == wx.ID_CANCEL:
				return
			self.textCtrl_FileRoger.SetValue(fileDialog.GetPath())
	
	def click_fileconnect( self, event ):
		with wx.FileDialog(self, "Choose sound file", wildcard="WAV files (*.wav)|*.wav", style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
			if fileDialog.ShowModal() == wx.ID_CANCEL:
				return
			self.textCtrl_FileConnect.SetValue(fileDialog.GetPath())
	
	def click_filedisconnect( self, event ):
		with wx.FileDialog(self, "Choose sound file", wildcard="WAV files (*.wav)|*.wav", style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
			if fileDialog.ShowModal() == wx.ID_CANCEL:
				return
			self.textCtrl_FileDisconnect.SetValue(fileDialog.GetPath())

	def apply_changes(self):
		# Apply changes to config
		self.main.config.parameters["soundfile_roger"] = self.textCtrl_FileRoger.GetValue()
		self.main.config.parameters["soundfile_connect"] = self.textCtrl_FileConnect.GetValue()
		self.main.config.parameters["soundfile_disconnect"] = self.textCtrl_FileDisconnect.GetValue()
		self.main.config.parameters["callsign"] = self.textCtrl_Callsign.GetValue()
		if self.checkBox_PlayRoger.GetValue():
			self.main.config.parameters["play_roger"] = "on"
		else:
			self.main.config.parameters["play_roger"] = "off"
		
		if self.checkBox_PlayConnect.GetValue():
			self.main.config.parameters["play_connect"] = "on"
		else:
			self.main.config.parameters["play_connect"] = "off"

		if self.checkBox_PlayDisconnect.GetValue():
			self.main.config.parameters["play_disconnect"] = "on"
		else:
			self.main.config.parameters["play_disconnect"] = "off"

		if self.checkBox_TransmitRoger.GetValue():
			self.main.config.parameters["transmit_roger"] = "on"
		else:
			self.main.config.parameters["transmit_roger"] = "off"

		if self.checkBox_RecordRoger.GetValue():
			self.main.config.parameters["record_roger"] = "on"
		else:
			self.main.config.parameters["record_roger"] = "off"
		
		if self.checkBox_RecordConnect.GetValue():
			self.main.config.parameters["record_connect"] = "on"
		else:
			self.main.config.parameters["record_connect"] = "off"

		if self.checkBox_RecordDisconnect.GetValue():
			self.main.config.parameters["record_disconnect"] = "on"
		else:
			self.main.config.parameters["record_disconnect"] = "off"

		self.main.config.parameters["volume_speaker"] = str(self.spinCtrl_Speaker.GetValue())
		self.main.config.parameters["volume_mic"] = str(self.spinCtrl_Mic.GetValue())

		self.main.config.parameters["recorder_path"] = self.textCtrl_RecordingPath.GetValue()
		if self.choice_Format.GetSelection() == 0:
			self.main.config.parameters["recorder_format"] = "wav"
		elif self.choice_Format.GetSelection() == 1:
			self.main.config.parameters["recorder_format"] = "mp3"
		elif self.choice_Format.GetSelection() == 2:
			self.main.config.parameters["recorder_format"] = "flac"
	
	def click_ok( self, event ):
		self.apply_changes()
		# Close window:
		self.Close()

	def click_save( self, event ):
		self.apply_changes()
		self.main.config.save(self.main.filename_config)
		log("Settings saved.")

	def click_cancel( self, event ):
		# Close window:
		self.Close()

class WindowMain(FrameMain):
	def __init__(self,parent):
		FrameMain.__init__(self,parent)
		self.settingswindow = None
		self.Bind(EVT_ErrorAudiostreamer, self.OnRecordError)
		self.audiostreamer = Audiostreamer(self)
		self.recorder = Recorder(self)
		self.recordingtodisc = False	# TODO: Get from config, use Recorder class variable instead of this
		# TODO:
		# - insert extra widgets into form (VU meters etc.)

	def set_main(self, main):
		# Used to access Client (parent) object's variables/functions
		self.main = main

	def push_ptt(self, event):
		try:
			log("PTT button pushed down, recording audio to server...")

			# Set PTT button color to red:
			self.button_Ptt.SetBackgroundColour(wx.Colour(216, 186, 200))
			self.button_Ptt.SetLabel("Transmitting...")

			# Record and stream audio to server:
			self.recorder = Recorder(self)
			self.recorder.start()
			self.audiostreamer = Audiostreamer(self)
			self.audiostreamer.start()

		except Exception as e:
			# Set PTT button color to green:
			self.button_Ptt.SetBackgroundColour(wx.Colour(186, 216, 200))
			self.button_Ptt.SetLabel("Push To Talk")
			error(self, "while streaming recording: " + str(e))

	def release_ptt(self, event):
		try:
			log("PTT button released, end recording to server.")

			# Set PTT button color to green:
			self.button_Ptt.SetBackgroundColour(wx.Colour(186, 216, 200))
			self.button_Ptt.SetLabel("Push To Talk")

			# Stop recording thread:
			self.recorder.stop()
			self.audiostreamer.stop()

		except Exception as e:
			error(str(e))
			
	def click_load(self, event):
		try:
			# Load preset
			# Update text fields:
			self.textCtrl_Server.SetValue(self.main.config.parameters["presets"])
			#self.textCtrl_Port.SetValue(parent.config.parameters["presets"])
			#self.choice_Protocol.SetSelection(2)	# BOGUS
			log('Load preset.')
		except Exception as e:
			error(self, "while loading preset: " + str(e))

	def click_delete(self, event):
		try:
			# Delete preset
			dialog_delete = wx.MessageDialog(self, 'Delete preset?', 'Confirm delete', wx.YES_NO | wx.ICON_QUESTION)
			result = dialog_delete.ShowModal()
			if result == wx.ID_YES:
				log('Delete preset.')
		except Exception as e:
			error(self, "while deleting preset: \n + str(e)")

	def click_save(self,event):
		try:
			# Save preset
			log('Save preset.')
			# self.config.save()
		except Exception as e:
			error(self, "while saving preset: " + str(e))

	def choose_room(self, event):
		# Connect to room
		log("Room changed.")

	def choose_Preset( self, event ):
		# probably not needed
		pass

	def click_connect(self, event):
		if self.button_Connect.GetLabel() == "Connect":		# We are connecting
			if len(self.textCtrl_Server.GetValue()) > 0:
				if self.textCtrl_Port.GetValue().isdigit():
					
					# Make connection:
					protocol = self.choice_Protocol.GetSelection()
					if protocol == 0:
						self.protocol = ClientProtocolEcholink(self.textCtrl_Server.GetValue(), int(self.textCtrl_Port.GetValue()))
					elif protocol == 1:
						self.protocol = ClientProtocolEqso(self.textCtrl_Server.GetValue(), int(self.textCtrl_Port.GetValue()))
					elif protocol == 2:
						self.protocol = ClientProtocolFrn(self.textCtrl_Server.GetValue(), int(self.textCtrl_Port.GetValue()))
					elif protocol == 3:
						self.protocol = ClientProtocolPyham(self.textCtrl_Server.GetValue(), int(self.textCtrl_Port.GetValue()))
					self.protocol.connect()
					#self.protocol.send(b"")
					
					# If successfully connected:
					if self.main.config.parameters["soundfile_connect"] != None:
						play_sound(self.main.config.parameters["soundfile_connect"])
					self.button_Connect.SetLabel("Disconnect")
				else:
					error(self, "Invalid port.")
			else:
				error(self, "Invalid server address.")
		else:		# We are disconnecting
			self.protocol.disconnect()
			# If successfully disconnected:
			if self.main.config.parameters["soundfile_disconnect"] != None:
				play_sound(self.main.config.parameters["soundfile_disconnect"])
				self.button_Connect.SetLabel("Connect")

	def click_send(self, event):
		try:
			log("Send to server.")
		except Exception as e:
			log('while sending to server: ' + str(e))

	def click_Diskrecorder( self, event ):
		try:
			self.recordingtodisc = not self.recordingtodisc
		except Exception as e:
			self.recordingtodisc = False
		if self.recordingtodisc:
			# Stop recording:
			# self.recorder.stop()
			# Set discrecorder button color to red:
			self.button_Discrecorder.SetBackgroundColour(wx.Colour(216, 186, 200))
			self.button_Discrecorder.SetLabel("Recording...")
		else:
			# Start recording:
			# self.recorder.start()
			# Set discrecorder button color to normal:
			self.button_Discrecorder.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE))	# FIXME: Wrong color - so is wx.SYS_COLOUR_WINDOW
			self.button_Discrecorder.SetLabel("Record to disc")


	def click_settings(self, event):
		if not self.settingswindow:
			# Closes automatically when main window closes:
			self.settingswindow = WindowSettings(self)
			self.settingswindow.set_main(self.main)
			# Persistent when main window closes:
			#self.settingswindow = Settingswindow(None)
		# Set from config:
		self.settingswindow.textCtrl_FileRoger.SetValue(self.main.config.parameters["soundfile_roger"])
		self.settingswindow.textCtrl_FileConnect.SetValue(self.main.config.parameters["soundfile_connect"])
		self.settingswindow.textCtrl_FileDisconnect.SetValue(self.main.config.parameters["soundfile_disconnect"])
		self.settingswindow.textCtrl_Callsign.SetValue(self.main.config.parameters["callsign"])
		if self.main.config.parameters["play_roger"] == "on":
			self.settingswindow.checkBox_PlayRoger.SetValue(True)
		elif self.main.config.parameters["play_roger"] == "off":
			self.settingswindow.checkBox_PlayRoger.SetValue(False)
		
		if self.main.config.parameters["play_connect"] == "on":
			self.settingswindow.checkBox_PlayConnect.SetValue(True)
		elif self.main.config.parameters["play_connect"] == "off":
			self.settingswindow.checkBox_PlayConnect.SetValue(False)
		
		if self.main.config.parameters["play_disconnect"] == "on":
			self.settingswindow.checkBox_PlayDisconnect.SetValue(True)
		elif self.main.config.parameters["play_disconnect"] == "off":
			self.settingswindow.checkBox_PlayDisconnect.SetValue(False)
		
		if self.main.config.parameters["transmit_roger"] == "on":
			self.settingswindow.checkBox_TransmitRoger.SetValue(True)
		elif self.main.config.parameters["transmit_roger"] == "off":
			self.settingswindow.checkBox_TransmitRoger.SetValue(False)

		if self.main.config.parameters["record_roger"] == "on":
			self.settingswindow.checkBox_RecordRoger.SetValue(True)
		elif self.main.config.parameters["record_roger"] == "off":
			self.settingswindow.checkBox_RecordRoger.SetValue(False)

		if self.main.config.parameters["record_connect"] == "on":
			self.settingswindow.checkBox_RecordConnect.SetValue(True)
		elif self.main.config.parameters["record_connect"] == "off":
			self.settingswindow.checkBox_RecordConnect.SetValue(False)

		if self.main.config.parameters["record_disconnect"] == "on":
			self.settingswindow.checkBox_RecordDisconnect.SetValue(True)
		elif self.main.config.parameters["record_disconnect"] == "off":
			self.settingswindow.checkBox_RecordDisconnect.SetValue(False)

		self.settingswindow.textCtrl_RecordingPath.SetValue(self.main.config.parameters["recorder_path"])
		if self.main.config.parameters["recorder_format"] == "wav":
			self.settingswindow.choice_Format.SetSelection(0)
		elif self.main.config.parameters["recorder_format"] == "mp3":
			self.settingswindow.choice_Format.SetSelection(1)
		elif self.main.config.parameters["recorder_format"] == "flac":
			self.settingswindow.choice_Format.SetSelection(2)

		self.settingswindow.spinCtrl_Speaker.SetValue(self.main.config.parameters["volume_speaker"])
		self.settingswindow.spinCtrl_Mic.SetValue(self.main.config.parameters["volume_mic"])

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
