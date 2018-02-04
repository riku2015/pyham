#!/usr/bin/python

import socket
from log import log

class ServerProtocol():
	def __init__(self, name, address, port):
		self.binded = False
		self.name = name
		self.address = "localhost"
		self.port = port
		self.protocolname = "NONE"
		self.rooms = []

	def __bind(self):
		log("Binding to port " + str(self.port) + " using " + self.protocolname + " protocol...")
		try:
			self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.socket.bind((socket.gethostname(), self.port))
			self.socket.listen(2)
			#self.accept()
			self.binded = True
		except Exception, e:
			self.binded = False
			log("Error while binding socket: " + str(e))
		return self.binded

	def __unbind(self):
		# TODO
		self.binded = False

	#def connect(self):
	#	log("Incoming connection from --- to port ---.")

	def send(self, data):
		log("Sending data.")
		totalsent = 0
		while totalsent < MSGLEN:
			sent = self.sock.send(data[totalsent:])
			if sent == 0:
				log("Error while sending trough socket: " + str(e))
				#raise RuntimeError("Error: broken socket while sending.")
			totalsent = totalsent + sent

	def receive(self):
		chunks = []
		bytes_received = 0
		while bytes_recd < MSGLEN:
			chunk = self.sock.recv(min(MSGLEN - bytes_received, 2048))
			if chunk == '':
				log("Error while receiving via socket: " + str(e))
				#raise RuntimeError("Error: broken socket while receiving.")
			chunks.append(chunk)
			bytes_received += len(chunk)
		return ''.join(chunks)

	def run(self):
		if self.__bind():
			log("Accepting connections.")
		#while True:
			# Accept connections from outside
			#(clientsocket, address) = self.socket.accept()
			#self.socket.accept()
			#log("Incoming client connection.")

			# Make thread for connection:
			# ct = client_thread(clientsocket)
			# ct.run()

	def set_rooms(rooms):
		self.rooms = rooms

	def get_rooms():
		return self.rooms

# ProtocolPyhamp
# Default port:
# 1000 ?

class ServerProtocolPyhamp(ServerProtocol):
	def __init__(self, name, address, port):
		ServerProtocol.__init__(self, name, address, port)
		self.protocolname = "PYHAMP"
		self.rooms = ["TESTROOM 1", "TESTROOM 2", "TESTROOM 3"]

	def connect(self):
		ServerProtocol.connect(self)

# ProtocolEqso
# Default port:
# 5000 ?

class ServerProtocolEqso(ServerProtocol):
	def __init__(self, name, address, port):
		ServerProtocol.__init__(self, name, address, port)
		self.protocolname = "EQSO"

	def connect(self):
		ServerProtocol.connect(self)

	def send(self):
		log("Sending data.")

# ProtocolEcholink
# Default ports:
# 5198 UDP EchoLink VoIP Amateur Radio Software (Voice)
# 5199 UDP EchoLink VoIP Amateur Radio Software (Voice)
# 5200 TCP EchoLink VoIP Amateur Radio Software (Information)

class ServerProtocolEcholink(ServerProtocol):
	def __init__(self, name, address, port):
		ServerProtocol.__init__(self, name, address, port)
		self.protocolname = "ECHOLINK"

	def connect(self):
		ServerProtocol.connect(self)

	def send(self):
		log("Sending data.")

# ProtocolFrn
# http://freeradionetwork.eu/frnprotocol.htm
# Default port:
# 10024 ?

class ServerProtocolFrn(ServerProtocol):
	def __init__(self, name, address, port):
		ServerProtocol.__init__(self, name, address, port)
		self.protocolname = "FRN"

	def connect(self):
		ServerProtocol.connect(self)

	def disconnect(self):
		self.socket.send("\x03") #lahetetaan random kakkaa servulle.. ei vie tie millai disconectataan
		log("Disconnected.")

	def send(self, data):
		#self.socket.send(data)
		log("Sending data.")

