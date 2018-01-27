#!/usr/bin/python

import sys
import time
from datetime import datetime
#import struct

def log(text, filename = None):
	# TODO:
	# - Stash multiple log messages into same timestamp entry
	# - Logging options: stdout, stderr, file, window...

	# Format text with timestamp:
	string = "[" + datetime.now().strftime('%Y/%m/%d %H:%M:%S') + "] " + text

	# Print to console:
	print >>sys.stderr, string

	# Append to file:
	if filename is not None:
		with open(filename, "a") as logfile:
			logfile.write(string + "\n")
