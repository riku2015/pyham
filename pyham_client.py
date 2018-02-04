#!/usr/bin/python

# pyham client program

# Command line parameters:
# -config=path/file.conf
# -log=path/file.log

# TODO:
# - Space key as PTT button without character repeating loop
# - Translate to different languages / Loalization
# - Threading
# - Status bar (with log display)
# - Log command line parameters

programName = "Pyham Client"
programVersion = "0.008"
filename_config = "pyham_client.conf"
filename_log = "pyham_client.log"

import sys
import argparse
from log import log
from client import Client

# Read command line parameters:
parser = argparse.ArgumentParser(description = programName)
parser.add_argument('-c', '--configfile', help='Read this configuration file')
parser.add_argument('-l', '--logfile', help='Log to this file')
args = parser.parse_args()
if args.configfile != None:
	filename_config = args.configfile
if args.logfile != None:
	filename_log = args.logfile

# Start client:
log("Program started.")

client = Client(filename_config)
client.Run()

# Terminate program:
log("Exit program.")
