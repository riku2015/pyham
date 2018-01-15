#!/usr/bin/python

# pyham client program

programName = "pyham client"
programVersion = "0.001"

import wx, wx.html
import sys
import wave
import pyaudio
#import sounddevice as sd

from window_client import FrameMain

class Mainwindow(FrameMain):
	# constructor
	def __init__(self,parent):
		# initialize parent class
		FrameMain.__init__(self,parent)

	def push_ptt(self,event):
		try:
			print >>sys.stderr, "PTT button pushed down, recording audio to server..."
			# Set PTT button color to red
		except Exception:
			print 'error'

	def release_ptt(self,event):
		try:
			print >>sys.stderr, "PTT button released, end recording to server."
			# Set PTT button color to green
			# Roger beep
		except Exception:
			print 'error'

	def click_load(self,event):
		try:
			# Load preset
			print 'Load preset.'
		except Exception:
			print 'error'

	def click_delete(self,event):
		try:
			# Delete preset
			print 'Delete preset.'
		except Exception:
			print 'error'

	def click_save(self,event):
		try:
			# Save preset
			print 'Save preset.'
		except Exception:
			print 'error'

	def click_connect(self,event):
		try:
			print >>sys.stderr, "Connect to server."
			# If successfull, disable connect button and enable disconnect button.
			# Play sound test:
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
			print 'error'

	def click_disconnect(self,event):
		try:
			print >>sys.stderr, "Disconnect from server."
			# Enable connect button and disable disconnect button.
		except Exception:
			print 'error'

	def click_send(self,event):
		try:
			print >>sys.stderr, "Send to server."
		except Exception:
			print 'error'

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
# - Scope graph, spectrogram
# - VoIP protocol
# - eQSO protocol
# - Echolink protocol
# - Space key as PTT button without character repeating loop
# - Translate to different languages / Loalization
