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
		
		fgSizer_Roomselect = wx.FlexGridSizer( 0, 0, 0, 0 )
		fgSizer_Roomselect.AddGrowableCol( 1 )
		fgSizer_Roomselect.SetFlexibleDirection( wx.BOTH )
		fgSizer_Roomselect.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.staticText_Room = wx.StaticText( self, wx.ID_ANY, u"Room", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_Room.Wrap( -1 )
		fgSizer_Roomselect.Add( self.staticText_Room, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		comboBox_RoomChoices = []
		self.comboBox_Room = wx.ComboBox( self, wx.ID_ANY, u"FINLAND", wx.DefaultPosition, wx.DefaultSize, comboBox_RoomChoices, 0 )
		fgSizer_Roomselect.Add( self.comboBox_Room, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		fgSizer2.Add( fgSizer_Roomselect, 1, wx.EXPAND, 5 )
		
		listBox_UsersChoices = []
		self.listBox_Users = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, listBox_UsersChoices, 0 )
		fgSizer2.Add( self.listBox_Users, 0, wx.EXPAND|wx.ALL, 5 )
		
		fgSizer_Send = wx.FlexGridSizer( 0, 5, 0, 0 )
		fgSizer_Send.AddGrowableCol( 3 )
		fgSizer_Send.SetFlexibleDirection( wx.HORIZONTAL )
		fgSizer_Send.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.staticTextCall = wx.StaticText( self, wx.ID_ANY, u"Callsign", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticTextCall.Wrap( -1 )
		fgSizer_Send.Add( self.staticTextCall, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.textCtrlCall = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textCtrlCall.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		
		fgSizer_Send.Add( self.textCtrlCall, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.staticText_Description = wx.StaticText( self, wx.ID_ANY, u"Description", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_Description.Wrap( -1 )
		fgSizer_Send.Add( self.staticText_Description, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.textCtrl_Comment = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textCtrl_Comment.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		
		fgSizer_Send.Add( self.textCtrl_Comment, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.button_Send = wx.Button( self, wx.ID_ANY, u"Send", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer_Send.Add( self.button_Send, 0, wx.ALL, 5 )
		
		
		fgSizer2.Add( fgSizer_Send, 0, wx.EXPAND, 5 )
		
		fgSizer21 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer21.AddGrowableCol( 0 )
		fgSizer21.SetFlexibleDirection( wx.BOTH )
		fgSizer21.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.panel_Server = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER|wx.TAB_TRAVERSAL )
		fgSizer16 = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer16.AddGrowableCol( 0 )
		fgSizer16.SetFlexibleDirection( wx.BOTH )
		fgSizer16.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		fgSizer5 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer5.AddGrowableCol( 1 )
		fgSizer5.SetFlexibleDirection( wx.HORIZONTAL )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.staticText_Preset = wx.StaticText( self.panel_Server, wx.ID_ANY, u"Preset", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_Preset.Wrap( -1 )
		fgSizer5.Add( self.staticText_Preset, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		comboBox_PresetChoices = []
		self.comboBox_Preset = wx.ComboBox( self.panel_Server, wx.ID_ANY, u"frn.titanix.net", wx.DefaultPosition, wx.DefaultSize, comboBox_PresetChoices, 0 )
		fgSizer5.Add( self.comboBox_Preset, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.staticText_Server = wx.StaticText( self.panel_Server, wx.ID_ANY, u"Server", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_Server.Wrap( -1 )
		fgSizer5.Add( self.staticText_Server, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.textCtrl_Server = wx.TextCtrl( self.panel_Server, wx.ID_ANY, u"frn.titanix.net", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.textCtrl_Server, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.staticText_Port = wx.StaticText( self.panel_Server, wx.ID_ANY, u"Port", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_Port.Wrap( -1 )
		fgSizer5.Add( self.staticText_Port, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.textCtrl_Port = wx.TextCtrl( self.panel_Server, wx.ID_ANY, u"10024", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.textCtrl_Port, 0, wx.ALL, 5 )
		
		self.staticText_Protocol = wx.StaticText( self.panel_Server, wx.ID_ANY, u"Protocol", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_Protocol.Wrap( -1 )
		fgSizer5.Add( self.staticText_Protocol, 0, wx.ALL, 5 )
		
		comboBox_ProtocolChoices = []
		self.comboBox_Protocol = wx.ComboBox( self.panel_Server, wx.ID_ANY, u"FRN", wx.DefaultPosition, wx.DefaultSize, comboBox_ProtocolChoices, 0 )
		fgSizer5.Add( self.comboBox_Protocol, 0, wx.ALL, 5 )
		
		
		fgSizer16.Add( fgSizer5, 1, wx.EXPAND, 5 )
		
		fgSizer13 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer13.SetFlexibleDirection( wx.HORIZONTAL )
		fgSizer13.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.button_Load = wx.Button( self.panel_Server, wx.ID_ANY, u"Load", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer13.Add( self.button_Load, 0, wx.ALL, 5 )
		
		self.button_Delete = wx.Button( self.panel_Server, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer13.Add( self.button_Delete, 0, wx.ALL, 5 )
		
		self.button_Save = wx.Button( self.panel_Server, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer13.Add( self.button_Save, 0, wx.ALL, 5 )
		
		
		fgSizer16.Add( fgSizer13, 1, wx.EXPAND, 5 )
		
		fgSizer18 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer18.SetFlexibleDirection( wx.HORIZONTAL )
		fgSizer18.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.button_Connect = wx.Button( self.panel_Server, wx.ID_ANY, u"Connect", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer18.Add( self.button_Connect, 0, wx.ALL, 5 )
		
		self.button_Disconnect = wx.Button( self.panel_Server, wx.ID_ANY, u"Disconnect", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.button_Disconnect.Enable( False )
		
		fgSizer18.Add( self.button_Disconnect, 0, wx.ALL, 5 )
		
		self.checkBox_Reconnect = wx.CheckBox( self.panel_Server, wx.ID_ANY, u"Reconnect", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer18.Add( self.checkBox_Reconnect, 0, wx.ALL, 5 )
		
		
		fgSizer16.Add( fgSizer18, 1, wx.EXPAND, 5 )
		
		
		self.panel_Server.SetSizer( fgSizer16 )
		self.panel_Server.Layout()
		fgSizer16.Fit( self.panel_Server )
		fgSizer21.Add( self.panel_Server, 1, wx.ALL|wx.EXPAND, 5 )
		
		fgSizer_Talk = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer_Talk.AddGrowableRow( 1 )
		fgSizer_Talk.SetFlexibleDirection( wx.BOTH )
		fgSizer_Talk.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.panel_Speaker = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER|wx.TAB_TRAVERSAL )
		fgSizer_Speaker = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer_Speaker.SetFlexibleDirection( wx.BOTH )
		fgSizer_Speaker.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.staticText_Speaker = wx.StaticText( self.panel_Speaker, wx.ID_ANY, u"Speaker", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_Speaker.Wrap( -1 )
		self.staticText_Speaker.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		
		fgSizer_Speaker.Add( self.staticText_Speaker, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.gauge_Speaker = wx.Gauge( self.panel_Speaker, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.gauge_Speaker.SetValue( 50 ) 
		fgSizer_Speaker.Add( self.gauge_Speaker, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.slider_Speaker = wx.Slider( self.panel_Speaker, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.Size( -1,-1 ), wx.SL_HORIZONTAL )
		fgSizer_Speaker.Add( self.slider_Speaker, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.panel_Speaker.SetSizer( fgSizer_Speaker )
		self.panel_Speaker.Layout()
		fgSizer_Speaker.Fit( self.panel_Speaker )
		gSizer1.Add( self.panel_Speaker, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.panel_Mic = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER|wx.TAB_TRAVERSAL )
		fgSizer_Mic = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer_Mic.SetFlexibleDirection( wx.BOTH )
		fgSizer_Mic.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.staticText_Mic = wx.StaticText( self.panel_Mic, wx.ID_ANY, u"Mic", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_Mic.Wrap( -1 )
		self.staticText_Mic.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		
		fgSizer_Mic.Add( self.staticText_Mic, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.gauge_Mic = wx.Gauge( self.panel_Mic, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.gauge_Mic.SetValue( 50 ) 
		fgSizer_Mic.Add( self.gauge_Mic, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.slider_Mic = wx.Slider( self.panel_Mic, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		fgSizer_Mic.Add( self.slider_Mic, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.panel_Mic.SetSizer( fgSizer_Mic )
		self.panel_Mic.Layout()
		fgSizer_Mic.Fit( self.panel_Mic )
		gSizer1.Add( self.panel_Mic, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		fgSizer_Talk.Add( gSizer1, 1, wx.EXPAND, 5 )
		
		self.button_Ptt = wx.Button( self, wx.ID_ANY, u"Push To Talk", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.button_Ptt.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.button_Ptt.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.button_Ptt.SetBackgroundColour( wx.Colour( 186, 216, 200 ) )
		
		fgSizer_Talk.Add( self.button_Ptt, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		fgSizer21.Add( fgSizer_Talk, 1, wx.EXPAND, 5 )
		
		
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
		self.button_Ptt.Bind( wx.EVT_KEY_DOWN, self.push_ptt )
		self.button_Ptt.Bind( wx.EVT_KEY_UP, self.release_ptt )
		self.button_Ptt.Bind( wx.EVT_LEFT_DOWN, self.push_ptt )
		self.button_Ptt.Bind( wx.EVT_LEFT_UP, self.release_ptt )
	
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
	
	
	

