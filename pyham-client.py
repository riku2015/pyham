#!/usr/bin/python

# pyham client program

programName = "pyham client"
programVersion = "0.002"

import wx, wx.html
import sys
import wave
import pyaudio
#import sounddevice as sd

from pyham import log
from pyham import EqsoServerConnection

from window_client import FrameMain

filename_settings = "pyham-client.conf"		# For saving presets etc.

#server_connection = None
server_name = "frn.titanix.net"
server_port = 10024
#server_protocol = "echolink"	# TODO: Named constants

def config_read():
	log("Loading config file.")
	# TODO: return or set values in variables

class Mainwindow(FrameMain):
	# constructor
	def __init__(self,parent):
		# initialize parent class
		FrameMain.__init__(self,parent)

	def push_ptt(self,event):
		try:
			log("PTT button pushed down, recording audio to server...")
			# Set PTT button color to red
		except Exception:
			log('error')

	def release_ptt(self,event):
		try:
			log("PTT button released, end recording to server.")
			# Set PTT button color to green
			# Roger beep
		except Exception:
			log('error')

	def click_load(self,event):
		try:
			# Load preset
			log('Load preset.')
		except Exception:
			log('error')

	def click_delete(self,event):
		try:
			# Delete preset
			log('Delete preset.')
		except Exception:
			log('error')

	def click_save(self,event):
		try:
			# Save preset
			log('Save preset.')
		except Exception:
			log('error')

	def click_connect(self,event):
		try:
			# Connect to server
			server_connection = EqsoServerConnection()
			server_connection.connect(server_name, server_port)

			# If successfull, disable connect button and enable disconnect button:
			# TODO
		
			# If successfull, play sound:
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
		except Exception:
			log('error')

	def click_disconnect(self,event):
		try:
			log("Disconnect from server.")
			server_connection.disconnect()		# katkaise (ei kylla toimi..)
			# Enable connect button and disable disconnect button.
		except Exception:
			log('error')

	def click_send(self,event):
		try:
			log("Send to server.")
		except Exception:
			log('error')

# Create wxwidgets application:
app = wx.App(False)
mainwindow = Mainwindow(parent=None)

# Show main window:
mainwindow.Show()

# Execute GUI:
app.MainLoop()


# TODO:
# - File recorder/player (.wav, .mp3 etc.)
# - Networking
# - Selection for input and output devices (Mic1, Mic2 etc.)
# - Scope graph, spectrogram
# - VoIP protocol
# - eQSO protocol
# - Echolink protocol
# - pyham protocol
# - Space key as PTT button without character repeating loop
# - Translate to different languages / Loalization
# - PTT push and release with keyboard
