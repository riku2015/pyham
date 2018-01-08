#!/usr/bin/python

# pyham ver. 0.001
programName = "pyham"
programVersion = "0.001"

#import wxversion
#wxversion.select("2.8")
import wx, wx.html
import sys

from window import MyFrame1

# OLD TEST CODE:
	# from tests import HtmlWindow
	# from tests import AboutBox
	# from tests import Frame

app = wx.App(False)   # Error messages go to popup window
main = MyFrame1(parent=None)
main.Show()
app.MainLoop()

# TODO:
# - Button to talk (ptt)
# - File recorder/player (.wav, .mp3 etc.)
# - Networking
# - Room/Channel selection
# - Checkbox for Auto reconnect
# - Textfields for Server, Port and setting presets.
# - Mic and speaker volume button, VU meters, scope graph, spectrogram
# - VoIP protocol
# - eQSO protocol
# - Echolink protocol
# - wxFormBuilder generates erroneous code: self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
