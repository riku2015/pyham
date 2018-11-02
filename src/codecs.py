#!/usr/bin/python

# Routines for packing and unpacking audio data
# Note: This may require C(++)

class Soundformat():
	def __init__(self, rate=0, bits=0, channels=0):
		self.rate = rate
		self.bits = bits
		self.channels = channels	# 1 = mono, 2 = stereo

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