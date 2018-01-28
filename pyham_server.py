#!/usr/bin/python

# pyham server program

# Command line parameters:
# -config=path/file.conf
# -log=path/file.log

# TODO:
# - Optional) GUI
# - Threading?
# - Translate to different languages / Loalization

programName = "Pyham Server"
programVersion = "0.004"
filename_config = "pyham_server.conf"
filename_log = "pyham_server.log"

import sys
from log import log
from server import Server

# Read command line parameters:
if len(sys.argv) >= 2 and len(sys.argv[1]) >= 3:		# At least >=1 characters for parameter name, 1 for '=', and >=1 characters for value
	pair = sys.argv[1].split('=')
	if len(pair) == 2 and len(pair[0]) > 0 and len(pair[1]) > 0:
		parameter = pair[0].strip()
		value = pair[1].strip()
		if parameter == "-config":
			filename_config = value

# Start server:
log("Program started.")
server = Server(filename_config)
server.Run()

# Terminate program:
log("Exit program.")
