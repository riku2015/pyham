#!/usr/bin/python

import sys
import struct
import socket
import time
from datetime import datetime

def log(text):
	# TODO: Where to log: stdout, stderr, file...
	print >>sys.stderr, "[" + datetime.now().strftime('%Y/%m/%d %H:%M:%S') + "] " + text

#class Config():
#	def load():
#	def save():

class EqsoServerConnection:
	def __init__(self):
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	def connect(self, address, port):
		# The default port is 10024
		log("Connecting to server " + address + " at port " + str(port) + ".")
		self.socket.connect((address, port))
		#self.socket.connect("frn.titanix.net", 10024)
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

# TODO:
# - Protocol classes

# PYHAMP - pyham protocol
#
# Protocol for connecting HAM radios trough the Internet.
# Similar to eqso, echolink and frn.
#
# Description:
# Clients are connected to server.
# Client sends audio to the server, and the server sends that audio to other clients that are joined to the same room.
#
# Features:
# - Audio
# - Callsign
# - Description
# - Room

