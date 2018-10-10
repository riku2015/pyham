#!/usr/bin/python

import socket
from log import log

class ServerProtocol():
	def __init__(self, name, port):
		self.binded = False
		self.name = name
		self.port = port
		self.protocolname = "NONE"
		self.rooms = []

	def bind(self):
		log("Binding to port " + self.port + " as '" + self.name + "' using " + self.protocolname + "...")
		try:
			self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.socket.bind((socket.gethostname(), int(self.port)))
			self.socket.listen(1)
			#self.accept()
			self.binded = True
		except Exception as e:
			self.binded = False
			log("Error while binding socket: " + str(e))
		return self.binded

	def unbind(self):
		# TODO
		self.binded = False
		# TODO: disconect all
		#self.disconnect()

	def connect(self):
		log(self.name + ": Incoming connection from --- to port ---.")

	def disconnect(self):
		log(self.name + ": Disconnected.")
		
	def send(self, data):
		log("Sending data.")
		totalsent = 0
		while totalsent < MSGLEN:
			sent = self.sock.send(data[totalsent:])
			if sent == 0:
				error(self, "while sending trough socket: " + str(e))
				#raise Runtimeerror(self, "Error: broken socket while sending.")
			totalsent = totalsent + sent

	def receive(self):
		chunks = []
		bytes_received = 0
		while bytes_recd < MSGLEN:
			chunk = self.sock.recv(min(MSGLEN - bytes_received, 2048))
			if chunk == '':
				error(self, "while receiving via socket: " + str(e))
				#raise Runtimeerror(self, "Error: broken socket while receiving.")
			chunks.append(chunk)
			bytes_received += len(chunk)
		return ''.join(chunks)

	def run(self):
		result = False
		if self.bind():
			log(self.name + ": Accepting connections.")
			result = True
		#while True:
			# Accept connections from outside
			#(clientsocket, address) = self.socket.accept()
			#self.socket.accept()
			#log("Incoming client connection.")

			# Make thread for connection:
			# ct = client_thread(clientsocket)
			# ct.run()
		return result

	def set_rooms(rooms):
		self.rooms = rooms

	def get_rooms():
		return self.rooms

# ProtocolPyham
# Default port:
# ?

class ServerProtocolPyham(ServerProtocol):
	def __init__(self, name, port):
		ServerProtocol.__init__(self, name, port)
		self.protocolname = "PYHAM"
		self.rooms = ["TESTROOM 1", "TESTROOM 2", "TESTROOM 3"]

	def connect(self):
		#ServerProtocol.connect(self)
		pass

	def send_rooms(self):
		pass

	def send_version(self):
		pass

	def send_audio(self):
		pass

	def get_audio(self):
		pass

# ProtocolEqso
# Default port:
# 5000 ?

class ServerProtocolEqso(ServerProtocol):
	def __init__(self, name, port):
		ServerProtocol.__init__(self, name, port)
		self.protocolname = "EQSO"

	def connect(self):
		#ServerProtocol.connect(self)
		pass

	def send(self):
		log("Sending data.")

	def disconnect(self):
		self.socket.send("\x03") #lahetetaan random kakkaa servulle.. ei vie tie millai disconectataan
		log("Disconnected.")

# ProtocolEcholink
# Default ports:
# 5198 UDP EchoLink VoIP Amateur Radio Software (Voice)
# 5199 UDP EchoLink VoIP Amateur Radio Software (Voice)
# 5200 TCP EchoLink VoIP Amateur Radio Software (Information)

class ServerProtocolEcholink(ServerProtocol):
	def __init__(self, name, port):
		ServerProtocol.__init__(self, name, port)
		self.protocolname = "ECHOLINK"

	def connect(self):
		#ServerProtocol.connect(self)
		pass

	def send(self):
		log("Sending data.")

# ProtocolFrn
# http://freeradionetwork.eu/frnprotocol.htm
# Default port:
# 10024 ?

class ServerProtocolFrn(ServerProtocol):
	def __init__(self, name, port):
		ServerProtocol.__init__(self, name, port)
		self.protocolname = "FRN"

	def connect(self):
		#ServerProtocol.connect(self)
		pass

	def send(self, data):
		#self.socket.send(data)
		log("Sending data.")

# from testcode import ServerProtocolTest