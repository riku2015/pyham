#!/usr/bin/python

# pyham client program

# TODO:
# - Command line parameters
# - File recorder/player (.wav, .mp3 etc.)
# - Networking
# - Selection for input and output devices (Mic1, Mic2 etc.)
# - Space key as PTT button without character repeating loop
# - Translate to different languages / Loalization
# - Threading?
# - Status bar (with log display)
# - Separate GUI (mandatory?) to .py file(s)

programName = "Pyham Client"
programVersion = "0.005"
filename_log = "pyham_client.log"
filename_config = "pyham_client.conf"		# For saving presets etc.

from log import log
from client import Client

# Start client:
log("Program started.")

client = Client(filename_config)
client.Run()

# Terminate program:
log("Exit program.")
