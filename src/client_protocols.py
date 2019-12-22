#!/usr/bin/python

import socket
from log import log

class ClientProtocol:
	def __init__(self, address, port):
		self.protocolname = "NONE"
		self.address = address
		self.port = port
		self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.__receivedbytes = 0
		self.__errors = 0
		self.__running = False

	def connect(self):
		self.__socket.connect((self.address, self.port))	# NOTE: Port as integer, not string
		log(self.protocolname + ": Connected to " + self.address + " at port " + str(self.port) + ".")

	def disconnect(self):
		#self.socket.shutdown()
		self.__socket.close()

	def send(self, data):
		self.__socket.send(data)
		# log("Error: cannot send trough socket.")

	def receive(self, length):
		# length as amount of bytes
		return self.__socket.recv(length)

# ProtocolPyham

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
		self.send(b"<C>")
		amount_received = 0
		amount_expected = 16
		while amount_received < amount_expected:
			data = self.__socket.recv(1)
			#data = self.socket.recv(1)
			amount_received += len(data)
			log('received "%s"' % data)
		log("DEBUG: Chunk read.")
		self.disconnect()

	def disconnect(self):
		self.send(b"<DC>")
		ClientProtocol.disconnect(self)

	def get_version(self):
		self.send(b"<GV>")
		# return version

	def send_version(self):
		self.send(b"<SV>" + self.version + "</SV>")

# ProtocolEqso

class ClientProtocolEqso(ClientProtocol):
	def __init__(self, address, port):
		ClientProtocol.__init__(self, address, port)
		self.protocolname = "EQSO"

	def send(self, data):
		#self.__socket.send(data)

		# TODO: Send the whole thing at once (if works):
		self.send(b"CT:")							# KIINTEE
		self.send(b"<VX>2014003</VX>")				# KIINTEE
		self.send(b"<EA>joku@ei.ole</EA>")			# Toistaseksi annetaan olla KIINTEE
		self.send(b"<PW>jotain</PW>")				# Toistaseksi kiintea
		self.send(b"<ON>Pyham</ON>")				# Kutsu tahan
		self.send(b"<CL>2</CL>")					# KIINTEE TOISTASEKS
		self.send(b"<BC>PC Only</BC>")				# KIINTEE toistaseks
		self.send(b"<DS>Pyham Cient Test</DS>")	# Paikkakunta kommentti ym tama
		self.send(b"<NN>Finland</NN>")				# KIINTEE TOISTASEKSI
		self.send(b"<CT>test</CT>")				# kaupunki, #KIINTEE TOISTASEKSI 
		#self.__socket.send(b"<NT>Suomen EQSO</NT>")		# HUONE Aloitushuone tuo toistaseksi
		self.send(b"<NT>FINLAND</NT>")				# HUONE Aloitushuone tuo toistaseksi
		self.send(b"\n")							# rivinvaihto viimeiseen muuten ei kuittaa sockki
		# odotetaan vastausta serverista, jos vastausta on enemman kun 1 merkki/bitti mika onkaa niin silloin lahettaa RX tilaan
		# Tama pitaisi korjata, ettkun serveri lahettaa OK niin se on ok..
		amount_received = 0
		amount_expected = 1

		while amount_received < amount_expected:
			data = self.receive(256)
			#data = self.socket.recv(1)
			amount_received += len(data)
			log('received "%s"' % data)
			self.send(b"\RX0")

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

class ClientProtocolFrn(ClientProtocol):
	def __init__(self, address, port):
		ClientProtocol.__init__(self, address, port)
		self.protocolname = "FRN"

	def connect(self):
		ClientProtocol.connect(self)

	def disconnect(self):
		self.send(b"\x03") #lahetetaan random kakkaa servulle.. ei vie tie millai disconectataan
		ClientProtocol.disconnect(self)

	def send(self, data):
		#self.__socket.send(data)

		# TODO: Send the whole thing at once (if works):
		self.send(b"CT:")							# KIINTEE
		self.send(b"<VX>2014003</VX>")				# KIINTEE
		self.send(b"<EA>joku@ei.ole</EA>")			# Toistaseksi annetaan olla KIINTEE
		self.send(b"<PW>jotain</PW>")				# Toistaseksi kiintea
		self.send(b"<ON>Pyham</ON>")				# Kutsu tahan
		self.send(b"<CL>2</CL>")					# KIINTEE TOISTASEKS
		self.send(b"<BC>PC Only</BC>")				# KIINTEE toistaseks
		self.send(b"<DS>Pyham Cient Test</DS>")	# Paikkakunta kommentti ym tama
		self.send(b"<NN>Finland</NN>")				# KIINTEE TOISTASEKSI
		self.send(b"<CT>test</CT>")				# kaupunki, #KIINTEE TOISTASEKSI 
		#self.__socket.send(b"<NT>Suomen EQSO</NT>")		# HUONE Aloitushuone tuo toistaseksi
		self.send(b"<NT>FINLAND</NT>")				# HUONE Aloitushuone tuo toistaseksi
		self.send(b"\n")							# rivinvaihto viimeiseen muuten ei kuittaa sockki
		# odotetaan vastausta serverista, jos vastausta on enemman kun 1 merkki/bitti mika onkaa niin silloin lahettaa RX tilaan
		# Tama pitaisi korjata, ettkun serveri lahettaa OK niin se on ok..
		amount_received = 0
		amount_expected = 1
		
		while amount_received < amount_expected:
			data = self.receive(256)
			#data = self.socket.recv(1)
			amount_received += len(data)
			log('received "%s"' % data)
			self.send(b"\RX0")

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
