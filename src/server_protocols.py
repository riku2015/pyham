#!/usr/bin/python

import socket
from log import log

class ServerProtocol():
	def __init__(self, name, port):
		self.__binded = False
		self.name = name
		self.port = port
		self.protocolname = "NONE"
		self.__rooms = []
		self.__sentbytes = 0
		self.__receivedbytes = 0
		self.__errors = 0

	def is_binded(self):
		return self.__binded

	def bind(self):
		log("Binding to port " + self.port + " as '" + self.name + "' using " + self.protocolname + "...")
		try:
			self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.__socket.bind((socket.gethostname(), int(self.port)))
			self.__socket.listen(1)
			#self.accept()
			self.__binded = True
		except Exception as e:
			self.__binded = False
			log("Error while binding socket: " + str(e))
		return self.__binded

	def unbind(self):
		# TODO
		self.__binded = False
		# TODO: disconect all
		#self.disconnect()

	def connect(self):
		log(self.name + ": Incoming connection from --- to port ---.")
		self.send(b"<C>")

	def disconnect(self):
		self.__socket.shutdown()
		self.__socket.close()
		log(self.name + ": Disconnected.")

	def stop(self):
		log("Stopping " + self.name)
		self.disconnect()

	def send(self, data):
		log("Sending data.")
		totalsent = 0
		while totalsent < MSGLEN:
			sent = self.__socket.send(data[totalsent:])
			if sent == 0:
				error(self, "while sending trough socket: " + str(e))
				#raise Runtimeerror(self, "Error: broken socket while sending.")
			totalsent = totalsent + sent
		self.__sentbytes += totalsent

	def receive(self):
		chunks = []
		bytes_received = 0
		while bytes_recd < MSGLEN:
			chunk = self.__socket.recv(min(MSGLEN - bytes_received, 2048))
			if chunk == b'':
				error(self, "while receiving via socket: " + str(e))
				#raise Runtimeerror(self, "Error: broken socket while receiving.")
			chunks.append(chunk)
			bytes_received += len(chunk)
		self.__receivedbytes += bytes_received
		return b''.join(chunks)

	def run(self):
		if self.bind():
			log(self.name + ": Accepting connections.")
			self.__running = True
		while True:
			# Accept connections from outside
			(clientsocket, address) = self.__socket.accept()
			#self.__socket.accept()
			log("Incoming client connection.")

			# Make thread for connection:
			ct = client_thread(clientsocket)
			ct.run()
		return self.__running

	def set_rooms(rooms):
		self.__rooms = rooms

	def get_rooms():
		return self.__rooms

# ProtocolPyham

class ServerProtocolPyham(ServerProtocol):
	def __init__(self, name, port):
		ServerProtocol.__init__(self, name, port)
		self.protocolname = "PYHAM"
		self.__version = "0.05"
		self.__rooms = ["TESTROOM 1", "TESTROOM 2", "TESTROOM 3"]

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
		self.send("\x03") #lahetetaan random kakkaa servulle.. ei vie tie millai disconectataan
		log("Disconnected.")

# ProtocolEcholink

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
