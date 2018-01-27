#!/usr/bin/python

# This file contains temporary test code and unfinished classes and routines.
# It is not meant for testing the runtime environment itself.
# It should not be imported at all in a final release.

from log import log

# For each incoming connection, create new ServerConnection

import pyaudio
import wave

'''
p = pyaudio.PyAudio()
for i in range(p.get_device_count()):
	print p.get_device_info_by_index(i)
'''

def get_devices():
	p = pyaudio.PyAudio()
	info = p.get_host_api_info_by_index(0)
	numdevices = info.get('deviceCount')
	result = ""
	for i in range(0, numdevices):
			if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
				result += "Input Device id " + str(i) + " - " + p.get_device_info_by_host_api_device_index(0, i).get('name')
	return result

class Test_Audiorecorder:
	def __init__(self):
		self.audio = pyaudio.PyAudio()

	def rec(self):
		FORMAT = pyaudio.paInt16
		CHANNELS = 2
		RATE = 44100
		CHUNK = 1024
		RECORD_SECONDS = 5
		WAVE_OUTPUT_FILENAME = "test.wav"

		# Start recording
		stream = self.audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
		log("TEST: Recording for 5 seconds...")
		frames = []

		for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
			data = stream.read(CHUNK)
			frames.append(data)

		# Stop recording
		stream.stop_stream()
		stream.close()
		self.audio.terminate()

		log("TEST: Finished recording.")

		# Save to file:
		waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
		waveFile.setnchannels(CHANNELS)
		waveFile.setsampwidth(self.audio.get_sample_size(FORMAT))
		waveFile.setframerate(RATE)
		waveFile.writeframes(b''.join(frames))
		waveFile.close()

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

def network_testcode():
	soundlooper = Soundlooper(self)
	# Create server
	# Connect with client
	# Stream data
