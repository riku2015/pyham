#!/usr/bin/python

# This file contains temporary test code and unfinished classes and routines.
# It is not meant for testing the runtime environment itself.
# It should not be included at all in a final release.

from log import log

#import pyaudio

class Test_Soundlooper:
	def __init__(self):
		self.__filename_sound = "music_gsm6.10_11025khz_mono_16b.wav"
		self.__buffer = None	# Store sound data here
		self.__index = 0		# Current position in buffer to be streamed from
		self.__playing = False
		self.streaming = False
		# Load sound file to buffer:
		# TODO

	def run(self):
		self.__index += 1
		self.stream()

	def stop(self):
		pass

	def stream(self):
		# Send data to client
		pass

	def reset(self):
		self.__index = 0
