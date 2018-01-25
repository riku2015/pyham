#!/usr/bin/python

# pyham client program

# TODO:
# - File recorder/player (.wav, .mp3 etc.)
# - Networking
# - Selection for input and output devices (Mic1, Mic2 etc.)
# - Space key as PTT button without character repeating loop
# - Translate to different languages / Loalization
# - Threading?
# - Status bar (with log display)
# - Separate GUI (mandatory?) to .py file(s)

programName = "Pyham Client"
programVersion = "0.002"
filename_config = "pyham_client.conf"		# For saving presets etc.

from pyham import log
from client import Client

# Start client:
log("Starting client.")
client = Client(filename_config)

# Terminate program:
log("Exit program.")
