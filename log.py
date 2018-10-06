#!/usr/bin/python

import sys
from datetime import datetime
import wx

# TODO:
# - Logging options: stdout, stderr, file, window...
# - Set filename from command line parameter
# - Verbose, normal and quiet mode

def log(text, filename = None):
	# Format text with timestamp:
	string = "[" + datetime.now().strftime('%Y/%m/%d %H:%M:%S') + "] " + text

	# Print to console:
	#print >>sys.stderr, string
	print (string)
	
	# Append to file:
	if filename != None:
		with open(filename, "a") as logfile:
			logfile.write(string + "\n")

class Log:
	def __init__(self, filename):
		self.filename = filename
		self.history = ""

	def write(text):
		# Format text with timestamp:
		string = "[" + datetime.now().strftime('%Y/%m/%d %H:%M:%S') + "] " + text

		# Add to history:
		self.history += text + "\n"	# TODO: List object

		# Print to console:
		print >>sys.stderr, string

		# Append to file:
		if self.filename != None:
			with open(filename, "a") as logfile:
				logfile.write(string + "\n")

	def gethistory():
		return this.history

def error(parent, message, caption='Error'):
	log("ERROR: " + message)
	dialogError = wx.MessageDialog(parent, "ERROR:\n" + message, caption, wx.OK | wx.ICON_WARNING)
	dialogError.ShowModal()
	dialogError.Destroy()
