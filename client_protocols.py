#!/usr/bin/python

import socket
from log import log

class ClientProtocol:
	def __init__(self, address, port):
		self.protocolname = "NONE"
		self.address = address
		self.port = port
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	def connect(self):
		self.socket.connect((self.address, self.port))

	def send(self, data):
		self.socket.send(data)
		# log("Error: cannot send trough socket.")

	def receive(self):
		return ""

# ProtocolPyhamp
# commands:
# <gr> get rooms
# <j roomname> join room
# <d> disconnect
# <v> get server version
# <v string> send client version
# <c callsign> send callsign
# <d description> send description

class ClientProtocolPyhamp(ClientProtocol):
	def __init__(self, address, port):
		ClientProtocol.__init__(self, address, port)
		self.protocolname = "PYHAMP"
		self.version = "0.05"

	def send_audio(data):
		pass

	def get_audio():
		return None

	def get_rooms(self):
		self.send(b"<gr>")
		self.receive()
		return []

	def join_room(self, room):
		self.send(b"<j " + room + ">()")

	def disconnect(self):
		pass

	def get_version(self):
		pass

	def send_version(self):
		pass

# ProtocolEqso

class ClientProtocolEqso(ClientProtocol):
	def __init__(self, address, port):
		ClientProtocol.__init__(self, address, port)
		self.protocolname = "EQSO"

	def send(self, data):
		#self.socket.send(data)

		# TODO: Send the whole thing at once (if works):
		self.socket.send(b"CT:")							# KIINTEE
		self.socket.send(b"<VX>2014003</VX>")			# KIINTEE
		self.socket.send(b"<EA>moimoi@moimoi.moi</EA>")	# Toistaseksi annetaan olla KIINTEE
		self.socket.send(b"<PW>asdfghjk</PW>")			# Toistaseksi kiintea
		self.socket.send(b"<ON>kokeilu</ON>")			# Kutsu tahan
		self.socket.send(b"<CL>2</CL>")					# KIINTEE TOISTASEKS
		self.socket.send(b"<BC>PC Only</BC>")			# KIINTEE toistaseks
		self.socket.send(b"<DS>Pyham Cient " + programVersion.encode('utf-8') + b" test</DS>")	# Paikkakunta kommentti ym tama
		self.socket.send(b"<NN>Finland</NN>")			# KIINTEE TOISTASEKSI
		self.socket.send(b"<CT>test</CT>")				# kaupunki, #KIINTEE TOISTASEKSI 
		self.socket.send(b"<NT>Suomen EQSO</NT>")		# HUONE Aloitushuone tuo toistaseksi
		self.socket.send(b"\n")							# rivinvaihto viimeiseen muuten ei kuittaa sockki
		# odotetaan vastausta serverista, jos vastausta on enemman kun 1 merkki/bitti mika onkaa niin silloin lahettaa RX tilaan
		# Tama pitaisi korjata, ettkun serveri lahettaa OK niin se on ok..
		amount_received = 0
		amount_expected = 1

		while amount_received < amount_expected:
			data = self.socket.recv(256)
			amount_received += len(data)
			log('received "%s"' % data)
			self.socket.send(b"\RX0")

	def send_audio(data):
		pass

	def get_audio():
		return None

	def get_rooms():
		return []

	def join_room(room):
		pass

	def disconnect(self):
		pass

	def get_version(self):
		pass

	def send_version(self):
		pass

# ProtocolEcholink

class ClientProtocolEcholink(ClientProtocol):
	def __init__(self, address, port):
		self.protocolname = "ECHOLINK"
		ClientProtocol.__init__(self, address, port)

	def send_audio(data):
		pass

	def get_audio():
		return None

	def get_rooms():
		return []

	def join_room(room):
		pass

	def disconnect(self):
		pass

	def get_version(self):
		pass

	def send_version(self):
		pass

# ProtocolFrn
# http://freeradionetwork.eu/frnprotocol.htm

programVersion = "0.010"	# FIXME: duplicate definition here

class ClientProtocolFrn(ClientProtocol):
	def __init__(self, address, port):
		ClientProtocol.__init__(self, address, port)

	def connect(self):
		log("Connecting to server " + self.address + " at port " + str(self.port) + " using FRN protocol...")
		self.socket.connect((self.address, self.port))
		log("Connected.")

	def disconnect(self):
		self.socket.send(b"\x03") #lahetetaan random kakkaa servulle.. ei vie tie millai disconectataan
		log("Disconnected.")

	def send(self, data):
		pass

	def send_audio(data):
		pass

	def get_audio():
		return None

	def get_rooms():
		return []

	def join_room(room):
		pass

	def get_version(self):
		pass

	def send_version(self):
		pass
