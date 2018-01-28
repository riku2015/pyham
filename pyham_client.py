#!/usr/bin/python

# pyham client program

# Command line parameters:
# -config=path/file.conf
# -log=path/file.log

# TODO:
# - Space key as PTT button without character repeating loop
# - Translate to different languages / Loalization
# - Threading?
# - Status bar (with log display)

programName = "Pyham Client"
programVersion = "0.006"
filename_config = "pyham_client.conf"
filename_log = "pyham_client.log"

import sys
from log import log
from client import Client

# Read command line parameters:
if len(sys.argv) >= 2 and len(sys.argv[1]) >= 3:		# At least >=1 characters for parameter name, 1 for '=', and >=1 characters for value
	pair = sys.argv[1].split('=')
	if len(pair) == 2 and len(pair[0]) > 0 and len(pair[1]) > 0:
		parameter = pair[0].strip()
		value = pair[1].strip()
		if parameter == "-config":
			filename_config = value

# Start client:
log("Program started.")

client = Client(filename_config)
client.Run()

# Terminate program:
log("Exit program.")
