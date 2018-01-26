#!/usr/bin/python

# pyham server program

# Command line parameters:
# config=path/file.conf

# TODO:
# - Separate (optional) GUI to .py file(s)

programName = "Pyham Server"
programVersion = "0.003"
filename_config = "pyham_server.conf"

from pyham import log
from server import Server

# Start server:
log("Program started.")
server = Server(filename_config)
server.Run()

# Terminate program:
log("Exit program.")
