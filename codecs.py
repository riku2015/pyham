#!/usr/bin/python

# Routines for packing and unpacking audio data
# Note: This may require C(++)

class Soundformat():
	def __init__(self):
		#self.rate = 44100
		#self.bits = 16
		#self.channels = 1 # mono
		pass

class GSM(Soundformat):
	def __init__(self):
		pass

	def encode(self):
		# return packed audio data
		pass

	def decode(self):
		# return unpacked audio data
		pass

class WAV(Soundformat):
	def __init__(self):
		pass

#class FLAC(Soundformat):
#	def __init__(self):
#		pass
#
#	def encode(self):
#		# return packed audio data
#		pass
#
#	def decode(self):
#		# return unpacked audio data
#		pass

#class OGG(Soundformat):
#	def __init__(self):
#		pass
#
#	def encode(self):
#		# return packed audio data
#		pass
#
#	def decode(self):
#		# return unpacked audio data
#		pass

#class MP3(Soundformat):
#	def __init__(self):
#		pass
#
#	def encode(self):
#		# return packed audio data
#		pass
#
#	def decode(self):
#		# return unpacked audio data
#		pass