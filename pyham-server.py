#!/usr/bin/python

# pyham server program

programName = "pyham server"
programVersion = "0.001"

#import sys
from pyham import log

filename_settings = "pyham-server.conf"

def config_read():
	log("Loading config file.")
	# TODO: return or set values in variables

# Defaults if not given in config
server_name = "mypyhamserver"
server_port = 5000

log("Server started.")
config_read()
log("Binding to port " + str(server_port) + " as " + server_name + ".")
log("Server stopped.")

# TODO:
# - Stash multiple log messages into same timestamp entry
# - Protocol selection
