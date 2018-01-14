# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Dec 26 2017)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class FrameMain
###########################################################################

class FrameMain ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"pyham", pos = wx.DefaultPosition, size = wx.Size( 702,509 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		#self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		gSizer3 = wx.GridSizer( 3, 1, 0, 0 )
		
		m_listBox3Choices = []
		self.m_listBox3 = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox3Choices, 0 )
		gSizer3.Add( self.m_listBox3, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer2 = wx.GridSizer( 1, 2, 0, 0 )
		
		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Preset", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		gSizer1.Add( self.m_staticText3, 0, wx.ALL, 5 )
		
		m_comboBox1Choices = []
		self.m_comboBox1 = wx.ComboBox( self, wx.ID_ANY, u"eqso.titanix.net", wx.DefaultPosition, wx.DefaultSize, m_comboBox1Choices, 0 )
		gSizer1.Add( self.m_comboBox1, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Server", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		gSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )
		
		self.m_textCtrlServer = wx.TextCtrl( self, wx.ID_ANY, u"eqso.titanix.net", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_textCtrlServer, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Port", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		gSizer1.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		self.m_textCtrlPort = wx.TextCtrl( self, wx.ID_ANY, u"5000", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_textCtrlPort, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_buttonConnect = wx.Button( self, wx.ID_ANY, u"Connect", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_buttonConnect, 0, wx.ALL, 5 )
		
		self.m_buttonDisconnect = wx.Button( self, wx.ID_ANY, u"Disconnect", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonDisconnect.Enable( False )
		
		gSizer1.Add( self.m_buttonDisconnect, 0, wx.ALL, 5 )
		
		self.m_checkBoxReconnect = wx.CheckBox( self, wx.ID_ANY, u"Reconnect", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_checkBoxReconnect, 0, wx.ALL, 5 )
		
		
		gSizer2.Add( gSizer1, 1, wx.EXPAND, 5 )
		
		gSizer6 = wx.GridSizer( 0, 1, 0, 0 )
		
		self.m_buttonPTT = wx.Button( self, wx.ID_ANY, u"PTT", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonPTT.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		
		gSizer6.Add( self.m_buttonPTT, 0, wx.ALL|wx.EXPAND, 5 )
		
		gSizerVU = wx.GridSizer( 0, 1, 0, 0 )
		
		gSizer7 = wx.GridSizer( 3, 2, 0, 0 )
		
		self.m_staticTextSpeaker = wx.StaticText( self, wx.ID_ANY, u"Speaker", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextSpeaker.Wrap( -1 )
		gSizer7.Add( self.m_staticTextSpeaker, 0, wx.ALL, 5 )
		
		self.m_staticTextMic = wx.StaticText( self, wx.ID_ANY, u"Mic", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextMic.Wrap( -1 )
		gSizer7.Add( self.m_staticTextMic, 0, wx.ALL, 5 )
		
		self.m_gaugeSpeaker = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.m_gaugeSpeaker.SetValue( 50 ) 
		gSizer7.Add( self.m_gaugeSpeaker, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_gaugeMic = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.m_gaugeMic.SetValue( 50 ) 
		gSizer7.Add( self.m_gaugeMic, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_sliderSpeaker = wx.Slider( self, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.Size( -1,-1 ), wx.SL_HORIZONTAL )
		gSizer7.Add( self.m_sliderSpeaker, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_sliderMic = wx.Slider( self, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		gSizer7.Add( self.m_sliderMic, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		gSizerVU.Add( gSizer7, 1, wx.EXPAND, 5 )
		
		
		gSizer6.Add( gSizerVU, 1, wx.EXPAND, 5 )
		
		
		gSizer2.Add( gSizer6, 1, wx.EXPAND, 5 )
		
		
		bSizer1.Add( gSizer2, 1, wx.EXPAND, 5 )
		
		
		gSizer3.Add( bSizer1, 1, wx.EXPAND, 5 )
		
		gSizer8 = wx.GridSizer( 0, 1, 0, 0 )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"City / Comment", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		gSizer8.Add( self.m_staticText4, 0, wx.ALL, 5 )
		
		self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer8.Add( self.m_textCtrl3, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Room", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		gSizer8.Add( self.m_staticText7, 0, wx.ALL, 5 )
		
		m_comboBox2Choices = []
		self.m_comboBox2 = wx.ComboBox( self, wx.ID_ANY, u"FINLAND", wx.DefaultPosition, wx.DefaultSize, m_comboBox2Choices, 0 )
		gSizer8.Add( self.m_comboBox2, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_button11 = wx.Button( self, wx.ID_ANY, u"Send", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer8.Add( self.m_button11, 0, wx.ALL, 5 )
		
		
		gSizer3.Add( gSizer8, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( gSizer3 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_buttonConnect.Bind( wx.EVT_BUTTON, self.click_connect )
		self.m_buttonDisconnect.Bind( wx.EVT_BUTTON, self.click_disconnect )
		self.m_buttonPTT.Bind( wx.EVT_BUTTON, self.click_ptt )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def click_connect( self, event ):
		event.Skip()
	
	def click_disconnect( self, event ):
		event.Skip()
	
	def click_ptt( self, event ):
		event.Skip()
	

