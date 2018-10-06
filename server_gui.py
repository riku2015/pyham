#!/usr/bin/python

# server windows

# TODO:
# - Scalable widgets (different font size for low res & high res etc.)

from log import log
from server_gui_fbp import FrameMain, FrameSettings, FrameStats

class WindowStats(FrameStats):
	def __init__(self,parent):
		FrameStats.__init__(self,parent)

class WindowSettings(FrameSettings):
	def __init__(self,parent):
		FrameSettings.__init__(self,parent)

	def click_ok( self, event ):
		# Apply changes
		# Close window:
		self.Close()

	def click_save( self, event ):
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
		self.Close()

	def click_settings( self, event ):
		if not self.settingswindow:
			# Closes automatically when main window closes:
			self.settingswindow = WindowSettings(self)
			# Persistent when main window closes:
			#self.settingswindow = Settingswindow(None)
		self.settingswindow.Show()

	def click_load( self, event ):
		log("Load.")

	def click_save( self, event ):
		log("Save.")

	def click_log( self, event ):
		# Show log window
		pass

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
		pass

	def click_eqso_apply( self, event ):
		pass

	def click_eqso_start( self, event ):
		if self.button_EqsoStart.GetLabel() == "Start":
			#self.eqso.run()
			# If successfully started:
			self.button_EqsoStart.SetLabel("Stop")
			self.staticText_EqsoState.SetLabel("Running")
		else:
			#self.eqso.disconnect()
			# If successfully Stopped:
			self.button_EqsoStart.SetLabel("Start")
			self.staticText_EqsoState.SetLabel("Stopped")

	def click_echolink_apply( self, event ):
		pass

	def click_echolink_start( self, event ):
		if self.button_EcholinkStart.GetLabel() == "Start":
			#self.echolink.run()
			# If successfully started:
			self.button_EcholinkStart.SetLabel("Stop")
			self.staticText_EcholinkState.SetLabel("Running")
		else:
			#self.echolink.disconnect()
			# If successfully Stopped:
			self.button_EcholinkStart.SetLabel("Start")
			self.staticText_EcholinkState.SetLabel("Stopped")

	def click_frn_apply( self, event ):
		pass

	def click_frn_start( self, event ):
		if self.button_FrnStart.GetLabel() == "Start":
			#self.frn.run()
			# If successfully started:
			self.button_FrnStart.SetLabel("Stop")
			self.staticText_FrnState.SetLabel("Running")
		else:
			#self.frn.disconnect()
			# If successfully Stopped:
			self.button_FrnStart.SetLabel("Start")
			self.staticText_FrnState.SetLabel("Stopped")

	def click_pyhamp_apply( self, event ):
		pass

	def click_pyhamp_start( self, event ):
		if self.button_PyhampStart.GetLabel() == "Start":
			#self.pyhamp.run()
			# If successfully started:
			self.button_PyhampStart.SetLabel("Stop")
			self.staticText_PyhampState.SetLabel("Running")
		else:
			#self.pyhamp.disconnect()
			# If successfully Stopped:
			self.button_PyhampStart.SetLabel("Start")
			self.staticText_PyhampState.SetLabel("Stopped")
