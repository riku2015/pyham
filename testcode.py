#!/usr/bin/python

# This file contains temporary test code and unfinished classes and routines.
# It is not meant for testing the runtime environment itself.
# It should not be imported at all in a final release.

from log import log
import pyaudio
import wave

from server_protocols import ServerProtocol

class ServerProtocolTest(ServerProtocol):
	def __init__(self, name, address, port):
		ServerProtocol.__init__(self, name, address, port)
		self.protocolname = "TEST"

	def connect(self):
		ServerProtocol.connect(self)

	def run(self):
		self.bind()
		while True:
			# Wait for a connection
			log('Waiting for incoming connection...')
			connection, client_address = self.socket.accept()
			try:
				Log('incoming from' + client_address)

				# Receive the data in small chunks and retransmit it
				while True:
					data = connection.recv(16)
					Log('received "%s"' % data)
					if data:
						Log('sending data back to the client')
						connection.sendall(data)
					else:
						Log('no more data from ' + client_address)
						break

			finally:
				# Clean up the connection
				connection.close()

from client_protocols import ClientProtocol

class ClientProtocolTest(ClientProtocol):
	def __init__(self, address, port):
		ClientProtocol.__init__(self, address, port)

	def connect(self):
		log("Connecting to server " + self.address + " at port " + str(self.port) + " using TEST...")
		self.socket.connect((self.address, self.port))
		log("Connected.")

	def disconnect(self):
		#self.socket.send("")
		log("Disconnected.")

	def test(self):
		self.socket.send(data)
		amount_received = 0
		amount_expected = 1
		try:
			# Send data
			message = 'This is the message.  It will be repeated.'
			print >>sys.stderr, 'sending "%s"' % message
			sock.sendall(message)

			# Look for the response
			amount_received = 0
			amount_expected = len(message)

			while amount_received < amount_expected:
				data = sock.recv(16)
				amount_received += len(data)
				print >>sys.stderr, 'received "%s"' % data

		finally:
			print >>sys.stderr, 'closing socket'
			sock.close()

'''
p = pyaudio.PyAudio()
for i in range(p.get_device_count()):
	print p.get_device_info_by_index(i)
'''

def get_audiodevices():
	p = pyaudio.PyAudio()
	info = p.get_host_api_info_by_index(0)
	numdevices = info.get('deviceCount')
	result = ""
	for i in range(0, numdevices):
			if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
				result += "Input Device id " + str(i) + " - " + p.get_device_info_by_host_api_device_index(0, i).get('name') + "\n"
	return result

def play_testsound():
	CHUNK = 1024
	wave_test = wave.open("sound.wav", 'rb')
	audio_test = pyaudio.PyAudio()
	stream_test = audio_test.open(format=audio_test.get_format_from_width(wave_test.getsampwidth()), channels=wave_test.getnchannels(), rate=wave_test.getframerate(), output=True)
	data_test = wave_test.readframes(CHUNK)
	while data_test != '':
		stream_test.write(data_test)
		data_test = wave_test.readframes(CHUNK)
	stream_test.stop_stream()
	stream_test.close()
	audio_test.terminate()

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
