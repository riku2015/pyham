#!/usr/bin/python

# pyham server program

# Command line parameters:
# --help
# --configfile path/file.conf
# --log path/file.log
# --nogui

programName = "Pyham Server"
programVersion = "0.018"
filename_config = "../conf/pyham_server.conf"
filename_log = "pyham_server.log"

import sys
import argparse
from log import log
from server import Server

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

# Start server:
log("Program started.")

if args.nogui:
	server = Server(filename_config)
else:
	from server import ServerWx
	server = ServerWx(filename_config, args.terminal)

server.run()

# Terminate program:
log("Exit program.")
