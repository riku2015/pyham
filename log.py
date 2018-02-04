#!/usr/bin/python

import sys
from datetime import datetime

# TODO:
# - Logging options: stdout, stderr, file, window...
# - Set filename from command line parameter

def log(text, filename = None):
	# Format text with timestamp:
	string = "[" + datetime.now().strftime('%Y/%m/%d %H:%M:%S') + "] " + text

	# Print to console:
	print >>sys.stderr, string

	# Append to file:
	if filename is not None:
		with open(filename, "a") as logfile:
			logfile.write(string + "\n")

'''
class Log:
	def __init__(self):
		self.text = ""

	def log(self, text, singleline = True):
		if singleline:
			self.text = "[" + datetime.now().strftime('%Y/%m/%d %H:%M:%S') + "] " + text + "\n"
		else:
			if len(self.text) > 0:
				self.text = "[" + datetime.now().strftime('%Y/%m/%d %H:%M:%S') + "] " + text
			else:
				self.text += text
'''
