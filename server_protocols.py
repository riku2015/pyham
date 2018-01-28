#!/usr/bin/python

import socket
from log import log

class ServerProtocol():
	def __init__(self, name, address, port):
		self.binded = False
		self.__name = name
		self.__address = "localhost"
		self.__port = port
		self.__protocolname = "NONE"
		self.__rooms = []

	def bind(self):
		log("Binding to port " + str(self.__port) + " using " + self.__protocolname + " protocol.")
		try:
			self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.socket.bind((socket.gethostname(), self.__port))
			self.socket.listen(5)
			self.binded = True
		except:
			self.binded = False
			log("Error: cannot bind socket.")

	def unbind(self):
		self.binded = False

	def isbinded(self):
		return self.binded

	#def connect(self):
	#	log("Incoming connection from --- to port ---.")

	def send(self, msg):
		log("Sending data.")
		totalsent = 0
		while totalsent < MSGLEN:
			sent = self.sock.send(msg[totalsent:])
			if sent == 0:
				log("Error: broken socket while sending.")
				#raise RuntimeError("Error: broken socket while sending.")
			totalsent = totalsent + sent

	def receive(self):
		chunks = []
		bytes_received = 0
		while bytes_recd < MSGLEN:
			chunk = self.sock.recv(min(MSGLEN - bytes_received, 2048))
			if chunk == '':
				log("Error: broken socket while receiving.")
				#raise RuntimeError("Error: broken socket while receiving.")
			chunks.append(chunk)
			bytes_received += len(chunk)
		return ''.join(chunks)

	def set_rooms(rooms):
		self.__rooms = rooms

	def get_rooms():
		return self.__rooms

# ProtocolPyhamp

class ServerProtocolPyhamp(ServerProtocol):
	def __init__(self, name, address, port):
		ServerProtocol.__init__(self, name, address, port)
		self.__protocolname = "PYHAMP"
		self.rooms = ["TESTROOM 1", "TESTROOM 2", "TESTROOM 3"]

	def connect(self):
		ServerProtocol.connect(self)

# ProtocolEqso
# Default port:
# 5000 ?

class ServerProtocolEqso(ServerProtocol):
	def __init__(self, name, address, port):
		ServerProtocol.__init__(self, name, address, port)
		self.__protocolname = "EQSO"

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
		self.__protocolname = "ECHOLINK"

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
		self.__protocolname = "FRN"
		self.__port = port

	def connect(self):
		ServerProtocol.connect(self)

	def disconnect(self):
		self.socket.send("\x03") #lahetetaan random kakkaa servulle.. ei vie tie millai disconectataan
		log("Disconnected.")

	def send(self, data):
		#self.socket.send(data)
		log("Sending data.")
