#!/usr/bin/python

import sys
import struct
import socket
import time
from datetime import datetime

# TODO:
# - Keep client and server sources in separate files so that they can be distributed independently

def log(text):
	# TODO:
	# - Stash multiple log messages into same timestamp entry
	# - Logging options: stdout, stderr, file...

	print >>sys.stderr, "[" + datetime.now().strftime('%Y/%m/%d %H:%M:%S') + "] " + text

class Config():
	def __init__(self):
		pass

	def load(self, filename):
		log("Loading config file '" + filename + "'.")
		# Return or set values in variables

	def save(self):
		log("Saving config file '" + filename + "'.")

# Protocols
# Clients are connected to server.
# Client sends audio to the server, and the server sends that audio to other clients that are joined to the same room.

# ProtocolPyhamp
# Features:
# - Audio
# - Callsign
# - Description
# - Rooms

class ProtocolPyhamp:
	def __init__(self, port):
		self.__port = port
		pass

# ProtocolEqso
# Features:
# - Audio
# - Callsign
# - Description
# - Rooms

class ProtocolEqso:
	def __init__(self, port):
		self.__port = port
		pass

# ProtocolEcholink
# Features:
# - Audio
# - Callsign
# - Description
# - Rooms

class ProtocolEcholink:
	def __init__(self, port):
		self.__port = port
		pass

# ProtocolFrn
# Features:
# - Audio
# - Callsign
# - Description
# - Rooms

class ProtocolFrn:
	def __init__(self, port):
		self.__port = port
		pass
