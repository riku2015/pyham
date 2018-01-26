#!/usr/bin/python

# This file contains temporary test code and unfinished classes and routines.
# It is not meant for testing the runtime environment itself.
# It should not be imported at all in a final release.

import socket
from pyham import log

# ClientConnection
# This class is used within the client program

class ClientConnection:
	def __init__(self):
		pass

# ServerConnection
# This class is used within the server program

class ServerConnection:
	def __init__(self):
		pass

# ClientConnection_Eqso
# Network test code

class ClientConnection_Eqso:
	def __init__(self, address, port):
		self.address = address
		self.port = port
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	def connect(self):
		# The default port is 10024
		log("Connecting to server " + self.address + " at port " + str(self.port) + ".")
		#self.socket.connect((self.address, self.port))
		self.socket.connect(("frn.titanix.net", 10024))
		log("Connected.")
		# TODO: Send the whole thing at once (if works):
		self.socket.send("CT:")							# KIINTEE
		self.socket.send("<VX>2014003</VX>")			# KIINTEE
		self.socket.send("<EA>moimoi@moimoi.moi</EA>")	# Toistaseksi annetaan olla KIINTEE
		self.socket.send("<PW>asdfghjk</PW>")			# Toistaseksi kiintea
		self.socket.send("<ON>kokeilu</ON>")			# Kutsu tahan
		self.socket.send("<CL>2</CL>")					# KIINTEE TOISTASEKS
		self.socket.send("<BC>PC Only</BC>")			# KIINTEE toistaseks
		self.socket.send("<DS>description</DS>")		# Paikkakunta kommentti ym tama
		self.socket.send("<NN>Finland</NN>")			# KIINTEE TOISTASEKSI
		self.socket.send("<CT>test</CT>")				# kaupunki, #KIINTEE TOISTASEKSI 
		self.socket.send("<NT>Suomen EQSO</NT>")		# HUONE Aloitushuone tuo toistaseksi
		self.socket.send("\n")							# rivinvaihto viimeiseen muuten ei kuittaa sockki

		# odotetaan vastausta serverista, jos vastausta on enemman kun 1 merkki/bitti mika onkaa niin silloin lahettaa RX tilaan
		# Tama pitaisi korjata, ettkun serveri lahettaa OK niin se on ok..
		amount_received = 0
		amount_expected = 1

		while amount_received < amount_expected:
			data = self.socket.recv(16)
			amount_received += len(data)
			log('received "%s"' % data)
			self.socket.send("\RX0")

	def disconnect(self):
		self.socket.send("\x03") #lahetetaan random kakkaa servulle.. ei vie tie millai disconectataan
		log("Disconnected.")

	def send(self, data):
		self.socket.send(data)

# Scope
# Graphical scope from sound

class Scope:
	def __init__(self):
		pass

	def draw(self, sound_data):
		# Return pixel array in some sort of wxwidget
		pass

# Scope
# Graphical spectrum analyzer from sound

class Spectrum:
	def __init__(self):
		pass

	def draw(self, sound_data):
		# Return pixel array in some sort of wxwidget
		pass

# Spectrogram

# Soundlooper
# This test class loads a sound file into server and keeps it looping by cycling the index.
# If a client connects to the server, it should start streaming and playing from that particular index.
# The purpose of this test is to investigate how GSM header works in soundfile module.

class Soundlooper:
	def __init__(self):
		self.__filename_sound = "music_gsm6.10_11025_mono_16bit.wav"
		self.__buffer = None	# Store sound data here
		self.__index = 0		# Current position in buffer to be streamed from
		# Load sound file to buffer:
		# TODO

	def run(self):
		self.__index += 1

	def stream():
		# Send data to client
		pass
