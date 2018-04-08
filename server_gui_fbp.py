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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Pyham Server", pos = wx.DefaultPosition, size = wx.Size( 800,700 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		#self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		fgSizer_Main = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer_Main.AddGrowableCol( 0 )
		fgSizer_Main.AddGrowableRow( 0 )
		fgSizer_Main.SetFlexibleDirection( wx.BOTH )
		fgSizer_Main.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.scrolledWindow_Main = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.scrolledWindow_Main.SetScrollRate( 5, 5 )
		fgSizer_MainScrolled = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer_MainScrolled.AddGrowableCol( 1 )
		fgSizer_MainScrolled.AddGrowableRow( 0 )
		fgSizer_MainScrolled.SetFlexibleDirection( wx.BOTH )
		fgSizer_MainScrolled.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.panel_MainButtons = wx.Panel( self.scrolledWindow_Main, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER|wx.TAB_TRAVERSAL )
		fgSizer_MainButtons = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer_MainButtons.AddGrowableRow( 2 )
		fgSizer_MainButtons.SetFlexibleDirection( wx.BOTH )
		fgSizer_MainButtons.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.button_Quit = wx.Button( self.panel_MainButtons, wx.ID_ANY, u"Quit", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer_MainButtons.Add( self.button_Quit, 0, wx.ALL, 5 )
		
		self.button_Load = wx.Button( self.panel_MainButtons, wx.ID_ANY, u"Load", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer_MainButtons.Add( self.button_Load, 0, wx.ALL, 5 )
		
		self.button_Save = wx.Button( self.panel_MainButtons, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer_MainButtons.Add( self.button_Save, 0, wx.ALL, 5 )
		
		self.button_Settings = wx.Button( self.panel_MainButtons, wx.ID_ANY, u"Settings", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer_MainButtons.Add( self.button_Settings, 0, wx.ALL, 5 )
		
		self.button_Stats = wx.Button( self.panel_MainButtons, wx.ID_ANY, u"Stats", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer_MainButtons.Add( self.button_Stats, 0, wx.ALL, 5 )
		
		self.button_Log = wx.Button( self.panel_MainButtons, wx.ID_ANY, u"Log", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer_MainButtons.Add( self.button_Log, 0, wx.ALL, 5 )
		
		
		self.panel_MainButtons.SetSizer( fgSizer_MainButtons )
		self.panel_MainButtons.Layout()
		fgSizer_MainButtons.Fit( self.panel_MainButtons )
		fgSizer_MainScrolled.Add( self.panel_MainButtons, 1, wx.ALL|wx.EXPAND, 5 )
		
		fgSizer_ = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer_.AddGrowableCol( 0 )
		fgSizer_.AddGrowableRow( 0 )
		fgSizer_.SetFlexibleDirection( wx.BOTH )
		fgSizer_.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		fgSizer_Clients = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer_Clients.AddGrowableCol( 0 )
		fgSizer_Clients.AddGrowableRow( 1 )
		fgSizer_Clients.AddGrowableRow( 3 )
		fgSizer_Clients.AddGrowableRow( 5 )
		fgSizer_Clients.SetFlexibleDirection( wx.BOTH )
		fgSizer_Clients.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.staticText_Clients = wx.StaticText( self.scrolledWindow_Main, wx.ID_ANY, u"Connected clients:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_Clients.Wrap( -1 )
		fgSizer_Clients.Add( self.staticText_Clients, 0, wx.ALL, 5 )
		
		listBox_ClientsChoices = []
		self.listBox_Clients = wx.ListBox( self.scrolledWindow_Main, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, listBox_ClientsChoices, 0 )
		fgSizer_Clients.Add( self.listBox_Clients, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.staticText_Allowed = wx.StaticText( self.scrolledWindow_Main, wx.ID_ANY, u"Allowed clients:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_Allowed.Wrap( -1 )
		fgSizer_Clients.Add( self.staticText_Allowed, 0, wx.ALL, 5 )
		
		listBox_AllowedChoices = []
		self.listBox_Allowed = wx.ListBox( self.scrolledWindow_Main, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, listBox_AllowedChoices, 0 )
		fgSizer_Clients.Add( self.listBox_Allowed, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.staticText_Banned = wx.StaticText( self.scrolledWindow_Main, wx.ID_ANY, u"Banned clients:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_Banned.Wrap( -1 )
		fgSizer_Clients.Add( self.staticText_Banned, 0, wx.ALL, 5 )
		
		m_listBox_BannedChoices = []
		self.m_listBox_Banned = wx.ListBox( self.scrolledWindow_Main, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox_BannedChoices, 0 )
		fgSizer_Clients.Add( self.m_listBox_Banned, 0, wx.ALL|wx.EXPAND, 5 )
		
		fgSizer12 = wx.FlexGridSizer( 0, 4, 0, 0 )
		fgSizer12.AddGrowableCol( 0 )
		fgSizer12.AddGrowableCol( 1 )
		fgSizer12.SetFlexibleDirection( wx.BOTH )
		fgSizer12.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.textCtrl_Hostname = wx.TextCtrl( self.scrolledWindow_Main, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer12.Add( self.textCtrl_Hostname, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.textCtrl_Ip = wx.TextCtrl( self.scrolledWindow_Main, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer12.Add( self.textCtrl_Ip, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.button_Allow = wx.Button( self.scrolledWindow_Main, wx.ID_ANY, u"Allow", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer12.Add( self.button_Allow, 0, wx.ALL, 5 )
		
		self.button_Ban = wx.Button( self.scrolledWindow_Main, wx.ID_ANY, u"Ban", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer12.Add( self.button_Ban, 0, wx.ALL, 5 )
		
		
		fgSizer_Clients.Add( fgSizer12, 1, wx.EXPAND, 5 )
		
		
		fgSizer_.Add( fgSizer_Clients, 1, wx.EXPAND, 5 )
		
		fgSizer_Protocols = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer_Protocols.SetFlexibleDirection( wx.BOTH )
		fgSizer_Protocols.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.panel_Echolink = wx.Panel( self.scrolledWindow_Main, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.RAISED_BORDER|wx.TAB_TRAVERSAL )
		fgSizer_Echolink = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer_Echolink.SetFlexibleDirection( wx.BOTH )
		fgSizer_Echolink.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		fgSizer141 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer141.AddGrowableCol( 1 )
		fgSizer141.SetFlexibleDirection( wx.BOTH )
		fgSizer141.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.staticText_Echolink = wx.StaticText( self.panel_Echolink, wx.ID_ANY, u"Echolink", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_Echolink.Wrap( -1 )
		self.staticText_Echolink.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		
		fgSizer141.Add( self.staticText_Echolink, 0, wx.ALL, 5 )
		
		self.staticText_EcholinkState = wx.StaticText( self.panel_Echolink, wx.ID_ANY, u"Stopped", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_EcholinkState.Wrap( -1 )
		fgSizer141.Add( self.staticText_EcholinkState, 0, wx.ALL, 5 )
		
		self.staticText_EcholinkName = wx.StaticText( self.panel_Echolink, wx.ID_ANY, u"Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_EcholinkName.Wrap( -1 )
		fgSizer141.Add( self.staticText_EcholinkName, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.textCtrl_EcholinkName = wx.TextCtrl( self.panel_Echolink, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer141.Add( self.textCtrl_EcholinkName, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.staticText_EcholinkPort = wx.StaticText( self.panel_Echolink, wx.ID_ANY, u"Port", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_EcholinkPort.Wrap( -1 )
		fgSizer141.Add( self.staticText_EcholinkPort, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.textCtrl_EcholinkPort = wx.TextCtrl( self.panel_Echolink, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer141.Add( self.textCtrl_EcholinkPort, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		fgSizer_Echolink.Add( fgSizer141, 1, wx.EXPAND, 5 )
		
		fgSizer381 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer381.SetFlexibleDirection( wx.BOTH )
		fgSizer381.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.button_EcholinkApply = wx.Button( self.panel_Echolink, wx.ID_ANY, u"Apply", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer381.Add( self.button_EcholinkApply, 0, wx.ALL, 5 )
		
		self.button_EcholinkStart = wx.Button( self.panel_Echolink, wx.ID_ANY, u"Start", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer381.Add( self.button_EcholinkStart, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		
		fgSizer_Echolink.Add( fgSizer381, 1, wx.EXPAND, 5 )
		
		
		self.panel_Echolink.SetSizer( fgSizer_Echolink )
		self.panel_Echolink.Layout()
		fgSizer_Echolink.Fit( self.panel_Echolink )
		fgSizer_Protocols.Add( self.panel_Echolink, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.panel_Eqso = wx.Panel( self.scrolledWindow_Main, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.RAISED_BORDER|wx.TAB_TRAVERSAL )
		fgSizer_Eqso = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer_Eqso.SetFlexibleDirection( wx.BOTH )
		fgSizer_Eqso.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		fgSizer1413 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1413.AddGrowableCol( 1 )
		fgSizer1413.SetFlexibleDirection( wx.BOTH )
		fgSizer1413.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.staticText_Eqso = wx.StaticText( self.panel_Eqso, wx.ID_ANY, u"eQSO", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_Eqso.Wrap( -1 )
		self.staticText_Eqso.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		
		fgSizer1413.Add( self.staticText_Eqso, 0, wx.ALL, 5 )
		
		self.staticText_EqsoState = wx.StaticText( self.panel_Eqso, wx.ID_ANY, u"Stopped", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_EqsoState.Wrap( -1 )
		fgSizer1413.Add( self.staticText_EqsoState, 0, wx.ALL, 5 )
		
		self.staticText_EqsoName = wx.StaticText( self.panel_Eqso, wx.ID_ANY, u"Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_EqsoName.Wrap( -1 )
		fgSizer1413.Add( self.staticText_EqsoName, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.textCtrl_EqsoName = wx.TextCtrl( self.panel_Eqso, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1413.Add( self.textCtrl_EqsoName, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.staticText_EqsoPort = wx.StaticText( self.panel_Eqso, wx.ID_ANY, u"Port", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_EqsoPort.Wrap( -1 )
		fgSizer1413.Add( self.staticText_EqsoPort, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.textCtrl_EqsoPort = wx.TextCtrl( self.panel_Eqso, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1413.Add( self.textCtrl_EqsoPort, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		fgSizer_Eqso.Add( fgSizer1413, 1, wx.EXPAND, 5 )
		
		fgSizer38 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer38.SetFlexibleDirection( wx.BOTH )
		fgSizer38.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.button_EqsoApply = wx.Button( self.panel_Eqso, wx.ID_ANY, u"Apply", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer38.Add( self.button_EqsoApply, 0, wx.ALL, 5 )
		
		self.button_EqsoStart = wx.Button( self.panel_Eqso, wx.ID_ANY, u"Start", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer38.Add( self.button_EqsoStart, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		
		fgSizer_Eqso.Add( fgSizer38, 1, wx.EXPAND, 5 )
		
		
		self.panel_Eqso.SetSizer( fgSizer_Eqso )
		self.panel_Eqso.Layout()
		fgSizer_Eqso.Fit( self.panel_Eqso )
		fgSizer_Protocols.Add( self.panel_Eqso, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.panel_Frn = wx.Panel( self.scrolledWindow_Main, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.RAISED_BORDER|wx.TAB_TRAVERSAL )
		fgSizer_Frn = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer_Frn.SetFlexibleDirection( wx.BOTH )
		fgSizer_Frn.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		fgSizer1411 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1411.AddGrowableCol( 1 )
		fgSizer1411.SetFlexibleDirection( wx.BOTH )
		fgSizer1411.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.staticText_Frn = wx.StaticText( self.panel_Frn, wx.ID_ANY, u"FRN", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_Frn.Wrap( -1 )
		self.staticText_Frn.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		
		fgSizer1411.Add( self.staticText_Frn, 0, wx.ALL, 5 )
		
		self.staticText_FrnState = wx.StaticText( self.panel_Frn, wx.ID_ANY, u"Stopped", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_FrnState.Wrap( -1 )
		fgSizer1411.Add( self.staticText_FrnState, 0, wx.ALL, 5 )
		
		self.staticText_FrnName = wx.StaticText( self.panel_Frn, wx.ID_ANY, u"Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_FrnName.Wrap( -1 )
		fgSizer1411.Add( self.staticText_FrnName, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.textCtrl_FrnName = wx.TextCtrl( self.panel_Frn, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1411.Add( self.textCtrl_FrnName, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.staticText_FrnPort = wx.StaticText( self.panel_Frn, wx.ID_ANY, u"Port", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_FrnPort.Wrap( -1 )
		fgSizer1411.Add( self.staticText_FrnPort, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.textCtrl_FrnPort = wx.TextCtrl( self.panel_Frn, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1411.Add( self.textCtrl_FrnPort, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		fgSizer_Frn.Add( fgSizer1411, 1, wx.EXPAND, 5 )
		
		fgSizer382 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer382.SetFlexibleDirection( wx.BOTH )
		fgSizer382.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.button_FrnApply = wx.Button( self.panel_Frn, wx.ID_ANY, u"Apply", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer382.Add( self.button_FrnApply, 0, wx.ALL, 5 )
		
		self.button_FrnStart = wx.Button( self.panel_Frn, wx.ID_ANY, u"Start", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer382.Add( self.button_FrnStart, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		
		fgSizer_Frn.Add( fgSizer382, 1, wx.EXPAND, 5 )
		
		
		self.panel_Frn.SetSizer( fgSizer_Frn )
		self.panel_Frn.Layout()
		fgSizer_Frn.Fit( self.panel_Frn )
		fgSizer_Protocols.Add( self.panel_Frn, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.Panel_Pyhamp = wx.Panel( self.scrolledWindow_Main, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.RAISED_BORDER|wx.TAB_TRAVERSAL )
		fgSizer_Pyhamp = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer_Pyhamp.SetFlexibleDirection( wx.BOTH )
		fgSizer_Pyhamp.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		fgSizer1412 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1412.AddGrowableCol( 1 )
		fgSizer1412.SetFlexibleDirection( wx.BOTH )
		fgSizer1412.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.staticText_Pyhamp = wx.StaticText( self.Panel_Pyhamp, wx.ID_ANY, u"pyhamp", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_Pyhamp.Wrap( -1 )
		self.staticText_Pyhamp.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		
		fgSizer1412.Add( self.staticText_Pyhamp, 0, wx.ALL, 5 )
		
		self.staticText_PyhampState = wx.StaticText( self.Panel_Pyhamp, wx.ID_ANY, u"Stopped", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_PyhampState.Wrap( -1 )
		fgSizer1412.Add( self.staticText_PyhampState, 0, wx.ALL, 5 )
		
		self.staticText_PyhampName = wx.StaticText( self.Panel_Pyhamp, wx.ID_ANY, u"Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_PyhampName.Wrap( -1 )
		fgSizer1412.Add( self.staticText_PyhampName, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.textCtrl_PyhampName = wx.TextCtrl( self.Panel_Pyhamp, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1412.Add( self.textCtrl_PyhampName, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.staticText_PyhampPort = wx.StaticText( self.Panel_Pyhamp, wx.ID_ANY, u"Port", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_PyhampPort.Wrap( -1 )
		fgSizer1412.Add( self.staticText_PyhampPort, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.textCtrl_PyhampPort = wx.TextCtrl( self.Panel_Pyhamp, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1412.Add( self.textCtrl_PyhampPort, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		fgSizer_Pyhamp.Add( fgSizer1412, 1, wx.EXPAND, 5 )
		
		fgSizer383 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer383.SetFlexibleDirection( wx.BOTH )
		fgSizer383.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.button_PyhampApply = wx.Button( self.Panel_Pyhamp, wx.ID_ANY, u"Apply", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer383.Add( self.button_PyhampApply, 0, wx.ALL, 5 )
		
		self.button_PyhampStart = wx.Button( self.Panel_Pyhamp, wx.ID_ANY, u"Start", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer383.Add( self.button_PyhampStart, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		
		fgSizer_Pyhamp.Add( fgSizer383, 1, wx.EXPAND, 5 )
		
		
		self.Panel_Pyhamp.SetSizer( fgSizer_Pyhamp )
		self.Panel_Pyhamp.Layout()
		fgSizer_Pyhamp.Fit( self.Panel_Pyhamp )
		fgSizer_Protocols.Add( self.Panel_Pyhamp, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		fgSizer_.Add( fgSizer_Protocols, 1, wx.EXPAND, 5 )
		
		
		fgSizer_MainScrolled.Add( fgSizer_, 1, wx.EXPAND, 5 )
		
		
		self.scrolledWindow_Main.SetSizer( fgSizer_MainScrolled )
		self.scrolledWindow_Main.Layout()
		fgSizer_MainScrolled.Fit( self.scrolledWindow_Main )
		fgSizer_Main.Add( self.scrolledWindow_Main, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( fgSizer_Main )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.button_Quit.Bind( wx.EVT_BUTTON, self.click_quit )
		self.button_Load.Bind( wx.EVT_BUTTON, self.click_load )
		self.button_Save.Bind( wx.EVT_BUTTON, self.click_save )
		self.button_Settings.Bind( wx.EVT_BUTTON, self.click_settings )
		self.button_Stats.Bind( wx.EVT_BUTTON, self.click_stats )
		self.button_Log.Bind( wx.EVT_BUTTON, self.click_log )
		self.button_Allow.Bind( wx.EVT_BUTTON, self.click_allow )
		self.button_Ban.Bind( wx.EVT_BUTTON, self.click_ban )
		self.button_EcholinkApply.Bind( wx.EVT_BUTTON, self.click_echolink_apply )
		self.button_EcholinkStart.Bind( wx.EVT_BUTTON, self.click_echolink_start )
		self.button_EqsoApply.Bind( wx.EVT_BUTTON, self.click_eqso_apply )
		self.button_EqsoStart.Bind( wx.EVT_BUTTON, self.click_eqso_start )
		self.button_FrnApply.Bind( wx.EVT_BUTTON, self.click_frn_apply )
		self.button_FrnStart.Bind( wx.EVT_BUTTON, self.click_frn_start )
		self.button_PyhampApply.Bind( wx.EVT_BUTTON, self.click_pyhamp_apply )
		self.button_PyhampStart.Bind( wx.EVT_BUTTON, self.click_pyhamp_start )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def click_quit( self, event ):
		event.Skip()
	
	def click_load( self, event ):
		event.Skip()
	
	def click_save( self, event ):
		event.Skip()
	
	def click_settings( self, event ):
		event.Skip()
	
	def click_stats( self, event ):
		event.Skip()
	
	def click_log( self, event ):
		event.Skip()
	
	def click_allow( self, event ):
		event.Skip()
	
	def click_ban( self, event ):
		event.Skip()
	
	def click_echolink_apply( self, event ):
		event.Skip()
	
	def click_echolink_start( self, event ):
		event.Skip()
	
	def click_eqso_apply( self, event ):
		event.Skip()
	
	def click_eqso_start( self, event ):
		event.Skip()
	
	def click_frn_apply( self, event ):
		event.Skip()
	
	def click_frn_start( self, event ):
		event.Skip()
	
	def click_pyhamp_apply( self, event ):
		event.Skip()
	
	def click_pyhamp_start( self, event ):
		event.Skip()
	

###########################################################################
## Class FrameSettings
###########################################################################

class FrameSettings ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Pyham Server - Settings", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		#self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		fgSizer20 = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer20.AddGrowableCol( 0 )
		fgSizer20.AddGrowableRow( 0 )
		fgSizer20.SetFlexibleDirection( wx.BOTH )
		fgSizer20.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_scrolledWindow2 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow2.SetScrollRate( 5, 5 )
		fgSizer21 = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer21.AddGrowableRow( 0 )
		fgSizer21.SetFlexibleDirection( wx.BOTH )
		fgSizer21.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_panel7 = wx.Panel( self.m_scrolledWindow2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL )
		fgSizer27 = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer27.SetFlexibleDirection( wx.BOTH )
		fgSizer27.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText18 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"PTT trigger", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )
		self.m_staticText18.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		
		fgSizer27.Add( self.m_staticText18, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		m_choice9Choices = [ u"COM1", u"LPT1", u"USB serial" ]
		self.m_choice9 = wx.Choice( self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice9Choices, 0 )
		self.m_choice9.SetSelection( 0 )
		fgSizer27.Add( self.m_choice9, 0, wx.ALL, 5 )
		
		
		self.m_panel7.SetSizer( fgSizer27 )
		self.m_panel7.Layout()
		fgSizer27.Fit( self.m_panel7 )
		fgSizer21.Add( self.m_panel7, 0, wx.ALL, 5 )
		
		fgSizer_BottomWidgets = wx.FlexGridSizer( 0, 4, 0, 0 )
		fgSizer_BottomWidgets.AddGrowableCol( 3 )
		fgSizer_BottomWidgets.SetFlexibleDirection( wx.BOTH )
		fgSizer_BottomWidgets.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.button_OK = wx.Button( self.m_scrolledWindow2, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer_BottomWidgets.Add( self.button_OK, 0, wx.ALL, 5 )
		
		self.button_Save = wx.Button( self.m_scrolledWindow2, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer_BottomWidgets.Add( self.button_Save, 0, wx.ALL, 5 )
		
		self.button_Cancel = wx.Button( self.m_scrolledWindow2, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer_BottomWidgets.Add( self.button_Cancel, 0, wx.ALL, 5 )
		
		self.checkBox_Autosave = wx.CheckBox( self.m_scrolledWindow2, wx.ID_ANY, u"Autosave on quit", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer_BottomWidgets.Add( self.checkBox_Autosave, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		fgSizer21.Add( fgSizer_BottomWidgets, 1, wx.EXPAND, 5 )
		
		
		self.m_scrolledWindow2.SetSizer( fgSizer21 )
		self.m_scrolledWindow2.Layout()
		fgSizer21.Fit( self.m_scrolledWindow2 )
		fgSizer20.Add( self.m_scrolledWindow2, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( fgSizer20 )
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
	

