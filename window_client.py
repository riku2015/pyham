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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"pyham", pos = wx.DefaultPosition, size = wx.Size( 620,520 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL, name = u"pyham" )
		
		#self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		fgSizer2 = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer2.AddGrowableCol( 0 )
		fgSizer2.AddGrowableRow( 1 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		fgSizer6 = wx.FlexGridSizer( 0, 0, 0, 0 )
		fgSizer6.AddGrowableCol( 1 )
		fgSizer6.SetFlexibleDirection( wx.BOTH )
		fgSizer6.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.staticText_Room = wx.StaticText( self, wx.ID_ANY, u"Room", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_Room.Wrap( -1 )
		fgSizer6.Add( self.staticText_Room, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		comboBox_RoomChoices = []
		self.comboBox_Room = wx.ComboBox( self, wx.ID_ANY, u"FINLAND", wx.DefaultPosition, wx.DefaultSize, comboBox_RoomChoices, 0 )
		fgSizer6.Add( self.comboBox_Room, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		fgSizer2.Add( fgSizer6, 1, wx.EXPAND, 5 )
		
		m_listBox3Choices = []
		self.m_listBox3 = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox3Choices, 0 )
		fgSizer2.Add( self.m_listBox3, 0, wx.ALL|wx.EXPAND, 5 )
		
		fgSizer4 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer4.AddGrowableCol( 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer7 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer7.AddGrowableCol( 1 )
		fgSizer7.SetFlexibleDirection( wx.BOTH )
		fgSizer7.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.staticText_Comment = wx.StaticText( self, wx.ID_ANY, u"Comment (city)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_Comment.Wrap( -1 )
		fgSizer7.Add( self.staticText_Comment, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.textCtrl_Comment = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.textCtrl_Comment, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer2.Add( fgSizer7, 1, wx.EXPAND, 5 )
		
		
		fgSizer4.Add( bSizer2, 1, wx.EXPAND, 5 )
		
		self.button_Send = wx.Button( self, wx.ID_ANY, u"Send", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.button_Send, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		fgSizer2.Add( fgSizer4, 1, wx.EXPAND, 5 )
		
		fgSizer21 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer21.AddGrowableCol( 0 )
		fgSizer21.SetFlexibleDirection( wx.BOTH )
		fgSizer21.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		fgSizer3 = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer3.AddGrowableCol( 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		fgSizer5 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer5.AddGrowableCol( 1 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.staticText_Preset = wx.StaticText( self, wx.ID_ANY, u"Preset", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_Preset.Wrap( -1 )
		fgSizer5.Add( self.staticText_Preset, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		comboBox_PresetChoices = []
		self.comboBox_Preset = wx.ComboBox( self, wx.ID_ANY, u"eqso.titanix.net", wx.DefaultPosition, wx.DefaultSize, comboBox_PresetChoices, 0 )
		fgSizer5.Add( self.comboBox_Preset, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.staticText_Server = wx.StaticText( self, wx.ID_ANY, u"Server", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_Server.Wrap( -1 )
		fgSizer5.Add( self.staticText_Server, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.textCtrl_Server = wx.TextCtrl( self, wx.ID_ANY, u"eqso.titanix.net", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.textCtrl_Server, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.staticText_Port = wx.StaticText( self, wx.ID_ANY, u"Port", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_Port.Wrap( -1 )
		fgSizer5.Add( self.staticText_Port, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.textCtrl_Port = wx.TextCtrl( self, wx.ID_ANY, u"5000", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.textCtrl_Port, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		fgSizer3.Add( fgSizer5, 1, wx.EXPAND, 5 )
		
		gSizer9 = wx.GridSizer( 0, 3, 0, 0 )
		
		self.button_Load = wx.Button( self, wx.ID_ANY, u"Load", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer9.Add( self.button_Load, 0, wx.ALL, 5 )
		
		self.button_Delete = wx.Button( self, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer9.Add( self.button_Delete, 0, wx.ALL, 5 )
		
		self.button_Save = wx.Button( self, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer9.Add( self.button_Save, 0, wx.ALL, 5 )
		
		self.button_Connect = wx.Button( self, wx.ID_ANY, u"Connect", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer9.Add( self.button_Connect, 0, wx.ALL, 5 )
		
		self.button_Disconnect = wx.Button( self, wx.ID_ANY, u"Disconnect", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.button_Disconnect.Enable( False )
		
		gSizer9.Add( self.button_Disconnect, 0, wx.ALL, 5 )
		
		self.checkBox_Reconnect = wx.CheckBox( self, wx.ID_ANY, u"Reconnect", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer9.Add( self.checkBox_Reconnect, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		fgSizer3.Add( gSizer9, 1, wx.EXPAND, 5 )
		
		
		fgSizer21.Add( fgSizer3, 1, wx.EXPAND, 5 )
		
		gSizer6 = wx.GridSizer( 0, 1, 0, 0 )
		
		gSizerVU = wx.GridSizer( 0, 1, 0, 0 )
		
		fgSizer8 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer8.SetFlexibleDirection( wx.BOTH )
		fgSizer8.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.staticText_Speaker = wx.StaticText( self, wx.ID_ANY, u"Speaker", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_Speaker.Wrap( -1 )
		fgSizer8.Add( self.staticText_Speaker, 0, wx.ALL, 5 )
		
		self.staticText_Mic = wx.StaticText( self, wx.ID_ANY, u"Mic", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_Mic.Wrap( -1 )
		fgSizer8.Add( self.staticText_Mic, 0, wx.ALL, 5 )
		
		self.gauge_Speaker = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.gauge_Speaker.SetValue( 50 ) 
		fgSizer8.Add( self.gauge_Speaker, 0, wx.ALL, 5 )
		
		self.gauge_Mic = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.gauge_Mic.SetValue( 50 ) 
		fgSizer8.Add( self.gauge_Mic, 0, wx.ALL, 5 )
		
		self.slider_Speaker = wx.Slider( self, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.Size( -1,-1 ), wx.SL_HORIZONTAL )
		fgSizer8.Add( self.slider_Speaker, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.slider_Mic = wx.Slider( self, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		fgSizer8.Add( self.slider_Mic, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		gSizerVU.Add( fgSizer8, 1, wx.EXPAND, 5 )
		
		
		gSizer6.Add( gSizerVU, 1, wx.EXPAND, 5 )
		
		self.button_ptt = wx.Button( self, wx.ID_ANY, u"Push To Talk", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.button_ptt.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.button_ptt.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.button_ptt.SetBackgroundColour( wx.Colour( 186, 216, 200 ) )
		
		gSizer6.Add( self.button_ptt, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		fgSizer21.Add( gSizer6, 1, 0, 5 )
		
		
		fgSizer2.Add( fgSizer21, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( fgSizer2 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.button_Send.Bind( wx.EVT_BUTTON, self.click_send )
		self.button_Load.Bind( wx.EVT_BUTTON, self.click_load )
		self.button_Delete.Bind( wx.EVT_BUTTON, self.click_delete )
		self.button_Save.Bind( wx.EVT_BUTTON, self.click_save )
		self.button_Connect.Bind( wx.EVT_BUTTON, self.click_connect )
		self.button_Disconnect.Bind( wx.EVT_BUTTON, self.click_disconnect )
		self.button_ptt.Bind( wx.EVT_KEY_DOWN, self.push_ptt )
		self.button_ptt.Bind( wx.EVT_KEY_UP, self.release_ptt )
		self.button_ptt.Bind( wx.EVT_LEFT_DOWN, self.push_ptt )
		self.button_ptt.Bind( wx.EVT_LEFT_UP, self.release_ptt )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def click_send( self, event ):
		event.Skip()
	
	def click_load( self, event ):
		event.Skip()
	
	def click_delete( self, event ):
		event.Skip()
	
	def click_save( self, event ):
		event.Skip()
	
	def click_connect( self, event ):
		event.Skip()
	
	def click_disconnect( self, event ):
		event.Skip()
	
	def push_ptt( self, event ):
		event.Skip()
	
	def release_ptt( self, event ):
		event.Skip()
	
	
	

