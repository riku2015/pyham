#!/usr/bin/python

from log import log
from server_gui_fbp import FrameMain

class Mainwindow(FrameMain):
	def __init__(self,parent):
		FrameMain.__init__(self,parent)

	def click_quit( self, event ):
		# TODO: autosave
		self.Close()

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

	def click_eqso_apply( self, event ):
		pass

	def click_eqso_start( self, event ):
		pass

	def click_echolink_apply( self, event ):
		pass

	def click_echolink_start( self, event ):
		pass

	def click_frn_apply( self, event ):
		pass

	def click_frn_start( self, event ):
		pass

	def click_pyhamp_apply( self, event ):
		pass

	def click_pyhamp_start( self, event ):
		pass
