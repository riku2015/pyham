#!/usr/bin/python

# server windows

import wx
from log import log
from server_gui_fbp import FrameMain, FrameSettings, FrameStats
from server_protocols import ServerProtocolEqso

class WindowStats(FrameStats):
	def __init__(self,parent):
		FrameStats.__init__(self,parent)

class WindowSettings(FrameSettings):
	def __init__(self,parent):
		FrameSettings.__init__(self,parent)

	def set_main(self, main):
		# Used to access Client (parent) object's variables/functions
		self.main = main

	def apply_changes(self):
		# Apply changes to config

		self.main.config.parameters["echolink_name"] = self.textCtrl_EcholinkName.GetValue()
		self.main.config.parameters["echolink_port"] = self.textCtrl_EcholinkPort.GetValue()
		if self.checkBox_EcholinkAutostart.GetValue():
			self.main.config.parameters["echolink_enabled"] = "on"
		else:
			self.main.config.parameters["echolink_enabled"] = "off"
		
		self.main.config.parameters["eqso_name"] = self.textCtrl_EqsoName.GetValue()
		self.main.config.parameters["eqso_port"] = self.textCtrl_EqsoPort.GetValue()
		if self.checkBox_EqsoAutostart.GetValue():
			self.main.config.parameters["eqso_enabled"] = "on"
		else:
			self.main.config.parameters["eqso_enabled"] = "off"

		self.main.config.parameters["frn_name"] = self.textCtrl_FrnName.GetValue()
		self.main.config.parameters["frn_port"] = self.textCtrl_FrnPort.GetValue()
		if self.checkBox_FrnAutostart.GetValue():
			self.main.config.parameters["frn_enabled"] = "on"
		else:
			self.main.config.parameters["frn_enabled"] = "off"

		self.main.config.parameters["pyham_name"] = self.textCtrl_PyhamName.GetValue()
		self.main.config.parameters["pyham_port"] = self.textCtrl_PyhamPort.GetValue()
		if self.checkBox_PyhamAutostart.GetValue():
			self.main.config.parameters["pyham_enabled"] = "on"
		else:
			self.main.config.parameters["pyham_enabled"] = "off"

		if self.checkBox_Autosave.GetValue():
			self.main.config.parameters["autosave"] = "on"
		else:
			self.main.config.parameters["autosave"] = "off"

		self.main.config.parameters["recorder_path"] = self.textCtrl_RecordingPath.GetValue()
		if self.choice_Format.GetSelection() == 0:
			self.main.config.parameters["recorder_format"] = "wav"
		elif self.choice_Format.GetSelection() == 1:
			self.main.config.parameters["recorder_format"] = "mp3"
		elif self.choice_Format.GetSelection() == 2:
			self.main.config.parameters["recorder_format"] = "flac"

		if self.choice_Overlap.GetSelection() == 0:
			self.main.config.parameters["overlap"] = "discard"
		elif self.choice_Overlap.GetSelection() == 1:
			self.main.config.parameters["overlap"] = "mix"
		elif self.choice_Overlap.GetSelection() == 2:
			self.main.config.parameters["overlap"] = "queue"

		self.main.config.parameters["max_connections"] = self.textCtrl_MaxConnections.GetValue()

		# TODO: Rooms
		# self.main.config.parameters[] =

		# TODO: PTT trigger value
		# self.main.config.parameters[] =

	def click_recorderpath( self, event):
		with wx.DirDialog(self, "Choose recording folder", style=wx.DD_DIR_MUST_EXIST) as dirDialog:
			if dirDialog.ShowModal() == wx.ID_CANCEL:
				return
			self.textCtrl_RecordingPath.SetValue(dirDialog.GetPath())

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
	def __init__(self, parent):
		FrameMain.__init__(self, parent)
		self.settingswindow = None
		self.statswindow = None

	def set_main(self, main):
		# Used to access Server (parent) object's variables/functions
		self.main = main

	def click_quit( self, event ):
		# TODO: autosave
		# if self.autosave:
		# 	self.main.config.save()
		self.Close()

	def click_settings( self, event ):
		if not self.settingswindow:
			# Closes automatically when main window closes:
			self.settingswindow = WindowSettings(self)
			self.settingswindow.set_main(self.main)
			# Persistent when main window closes:
			#self.settingswindow = Settingswindow(None)

			# Update settings window text fields:
			self.settingswindow.textCtrl_EqsoName.SetValue(self.main.config.parameters["eqso_name"])
			self.settingswindow.textCtrl_EqsoPort.SetValue(self.main.config.parameters["eqso_port"])

			self.settingswindow.textCtrl_EcholinkName.SetValue(self.main.config.parameters["echolink_name"])
			self.settingswindow.textCtrl_EcholinkPort.SetValue(self.main.config.parameters["echolink_port"])
			
			self.settingswindow.textCtrl_FrnName.SetValue(self.main.config.parameters["frn_name"])
			self.settingswindow.textCtrl_FrnPort.SetValue(self.main.config.parameters["frn_port"])
			
			self.settingswindow.textCtrl_PyhamName.SetValue(self.main.config.parameters["pyham_name"])
			self.settingswindow.textCtrl_PyhamPort.SetValue(self.main.config.parameters["pyham_port"])
			
			if self.main.config.parameters["autosave"] == "on":
				self.settingswindow.checkBox_Autosave.SetValue(True)
			elif self.main.config.parameters["autosave"] == "off":
				self.settingswindow.checkBox_Autosave.SetValue(False)

			self.settingswindow.textCtrl_RecordingPath.SetValue(self.main.config.parameters["recorder_path"])
			if self.main.config.parameters["recorder_format"] == "wav":
				self.settingswindow.choice_Format.SetSelection(0)
			elif self.main.config.parameters["recorder_format"] == "mp3":
				self.settingswindow.choice_Format.SetSelection(1)
			elif self.main.config.parameters["recorder_format"] == "flac":
				self.settingswindow.choice_Format.SetSelection(2)

			if self.main.config.parameters["overlap"] == "discard":
				self.settingswindow.choice_Overlap.SetSelection(0)
			elif self.main.config.parameters["overlap"] == "mix":
				self.settingswindow.choice_Overlap.SetSelection(1)
			elif self.main.config.parameters["overlap"] == "queue":
				self.settingswindow.choice_Overlap.SetSelection(2)

			self.settingswindow.textCtrl_MaxConnections.SetValue(self.main.config.parameters["max_connections"])

		self.settingswindow.Show()

	def click_load( self, event ):
		log("Load.")

	def click_save( self, event ):
		log("Saved.")

	def click_allow( self, event ):
		log("Allow.")
	
	def click_ban( self, event ):
		log("Ban.")

	def click_stats( self, event ):
		# Open stats window
		if not self.statswindow:
			# Closes automatically when main window closes:
			self.statswindow = WindowStats(self)
			# Persistent when main window closes:
			#self.settingswindow = Settingswindow(None)
		self.statswindow.Show()

	def click_eqso_apply( self, event ):
		self.button_EqsoApply.Enable(False)

	def click_eqso_start( self, event ):
		if self.button_EqsoStart.GetLabel() == "Start":		# TODO: Get from class boolean variable
			if self.main.eqso != None:
				self.main.eqso = ServerProtocolEqso(self.textCtrl_EqsoName.GetValue(), self.textCtrl_EqsoPort.GetValue())
			self.main.eqso.run()
			# If successfully started:
			self.button_EqsoStart.SetLabel("Stop")
			self.staticText_EqsoState.SetLabel("Running")
		else:
			self.main.eqso.close()
			# If successfully Stopped:
			self.button_EqsoStart.SetLabel("Start")
			self.staticText_EqsoState.SetLabel("Stopped")

	def click_echolink_apply( self, event ):
		self.button_EcholinkApply.Enable(False)

	def click_echolink_start( self, event ):
		if self.button_EcholinkStart.GetLabel() == "Start":		# TODO: Get from class boolean variable
			self.main.echolink.run()
			# If successfully started:
			self.button_EcholinkStart.SetLabel("Stop")
			self.staticText_EcholinkState.SetLabel("Running")
		else:
			self.echolink.close()
			# If successfully Stopped:
			self.button_EcholinkStart.SetLabel("Start")
			self.staticText_EcholinkState.SetLabel("Stopped")

	def click_frn_apply( self, event ):
		self.button_FrnApply.Enable(False)

	def click_frn_start( self, event ):
		if self.button_FrnStart.GetLabel() == "Start":		# TODO: Get from class boolean variable
			self.main.frn.run()
			# If successfully started:
			self.button_FrnStart.SetLabel("Stop")
			self.staticText_FrnState.SetLabel("Running")
		else:
			self.frn.close()
			# If successfully stopped:
			self.button_FrnStart.SetLabel("Start")
			self.staticText_FrnState.SetLabel("Stopped")

	def click_pyham_apply( self, event ):
		self.button_PyhamApply.Enable(False)

	def click_pyham_start( self, event ):
		if self.button_PyhamStart.GetLabel() == "Start":		# TODO: Get from class boolean variable
			self.main.pyham.run()
			# If successfully started:
			self.button_PyhamStart.SetLabel("Stop")
			self.staticText_PyhamState.SetLabel("Running")
		else:
			self.pyham.close()
			# If successfully Stopped:
			self.button_PyhamStart.SetLabel("Start")
			self.staticText_PyhamState.SetLabel("Stopped")

	def text_Echolink(self, event):
		# Name or Port changed, enable Apply button:
		self.button_EcholinkApply.Enable(True)

	def text_Eqso(self, event):
		# Name or Port changed, enable Apply button:
		self.button_EqsoApply.Enable(True)

	def text_Frn(self, event):
		# Name or Port changed, enable Apply button:
		self.button_FrnApply.Enable(True)

	def text_Pyham(self, event):
		# Name or Port changed, enable Apply button:
		self.button_PyhamApply.Enable(True)