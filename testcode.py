#!/usr/bin/python

# This file contains temporary test code and unfinished classes and routines.
# It is not meant for testing the runtime environment itself.
# It should not be imported at all in a final release.

from log import log

#import pyaudio

'''
p = pyaudio.PyAudio()
for i in range(p.get_device_count()):
	print p.get_device_info_by_index(i)

WAVE_OUTPUT_FILENAME = "test.wav"
# Save to file:
#waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
#waveFile.setnchannels(CHANNELS)
#waveFile.setsampwidth(self.audio.get_sample_size(FORMAT))
#waveFile.setframerate(RATE)
#waveFile.writeframes(b''.join(frames))
#waveFile.close()

'''

class Test_Soundlooper:
	def __init__(self):
		self.__filename_sound = "music_gsm6.10_11025khz_mono_16b.wav"
		self.__buffer = None	# Store sound data here
		self.__index = 0		# Current position in buffer to be streamed from
		# Load sound file to buffer:
		# TODO

	def run(self):
		self.__index += 1

	def stream():
		# Send data to client
		pass
