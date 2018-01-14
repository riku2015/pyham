#!/usr/bin/python

# pyham ver. 0.001
programName = "pyham"
programVersion = "0.001"

import wx, wx.html
import sys
#import sounddevice as sd
import wave
import pyaudio

from window import FrameMain

class Mainwindow(FrameMain):
	#constructor
	def __init__(self,parent):
		#initialize parent class
		FrameMain.__init__(self,parent)
	def click_ptt(self,event):
		try:
			print >>sys.stderr, "PTT button clicked."
			# Play sound:
			CHUNK = 1024
			wf = wave.open("sound.wav", 'rb')
			p = pyaudio.PyAudio()
			stream = p.open(format=p.get_format_from_width(wf.getsampwidth()), channels=wf.getnchannels(), rate=wf.getframerate(), output=True)
			data = wf.readframes(CHUNK)
			while data != '':
				stream.write(data)
				data = wf.readframes(CHUNK)
			stream.stop_stream()
			stream.close()
			p.terminate()

		except Exception:
			print 'error'

	def click_connect(self,event):
		print >>sys.stderr, "Connect to server."

	def click_disconnect(self,event):
		print >>sys.stderr, "Disconnect from server."

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
# - wxFormBuilder generates erroneous code: self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
