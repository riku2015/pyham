#!/usr/bin/python

# pyham server program

# TODO:
# - Separate (optional) GUI to .py file(s)

programName = "Pyham Server"
programVersion = "0.002"
filename_config = "pyham_server.conf"

from pyham import log
from server import Server

# Start server:
log("Starting server.")
server = Server(filename_config)

# Terminate program:
log("Exit program.")
