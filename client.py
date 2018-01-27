#!/usr/bin/python

import wx

from log import log
#from pyham import ProtocolPyhamp, ProtocolEqso, ProtocolEcholink, ProtocolFrn
from client_gui import Mainwindow
from client_gui import Settingswindow

# ClientConnection
# This class is used within the client program

class ClientConnection:
	def __init__(self):
		pass

class ClientProtocol:
	def __init__(self, port):
		self.__port = port

# ProtocolPyhamp

class ClientProtocolPyhamp(ClientProtocol):
	def __init__(self, port):
		#super().__init__(port)
		pass

	def connect(self):
		pass

	def send(self):
		pass

# ProtocolEqso

class ClientProtocolEqso(ClientProtocol):
	def __init__(self, port):
		#super().__init__(port)
		pass

	def connect(self):
		pass

	def send(self):
		pass

# ProtocolEcholink

class ClientProtocolEcholink(ClientProtocol):
	def __init__(self, port):
		#super().__init__(port)
		pass

	def connect(self):
		pass

	def send(self):
		pass

# ProtocolFrn
# http://freeradionetwork.eu/frnprotocol.htm
# Default port: 10024

class ClientProtocolFrn(ClientProtocol):
	#def __init__(self, address, port):
	#	self.address = address
	#	self.port = port

	def __init__(self):
		#super().__init__()
		self.address = "frn.titanix.net"
		self.port = 10024
		self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	def connect(self):
		log("Connecting to server " + self.address + " at port " + str(self.port) + ".")
		#self.socket.connect((self.address, self.port))
		self.socket.connect(("frn.titanix.net", 10024))
		log("Connected.")

	def disconnect(self):
		self.__socket.send("\x03") #lahetetaan random kakkaa servulle.. ei vie tie millai disconectataan
		log("Disconnected.")

	def send(self, data):
		#self.__socket.send(data)

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

class Client:
	def __init__(self, filename_config):
		# Defaults if not given in config file:
		self.server_name = "frn.titanix.net"
		self.server_port = 10024
		self.server_protocol = "frn"

		# Create wxwidgets application:
		#self.app = wx.App(self)
		self.app = wx.App(None)
		self.mainwindow = Mainwindow(parent=None)

	def Run(self):
		log("Starting graphical client.")
		# Show main window:
		#self.settingswindow.Show()
		self.mainwindow.Show()
		# Execute GUI:
		self.app.MainLoop()

	def connect(self):
		pass
