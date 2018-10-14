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
		self.socket.connect((self.address, self.port))	# NOTE: Port as integer, not string
		log(self.protocolname + ": Connected to " + self.address + " at port " + str(self.port) + ".")

	def disconnect(self):
		#self.socket.shutdown()
		self.socket.close()

	def send(self, data):
		self.socket.send(data)
		# log("Error: cannot send trough socket.")

	def receive(self):
		pass

# ProtocolPyham
# commands:
# <GR> get rooms
# <JR>roomname</JR> join room
# <D> disconnect
# <GV> get server version
# <SV>version</SV> send client version
# <SC>callsign</SC> send callsign
# <SD>description</SD> send description
# <SA> send audio
# <GA> get audio

class ClientProtocolPyham(ClientProtocol):
	def __init__(self, address, port):
		ClientProtocol.__init__(self, address, port)
		self.protocolname = "PYHAM"
		self.version = "0.05"

	def send_audio(data):
		self.send(b"<SA>")

	def get_audio(self):
		self.send(b"<GA>")

	def get_rooms(self):
		self.send(b"<GR>")
		self.receive()
		return []

	def join_room(self, room):
		self.send(b"<JR>" + room + "</JR>()")

	def connect(self):
		ClientProtocol.connect(self)
		self.send(b"<INIT>1234567890")	# NOTE: Port as integer, not string
		amount_received = 0
		amount_expected = 16
		while amount_received < amount_expected:
			data = self.socket.recv(1)
			#data = self.socket.recv(1)
			amount_received += len(data)
			log('received "%s"' % data)
		log("DEBUG: Chunk read.")
		self.disconnect()

	def disconnect(self):
		self.send(b"<d>")
		ClientProtocol.disconnect(self)

	def get_version(self):
		self.send(b"<gv>")
		# return version

	def send_version(self):
		self.send(b"<sv>" + self.version + "</sv>")

# ProtocolEqso

class ClientProtocolEqso(ClientProtocol):
	def __init__(self, address, port):
		ClientProtocol.__init__(self, address, port)
		self.protocolname = "EQSO"

	def send(self, data):
		#self.socket.send(data)

		# TODO: Send the whole thing at once (if works):
		self.socket.send(b"CT:")						# KIINTEE
		self.socket.send(b"<VX>2014003</VX>")			# KIINTEE
		self.socket.send(b"<EA>joku@ei.ole</EA>")		# Toistaseksi annetaan olla KIINTEE
		self.socket.send(b"<PW>jotain</PW>")			# Toistaseksi kiintea
		self.socket.send(b"<ON>Pyham</ON>")				# Kutsu tahan
		self.socket.send(b"<CL>2</CL>")					# KIINTEE TOISTASEKS
		self.socket.send(b"<BC>PC Only</BC>")			# KIINTEE toistaseks
		self.socket.send(b"<DS>Pyham Cient Test</DS>")	# Paikkakunta kommentti ym tama
		self.socket.send(b"<NN>Finland</NN>")			# KIINTEE TOISTASEKSI
		self.socket.send(b"<CT>test</CT>")				# kaupunki, #KIINTEE TOISTASEKSI 
		#self.socket.send(b"<NT>Suomen EQSO</NT>")		# HUONE Aloitushuone tuo toistaseksi
		self.socket.send(b"<NT>FINLAND</NT>")			# HUONE Aloitushuone tuo toistaseksi
		self.socket.send(b"\n")							# rivinvaihto viimeiseen muuten ei kuittaa sockki
		# odotetaan vastausta serverista, jos vastausta on enemman kun 1 merkki/bitti mika onkaa niin silloin lahettaa RX tilaan
		# Tama pitaisi korjata, ettkun serveri lahettaa OK niin se on ok..
		amount_received = 0
		amount_expected = 1

		while amount_received < amount_expected:
			data = self.socket.recv(256)
			#data = self.socket.recv(1)
			amount_received += len(data)
			log('received "%s"' % data)
			self.socket.send(b"\RX0")

	def send_audio(data):
		pass

	def get_audio(self):
		return None

	def get_rooms(self):
		return []

	def join_room(room):
		pass

	def connect(self):
		ClientProtocol.connect(self)

	def disconnect(self):
		ClientProtocol.disconnect(self)

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

	def connect(self):
		ClientProtocol.connect(self)

	def connect(self):
		ClientProtocol.connect(self)

	def disconnect(self):
		pass

	def get_version(self):
		pass

	def send_version(self):
		pass

# ProtocolFrn
# http://freeradionetwork.eu/frnprotocol.htm

class ClientProtocolFrn(ClientProtocol):
	def __init__(self, address, port):
		ClientProtocol.__init__(self, address, port)
		self.protocolname = "FRN"

	def connect(self):
		ClientProtocol.connect(self)

	def disconnect(self):
		self.socket.send(b"\x03") #lahetetaan random kakkaa servulle.. ei vie tie millai disconectataan
		ClientProtocol.disconnect(self)

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

# from testcode import ClientProtocolTest