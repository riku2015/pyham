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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Pyham Client", pos = wx.DefaultPosition, size = wx.Size( 680,540 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL, name = u"pyham" )
		
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
		
		choice_RoomChoices = []
		self.choice_Room = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choice_RoomChoices, 0 )
		self.choice_Room.SetSelection( 0 )
		fgSizer_Roomselect.Add( self.choice_Room, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.button_Settings = wx.Button( self, wx.ID_ANY, u"Settings", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer_Roomselect.Add( self.button_Settings, 0, wx.ALL, 5 )
		
		
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
		
		fgSizer27 = wx.FlexGridSizer( 0, 4, 0, 0 )
		fgSizer27.AddGrowableCol( 0 )
		fgSizer27.AddGrowableCol( 2 )
		fgSizer27.SetFlexibleDirection( wx.BOTH )
		fgSizer27.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.textCtrl_Port = wx.TextCtrl( self.panel_Server, wx.ID_ANY, u"10024", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer27.Add( self.textCtrl_Port, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.staticText_Protocol = wx.StaticText( self.panel_Server, wx.ID_ANY, u"Protocol", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_Protocol.Wrap( -1 )
		fgSizer27.Add( self.staticText_Protocol, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		choice_ProtocolChoices = [ u"Frn", u"Eqso", u"Echolink", u"Pyhamp" ]
		self.choice_Protocol = wx.Choice( self.panel_Server, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choice_ProtocolChoices, 0 )
		self.choice_Protocol.SetSelection( 0 )
		fgSizer27.Add( self.choice_Protocol, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		fgSizer5.Add( fgSizer27, 1, wx.EXPAND, 5 )
		
		
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
		
		Sizer_Audio = wx.FlexGridSizer( 0, 2, 0, 0 )
		Sizer_Audio.SetFlexibleDirection( wx.BOTH )
		Sizer_Audio.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.panel_Speaker = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.SUNKEN_BORDER|wx.TAB_TRAVERSAL )
		fgSizer_Speaker = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer_Speaker.AddGrowableRow( 0 )
		fgSizer_Speaker.AddGrowableRow( 1 )
		fgSizer_Speaker.AddGrowableRow( 2 )
		fgSizer_Speaker.SetFlexibleDirection( wx.BOTH )
		fgSizer_Speaker.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		fgSizer24 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer24.AddGrowableCol( 1 )
		fgSizer24.SetFlexibleDirection( wx.BOTH )
		fgSizer24.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.staticText_Speaker = wx.StaticText( self.panel_Speaker, wx.ID_ANY, u"Spk", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_Speaker.Wrap( -1 )
		self.staticText_Speaker.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		
		fgSizer24.Add( self.staticText_Speaker, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		choise_SpeakerChoices = [ u"Spk 1", u"Spk 2" ]
		self.choise_Speaker = wx.Choice( self.panel_Speaker, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choise_SpeakerChoices, 0 )
		self.choise_Speaker.SetSelection( 0 )
		fgSizer24.Add( self.choise_Speaker, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		fgSizer_Speaker.Add( fgSizer24, 1, wx.EXPAND, 5 )
		
		self.slider_Speaker = wx.Slider( self.panel_Speaker, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.Size( -1,-1 ), wx.SL_HORIZONTAL )
		fgSizer_Speaker.Add( self.slider_Speaker, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.gauge_Speaker = wx.Gauge( self.panel_Speaker, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.gauge_Speaker.SetValue( 50 ) 
		fgSizer_Speaker.Add( self.gauge_Speaker, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.panel_Speaker.SetSizer( fgSizer_Speaker )
		self.panel_Speaker.Layout()
		fgSizer_Speaker.Fit( self.panel_Speaker )
		Sizer_Audio.Add( self.panel_Speaker, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.panel_Mic = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.SUNKEN_BORDER|wx.TAB_TRAVERSAL )
		fgSizer_Mic = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer_Mic.AddGrowableRow( 0 )
		fgSizer_Mic.AddGrowableRow( 1 )
		fgSizer_Mic.AddGrowableRow( 2 )
		fgSizer_Mic.SetFlexibleDirection( wx.BOTH )
		fgSizer_Mic.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		fgSizer25 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer25.AddGrowableCol( 1 )
		fgSizer25.SetFlexibleDirection( wx.BOTH )
		fgSizer25.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.staticText_Mic = wx.StaticText( self.panel_Mic, wx.ID_ANY, u"Mic", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_Mic.Wrap( -1 )
		self.staticText_Mic.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		
		fgSizer25.Add( self.staticText_Mic, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		choice_MicChoices = [ u"Mic 1", u"Mic 2" ]
		self.choice_Mic = wx.Choice( self.panel_Mic, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choice_MicChoices, 0 )
		self.choice_Mic.SetSelection( 0 )
		fgSizer25.Add( self.choice_Mic, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		fgSizer_Mic.Add( fgSizer25, 1, wx.EXPAND, 5 )
		
		self.slider_Mic = wx.Slider( self.panel_Mic, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		fgSizer_Mic.Add( self.slider_Mic, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.gauge_Mic = wx.Gauge( self.panel_Mic, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.gauge_Mic.SetValue( 50 ) 
		fgSizer_Mic.Add( self.gauge_Mic, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.panel_Mic.SetSizer( fgSizer_Mic )
		self.panel_Mic.Layout()
		fgSizer_Mic.Fit( self.panel_Mic )
		Sizer_Audio.Add( self.panel_Mic, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		fgSizer_Talk.Add( Sizer_Audio, 1, wx.EXPAND, 5 )
		
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
		self.button_Settings.Bind( wx.EVT_BUTTON, self.click_settings )
		self.button_Send.Bind( wx.EVT_BUTTON, self.click_send )
		self.button_Load.Bind( wx.EVT_BUTTON, self.click_load )
		self.button_Delete.Bind( wx.EVT_BUTTON, self.click_delete )
		self.button_Save.Bind( wx.EVT_BUTTON, self.click_save )
		self.button_Connect.Bind( wx.EVT_BUTTON, self.click_connect )
		self.button_Disconnect.Bind( wx.EVT_BUTTON, self.click_disconnect )
		self.slider_Speaker.Bind( wx.EVT_SCROLL, self.volume_speaker )
		self.slider_Mic.Bind( wx.EVT_SCROLL, self.volume_mic )
		self.button_Ptt.Bind( wx.EVT_KEY_DOWN, self.push_ptt )
		self.button_Ptt.Bind( wx.EVT_KEY_UP, self.release_ptt )
		self.button_Ptt.Bind( wx.EVT_LEFT_DOWN, self.push_ptt )
		self.button_Ptt.Bind( wx.EVT_LEFT_UP, self.release_ptt )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def click_settings( self, event ):
		event.Skip()
	
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
	
	def volume_speaker( self, event ):
		event.Skip()
	
	def volume_mic( self, event ):
		event.Skip()
	
	def push_ptt( self, event ):
		event.Skip()
	
	def release_ptt( self, event ):
		event.Skip()
	
	
	

###########################################################################
## Class FrameSettings
###########################################################################

class FrameSettings ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Pyham Client - Settings", pos = wx.DefaultPosition, size = wx.Size( 440,280 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		#self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		fgSizer18 = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer18.AddGrowableRow( 1 )
		fgSizer18.SetFlexibleDirection( wx.BOTH )
		fgSizer18.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.staticTextAbout = wx.StaticText( self, wx.ID_ANY, u"These settings apply when program starts up.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticTextAbout.Wrap( -1 )
		self.staticTextAbout.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		
		fgSizer18.Add( self.staticTextAbout, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		fgSizer14 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer14.AddGrowableCol( 0 )
		fgSizer14.AddGrowableCol( 1 )
		fgSizer14.SetFlexibleDirection( wx.BOTH )
		fgSizer14.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.panel_Sound = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER|wx.TAB_TRAVERSAL )
		fgSizer12 = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer12.SetFlexibleDirection( wx.BOTH )
		fgSizer12.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText17 = wx.StaticText( self.panel_Sound, wx.ID_ANY, u"Audio devices", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )
		self.m_staticText17.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		
		fgSizer12.Add( self.m_staticText17, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.staticText_Output = wx.StaticText( self.panel_Sound, wx.ID_ANY, u"Default output:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_Output.Wrap( -1 )
		fgSizer12.Add( self.staticText_Output, 0, wx.ALL, 5 )
		
		choice_OutputChoices = [ u"Spk 1", u"Spk 2" ]
		self.choice_Output = wx.Choice( self.panel_Sound, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choice_OutputChoices, 0 )
		self.choice_Output.SetSelection( 0 )
		fgSizer12.Add( self.choice_Output, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.staticText_Input = wx.StaticText( self.panel_Sound, wx.ID_ANY, u"Default input:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_Input.Wrap( -1 )
		fgSizer12.Add( self.staticText_Input, 0, wx.ALL, 5 )
		
		choice_InputChoices = [ u"Mic 1", u"Mic 2" ]
		self.choice_Input = wx.Choice( self.panel_Sound, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choice_InputChoices, 0 )
		self.choice_Input.SetSelection( 0 )
		fgSizer12.Add( self.choice_Input, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.panel_Sound.SetSizer( fgSizer12 )
		self.panel_Sound.Layout()
		fgSizer12.Fit( self.panel_Sound )
		fgSizer14.Add( self.panel_Sound, 1, wx.ALL, 5 )
		
		self.panel_Autoconnect = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER|wx.TAB_TRAVERSAL )
		fgSizer21 = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer21.SetFlexibleDirection( wx.BOTH )
		fgSizer21.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText16 = wx.StaticText( self.panel_Autoconnect, wx.ID_ANY, u"Autoconnect", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )
		self.m_staticText16.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		
		fgSizer21.Add( self.m_staticText16, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.staticText_Autoconnect = wx.StaticText( self.panel_Autoconnect, wx.ID_ANY, u"Server preset:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_Autoconnect.Wrap( -1 )
		fgSizer21.Add( self.staticText_Autoconnect, 0, wx.ALL, 5 )
		
		choice_AutoconnectChoices = [ u"frn.titanix.net" ]
		self.choice_Autoconnect = wx.Choice( self.panel_Autoconnect, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choice_AutoconnectChoices, 0 )
		self.choice_Autoconnect.SetSelection( 0 )
		fgSizer21.Add( self.choice_Autoconnect, 0, wx.ALL, 5 )
		
		self.m_staticText15 = wx.StaticText( self.panel_Autoconnect, wx.ID_ANY, u"Room:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )
		fgSizer21.Add( self.m_staticText15, 0, wx.ALL, 5 )
		
		m_choice8Choices = []
		self.m_choice8 = wx.Choice( self.panel_Autoconnect, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice8Choices, 0 )
		self.m_choice8.SetSelection( 0 )
		fgSizer21.Add( self.m_choice8, 0, wx.ALL, 5 )
		
		
		self.panel_Autoconnect.SetSizer( fgSizer21 )
		self.panel_Autoconnect.Layout()
		fgSizer21.Fit( self.panel_Autoconnect )
		fgSizer14.Add( self.panel_Autoconnect, 1, wx.ALL, 5 )
		
		
		fgSizer18.Add( fgSizer14, 1, wx.EXPAND, 5 )
		
		fgSizer20 = wx.FlexGridSizer( 0, 4, 0, 0 )
		fgSizer20.AddGrowableCol( 3 )
		fgSizer20.SetFlexibleDirection( wx.BOTH )
		fgSizer20.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.button_OK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer20.Add( self.button_OK, 0, wx.ALL, 5 )
		
		self.button_Save = wx.Button( self, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer20.Add( self.button_Save, 0, wx.ALL, 5 )
		
		self.button_Cancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer20.Add( self.button_Cancel, 0, wx.ALL, 5 )
		
		self.m_checkBox2 = wx.CheckBox( self, wx.ID_ANY, u"Autosave on exit", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer20.Add( self.m_checkBox2, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		fgSizer18.Add( fgSizer20, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( fgSizer18 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.button_OK.Bind( wx.EVT_BUTTON, self.click_ok )
		self.button_Save.Bind( wx.EVT_BUTTON, self.click_save )
		self.button_Cancel.Bind( wx.EVT_BUTTON, self.click_cancel )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def click_ok( self, event ):
		event.Skip()
	
	def click_save( self, event ):
		event.Skip()
	
	def click_cancel( self, event ):
		event.Skip()
	

