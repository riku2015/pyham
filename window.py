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
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"pyham", pos = wx.DefaultPosition, size = wx.Size( 517,509 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		#self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		gSizer3 = wx.GridSizer( 3, 1, 0, 0 )
		
		m_listBox3Choices = []
		self.m_listBox3 = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox3Choices, 0 )
		gSizer3.Add( self.m_listBox3, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer2 = wx.GridSizer( 1, 2, 0, 0 )
		
		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Server", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		gSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )
		
		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_textCtrl1, 0, wx.ALL, 5 )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Port", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		gSizer1.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_textCtrl2, 0, wx.ALL, 5 )
		
		self.m_buttonConnect = wx.Button( self, wx.ID_ANY, u"Connect", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_buttonConnect, 0, wx.ALL, 5 )
		
		self.m_buttonDisconnect = wx.Button( self, wx.ID_ANY, u"Disconnect", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_buttonDisconnect, 0, wx.ALL, 5 )
		
		self.m_checkBox1 = wx.CheckBox( self, wx.ID_ANY, u"Reconnect", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_checkBox1, 0, wx.ALL, 5 )
		
		
		gSizer2.Add( gSizer1, 1, wx.EXPAND, 5 )
		
		gSizer6 = wx.GridSizer( 0, 1, 0, 0 )
		
		self.m_buttonPTT = wx.Button( self, wx.ID_ANY, u"PTT", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer6.Add( self.m_buttonPTT, 0, wx.ALL|wx.EXPAND, 5 )
		
		gSizerVU = wx.GridSizer( 0, 1, 0, 0 )
		
		gSizer7 = wx.GridSizer( 3, 2, 0, 0 )
		
		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Speaker", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		gSizer7.Add( self.m_staticText8, 0, wx.ALL, 5 )
		
		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Mic", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		gSizer7.Add( self.m_staticText9, 0, wx.ALL, 5 )
		
		self.m_gauge11 = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.m_gauge11.SetValue( 50 ) 
		gSizer7.Add( self.m_gauge11, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_gauge1 = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.m_gauge1.SetValue( 50 ) 
		gSizer7.Add( self.m_gauge1, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_slider1 = wx.Slider( self, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.Size( -1,-1 ), wx.SL_HORIZONTAL )
		gSizer7.Add( self.m_slider1, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_slider2 = wx.Slider( self, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		gSizer7.Add( self.m_slider2, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		gSizerVU.Add( gSizer7, 1, wx.EXPAND, 5 )
		
		
		gSizer6.Add( gSizerVU, 1, wx.EXPAND, 5 )
		
		
		gSizer2.Add( gSizer6, 1, wx.EXPAND, 5 )
		
		
		bSizer1.Add( gSizer2, 1, wx.EXPAND, 5 )
		
		
		gSizer3.Add( bSizer1, 1, wx.EXPAND, 5 )
		
		gSizer8 = wx.GridSizer( 0, 1, 0, 0 )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Preset", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		gSizer8.Add( self.m_staticText3, 0, wx.ALL, 5 )
		
		m_listBox1Choices = []
		self.m_listBox1 = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox1Choices, 0 )
		gSizer8.Add( self.m_listBox1, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"City / Comment", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		gSizer8.Add( self.m_staticText4, 0, wx.ALL, 5 )
		
		self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer8.Add( self.m_textCtrl3, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Room", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		gSizer8.Add( self.m_staticText7, 0, wx.ALL, 5 )
		
		m_listBox2Choices = []
		self.m_listBox2 = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox2Choices, 0 )
		gSizer8.Add( self.m_listBox2, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_button11 = wx.Button( self, wx.ID_ANY, u"Send", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer8.Add( self.m_button11, 0, wx.ALL, 5 )
		
		
		gSizer3.Add( gSizer8, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( gSizer3 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

