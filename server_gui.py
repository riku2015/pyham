#!/usr/bin/python

from log import log
from server_gui_fbp import FrameMain

class Mainwindow(FrameMain):
	def __init__(self,parent):
		FrameMain.__init__(self,parent)

	def click_quit( self, event ):
		# TODO: autosave
		pass

	def click_settings( self, event ):
		pass

	def click_load( self, event ):
		log("Load.")

	def click_save( self, event ):
		log("Save.")

	def click_log( self, event ):
		pass

	def click_allow( self, event ):
		log("Allow.")
	
	def click_ban( self, event ):
		log("Ban.")

	def click_stats( self, event ):
		pass
