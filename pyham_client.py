#!/usr/bin/python

# pyham client program

# Command line parameters:
# --help
# --configfile path/file.conf
# --logfile path/file.log

programName = "Pyham Client"
programVersion = "0.020"
filename_config = "pyham_client.conf"
filename_log = "pyham_client.log"

import sys
import argparse
from log import log
from client import Client

# Read command line parameters:
parser = argparse.ArgumentParser(description = programName + " " + programVersion)
parser.add_argument('-c', '--configfile', help='use this configuration file')
parser.add_argument('-l', '--logfile', help='log to this file')
parser.add_argument('-n', '--nogui', action='store_true', help='start without wxWidgets GUI')
parser.add_argument('-t', '--terminal', action='store_true', help='start with separate console window (when using GUI)')
parser.add_argument('-v', '--verbose', action='store_true', help='log more details')

args = parser.parse_args()
if args.configfile != None:
	filename_config = args.configfile
if args.logfile != None:
	filename_log = args.logfile

# Start client:
log("Program started.")

if args.nogui:
	client = Client(filename_config)
else:
	from client import ClientWx
	client = ClientWx(filename_config, args.terminal)

client.run()

# Terminate program:
log("Exit program.")
