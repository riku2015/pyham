# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Aug  8 2018)
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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Pyham Server 0.016", pos = wx.DefaultPosition, size = wx.Size( 800,700 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		fgSizer_Main = wx.FlexGridSizer( 0, 1, 0, 0 )
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
		
		self.panel_MainButtons = wx.Panel( self.scrolledWindow_Main, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL|wx.BORDER_SUNKEN )
		fgSizer_MainButtons = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer_MainButtons.SetFlexibleDirection( wx.BOTH )
		fgSizer_MainButtons.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.button_Settings = wx.Button( self.panel_MainButtons, wx.ID_ANY, u"Settings", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer_MainButtons.Add( self.button_Settings, 0, wx.ALL, 5 )
		
		self.button_Stats = wx.Button( self.panel_MainButtons, wx.ID_ANY, u"Stats", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer_MainButtons.Add( self.button_Stats, 0, wx.ALL, 5 )
		
		self.button_Quit = wx.Button( self.panel_MainButtons, wx.ID_ANY, u"Quit", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer_MainButtons.Add( self.button_Quit, 0, wx.ALL, 5 )
		
		
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
		
		self.textCtrl_IP = wx.TextCtrl( self.scrolledWindow_Main, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer12.Add( self.textCtrl_IP, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.button_Ban = wx.Button( self.scrolledWindow_Main, wx.ID_ANY, u"Ban / Unban", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer12.Add( self.button_Ban, 0, wx.ALL, 5 )
		
		
		fgSizer_Clients.Add( fgSizer12, 1, wx.EXPAND, 5 )
		
		
		fgSizer_.Add( fgSizer_Clients, 1, wx.EXPAND, 5 )
		
		fgSizer_Protocols = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer_Protocols.SetFlexibleDirection( wx.BOTH )
		fgSizer_Protocols.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.panel_Echolink = wx.Panel( self.scrolledWindow_Main, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL|wx.BORDER_RAISED )
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
		self.button_EcholinkApply.Enable( False )
		
		fgSizer381.Add( self.button_EcholinkApply, 0, wx.ALL, 5 )
		
		self.button_EcholinkStart = wx.Button( self.panel_Echolink, wx.ID_ANY, u"Start", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer381.Add( self.button_EcholinkStart, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		
		fgSizer_Echolink.Add( fgSizer381, 1, wx.EXPAND, 5 )
		
		
		self.panel_Echolink.SetSizer( fgSizer_Echolink )
		self.panel_Echolink.Layout()
		fgSizer_Echolink.Fit( self.panel_Echolink )
		fgSizer_Protocols.Add( self.panel_Echolink, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.panel_Eqso = wx.Panel( self.scrolledWindow_Main, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL|wx.BORDER_RAISED )
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
		self.button_EqsoApply.Enable( False )
		
		fgSizer38.Add( self.button_EqsoApply, 0, wx.ALL, 5 )
		
		self.button_EqsoStart = wx.Button( self.panel_Eqso, wx.ID_ANY, u"Start", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer38.Add( self.button_EqsoStart, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		
		fgSizer_Eqso.Add( fgSizer38, 1, wx.EXPAND, 5 )
		
		
		self.panel_Eqso.SetSizer( fgSizer_Eqso )
		self.panel_Eqso.Layout()
		fgSizer_Eqso.Fit( self.panel_Eqso )
		fgSizer_Protocols.Add( self.panel_Eqso, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.panel_Frn = wx.Panel( self.scrolledWindow_Main, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL|wx.BORDER_RAISED )
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
		self.button_FrnApply.Enable( False )
		
		fgSizer382.Add( self.button_FrnApply, 0, wx.ALL, 5 )
		
		self.button_FrnStart = wx.Button( self.panel_Frn, wx.ID_ANY, u"Start", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer382.Add( self.button_FrnStart, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		
		fgSizer_Frn.Add( fgSizer382, 1, wx.EXPAND, 5 )
		
		
		self.panel_Frn.SetSizer( fgSizer_Frn )
		self.panel_Frn.Layout()
		fgSizer_Frn.Fit( self.panel_Frn )
		fgSizer_Protocols.Add( self.panel_Frn, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.Panel_Pyhamp = wx.Panel( self.scrolledWindow_Main, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL|wx.BORDER_RAISED )
		fgSizer_Pyhamp = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer_Pyhamp.SetFlexibleDirection( wx.BOTH )
		fgSizer_Pyhamp.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		fgSizer1412 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1412.AddGrowableCol( 1 )
		fgSizer1412.SetFlexibleDirection( wx.BOTH )
		fgSizer1412.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.staticText_Pyham = wx.StaticText( self.Panel_Pyhamp, wx.ID_ANY, u"Pyham", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_Pyham.Wrap( -1 )
		
		self.staticText_Pyham.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		
		fgSizer1412.Add( self.staticText_Pyham, 0, wx.ALL, 5 )
		
		self.staticText_PyhamState = wx.StaticText( self.Panel_Pyhamp, wx.ID_ANY, u"Stopped", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_PyhamState.Wrap( -1 )
		
		fgSizer1412.Add( self.staticText_PyhamState, 0, wx.ALL, 5 )
		
		self.staticText_PyhamName = wx.StaticText( self.Panel_Pyhamp, wx.ID_ANY, u"Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_PyhamName.Wrap( -1 )
		
		fgSizer1412.Add( self.staticText_PyhamName, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.textCtrl_PyhamName = wx.TextCtrl( self.Panel_Pyhamp, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1412.Add( self.textCtrl_PyhamName, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.staticText_PyhamPort = wx.StaticText( self.Panel_Pyhamp, wx.ID_ANY, u"Port", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_PyhamPort.Wrap( -1 )
		
		fgSizer1412.Add( self.staticText_PyhamPort, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.textCtrl_PyhamPort = wx.TextCtrl( self.Panel_Pyhamp, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1412.Add( self.textCtrl_PyhamPort, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		fgSizer_Pyhamp.Add( fgSizer1412, 1, wx.EXPAND, 5 )
		
		fgSizer383 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer383.SetFlexibleDirection( wx.BOTH )
		fgSizer383.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.button_PyhamApply = wx.Button( self.Panel_Pyhamp, wx.ID_ANY, u"Apply", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.button_PyhamApply.Enable( False )
		
		fgSizer383.Add( self.button_PyhamApply, 0, wx.ALL, 5 )
		
		self.button_PyhamStart = wx.Button( self.Panel_Pyhamp, wx.ID_ANY, u"Start", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer383.Add( self.button_PyhamStart, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		
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
		self.button_Settings.Bind( wx.EVT_BUTTON, self.click_settings )
		self.button_Stats.Bind( wx.EVT_BUTTON, self.click_stats )
		self.button_Quit.Bind( wx.EVT_BUTTON, self.click_quit )
		self.button_Ban.Bind( wx.EVT_BUTTON, self.click_ban )
		self.textCtrl_EcholinkName.Bind( wx.EVT_TEXT, self.text_Echolink )
		self.textCtrl_EcholinkPort.Bind( wx.EVT_TEXT, self.text_Echolink )
		self.button_EcholinkApply.Bind( wx.EVT_BUTTON, self.click_echolink_apply )
		self.button_EcholinkStart.Bind( wx.EVT_BUTTON, self.click_echolink_start )
		self.textCtrl_EqsoName.Bind( wx.EVT_TEXT, self.text_Eqso )
		self.textCtrl_EqsoPort.Bind( wx.EVT_TEXT, self.text_Eqso )
		self.button_EqsoApply.Bind( wx.EVT_BUTTON, self.click_eqso_apply )
		self.button_EqsoStart.Bind( wx.EVT_BUTTON, self.click_eqso_start )
		self.textCtrl_FrnName.Bind( wx.EVT_TEXT, self.text_Frn )
		self.textCtrl_FrnPort.Bind( wx.EVT_TEXT, self.text_Frn )
		self.button_FrnApply.Bind( wx.EVT_BUTTON, self.click_frn_apply )
		self.button_FrnStart.Bind( wx.EVT_BUTTON, self.click_frn_start )
		self.textCtrl_PyhamName.Bind( wx.EVT_TEXT, self.text_Pyham )
		self.textCtrl_PyhamPort.Bind( wx.EVT_TEXT, self.text_Pyham )
		self.button_PyhamApply.Bind( wx.EVT_BUTTON, self.click_pyham_apply )
		self.button_PyhamStart.Bind( wx.EVT_BUTTON, self.click_pyham_start )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def click_settings( self, event ):
		event.Skip()
	
	def click_stats( self, event ):
		event.Skip()
	
	def click_quit( self, event ):
		event.Skip()
	
	def click_ban( self, event ):
		event.Skip()
	
	def text_Echolink( self, event ):
		event.Skip()
	
	
	def click_echolink_apply( self, event ):
		event.Skip()
	
	def click_echolink_start( self, event ):
		event.Skip()
	
	def text_Eqso( self, event ):
		event.Skip()
	
	
	def click_eqso_apply( self, event ):
		event.Skip()
	
	def click_eqso_start( self, event ):
		event.Skip()
	
	def text_Frn( self, event ):
		event.Skip()
	
	
	def click_frn_apply( self, event ):
		event.Skip()
	
	def click_frn_start( self, event ):
		event.Skip()
	
	def text_Pyham( self, event ):
		event.Skip()
	
	
	def click_pyham_apply( self, event ):
		event.Skip()
	
	def click_pyham_start( self, event ):
		event.Skip()
	

###########################################################################
## Class FrameSettings
###########################################################################

class FrameSettings ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Pyham Server - Settings", pos = wx.DefaultPosition, size = wx.Size( 520,720 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		fgSizer_Main = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer_Main.AddGrowableCol( 0 )
		fgSizer_Main.AddGrowableRow( 0 )
		fgSizer_Main.SetFlexibleDirection( wx.BOTH )
		fgSizer_Main.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.scrolledWindow_Main = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.scrolledWindow_Main.SetScrollRate( 5, 5 )
		fgSizer21 = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer21.AddGrowableCol( 0 )
		fgSizer21.AddGrowableRow( 1 )
		fgSizer21.SetFlexibleDirection( wx.BOTH )
		fgSizer21.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		fgSizer24 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer24.AddGrowableCol( 0 )
		fgSizer24.AddGrowableCol( 1 )
		fgSizer24.SetFlexibleDirection( wx.BOTH )
		fgSizer24.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_panel7 = wx.Panel( self.scrolledWindow_Main, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL|wx.BORDER_SIMPLE )
		fgSizer32 = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer32.AddGrowableCol( 0 )
		fgSizer32.SetFlexibleDirection( wx.BOTH )
		fgSizer32.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.staticText_Echolink = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Echolink", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_Echolink.Wrap( -1 )
		
		self.staticText_Echolink.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		
		fgSizer32.Add( self.staticText_Echolink, 0, wx.ALL, 5 )
		
		fgSizer141 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer141.AddGrowableCol( 1 )
		fgSizer141.SetFlexibleDirection( wx.BOTH )
		fgSizer141.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.staticText_EcholinkName = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_EcholinkName.Wrap( -1 )
		
		fgSizer141.Add( self.staticText_EcholinkName, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.textCtrl_EcholinkName = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer141.Add( self.textCtrl_EcholinkName, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.staticText_EcholinkPort = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Port", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_EcholinkPort.Wrap( -1 )
		
		fgSizer141.Add( self.staticText_EcholinkPort, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.textCtrl_EcholinkPort = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer141.Add( self.textCtrl_EcholinkPort, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		fgSizer32.Add( fgSizer141, 1, wx.EXPAND, 5 )
		
		self.checkBox_EcholinkAutostart = wx.CheckBox( self.m_panel7, wx.ID_ANY, u"Autostart", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer32.Add( self.checkBox_EcholinkAutostart, 0, wx.ALL, 5 )
		
		
		self.m_panel7.SetSizer( fgSizer32 )
		self.m_panel7.Layout()
		fgSizer32.Fit( self.m_panel7 )
		fgSizer24.Add( self.m_panel7, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_panel71 = wx.Panel( self.scrolledWindow_Main, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL|wx.BORDER_SIMPLE )
		fgSizer251 = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer251.AddGrowableCol( 0 )
		fgSizer251.SetFlexibleDirection( wx.BOTH )
		fgSizer251.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText211 = wx.StaticText( self.m_panel71, wx.ID_ANY, u"eQSO", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText211.Wrap( -1 )
		
		self.m_staticText211.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		
		fgSizer251.Add( self.m_staticText211, 0, wx.ALL, 5 )
		
		fgSizer1413 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1413.AddGrowableCol( 1 )
		fgSizer1413.SetFlexibleDirection( wx.BOTH )
		fgSizer1413.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.staticText_EqsoName = wx.StaticText( self.m_panel71, wx.ID_ANY, u"Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_EqsoName.Wrap( -1 )
		
		fgSizer1413.Add( self.staticText_EqsoName, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.textCtrl_EqsoName = wx.TextCtrl( self.m_panel71, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1413.Add( self.textCtrl_EqsoName, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.staticText_EqsoPort = wx.StaticText( self.m_panel71, wx.ID_ANY, u"Port", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_EqsoPort.Wrap( -1 )
		
		fgSizer1413.Add( self.staticText_EqsoPort, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.textCtrl_EqsoPort = wx.TextCtrl( self.m_panel71, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1413.Add( self.textCtrl_EqsoPort, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		fgSizer251.Add( fgSizer1413, 1, wx.EXPAND, 5 )
		
		self.checkBox_EqsoAutostart = wx.CheckBox( self.m_panel71, wx.ID_ANY, u"Autostart", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer251.Add( self.checkBox_EqsoAutostart, 0, wx.ALL, 5 )
		
		
		self.m_panel71.SetSizer( fgSizer251 )
		self.m_panel71.Layout()
		fgSizer251.Fit( self.m_panel71 )
		fgSizer24.Add( self.m_panel71, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel711 = wx.Panel( self.scrolledWindow_Main, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL|wx.BORDER_SIMPLE )
		fgSizer2511 = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer2511.AddGrowableCol( 0 )
		fgSizer2511.SetFlexibleDirection( wx.BOTH )
		fgSizer2511.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText2111 = wx.StaticText( self.m_panel711, wx.ID_ANY, u"FRN", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2111.Wrap( -1 )
		
		self.m_staticText2111.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		
		fgSizer2511.Add( self.m_staticText2111, 0, wx.ALL, 5 )
		
		fgSizer1411 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1411.AddGrowableCol( 1 )
		fgSizer1411.SetFlexibleDirection( wx.BOTH )
		fgSizer1411.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.staticText_FrnName = wx.StaticText( self.m_panel711, wx.ID_ANY, u"Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_FrnName.Wrap( -1 )
		
		fgSizer1411.Add( self.staticText_FrnName, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.textCtrl_FrnName = wx.TextCtrl( self.m_panel711, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1411.Add( self.textCtrl_FrnName, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.staticText_FrnPort = wx.StaticText( self.m_panel711, wx.ID_ANY, u"Port", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_FrnPort.Wrap( -1 )
		
		fgSizer1411.Add( self.staticText_FrnPort, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.textCtrl_FrnPort = wx.TextCtrl( self.m_panel711, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1411.Add( self.textCtrl_FrnPort, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		fgSizer2511.Add( fgSizer1411, 1, wx.EXPAND, 5 )
		
		self.checkBox_FrnAutostart = wx.CheckBox( self.m_panel711, wx.ID_ANY, u"Autostart", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2511.Add( self.checkBox_FrnAutostart, 0, wx.ALL, 5 )
		
		
		self.m_panel711.SetSizer( fgSizer2511 )
		self.m_panel711.Layout()
		fgSizer2511.Fit( self.m_panel711 )
		fgSizer24.Add( self.m_panel711, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel712 = wx.Panel( self.scrolledWindow_Main, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL|wx.BORDER_SIMPLE )
		fgSizer2512 = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer2512.AddGrowableCol( 0 )
		fgSizer2512.SetFlexibleDirection( wx.BOTH )
		fgSizer2512.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.staticText_Pyham = wx.StaticText( self.m_panel712, wx.ID_ANY, u"Pyham", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_Pyham.Wrap( -1 )
		
		self.staticText_Pyham.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		
		fgSizer2512.Add( self.staticText_Pyham, 0, wx.ALL, 5 )
		
		fgSizer1412 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1412.AddGrowableCol( 1 )
		fgSizer1412.SetFlexibleDirection( wx.BOTH )
		fgSizer1412.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.staticText_PyhampName = wx.StaticText( self.m_panel712, wx.ID_ANY, u"Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_PyhampName.Wrap( -1 )
		
		fgSizer1412.Add( self.staticText_PyhampName, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.textCtrl_PyhamName = wx.TextCtrl( self.m_panel712, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1412.Add( self.textCtrl_PyhamName, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.staticText_PyhampPort = wx.StaticText( self.m_panel712, wx.ID_ANY, u"Port", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_PyhampPort.Wrap( -1 )
		
		fgSizer1412.Add( self.staticText_PyhampPort, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.textCtrl_PyhamPort = wx.TextCtrl( self.m_panel712, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1412.Add( self.textCtrl_PyhamPort, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		fgSizer2512.Add( fgSizer1412, 1, wx.EXPAND, 5 )
		
		self.checkBox_PyhamAutostart = wx.CheckBox( self.m_panel712, wx.ID_ANY, u"Autostart", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2512.Add( self.checkBox_PyhamAutostart, 0, wx.ALL, 5 )
		
		
		self.m_panel712.SetSizer( fgSizer2512 )
		self.m_panel712.Layout()
		fgSizer2512.Fit( self.m_panel712 )
		fgSizer24.Add( self.m_panel712, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		fgSizer21.Add( fgSizer24, 1, wx.EXPAND, 5 )
		
		fgSizer36 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer36.AddGrowableCol( 1 )
		fgSizer36.AddGrowableRow( 0 )
		fgSizer36.SetFlexibleDirection( wx.BOTH )
		fgSizer36.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		fgSizer46 = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer46.SetFlexibleDirection( wx.BOTH )
		fgSizer46.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.panel_Devices = wx.Panel( self.scrolledWindow_Main, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL|wx.BORDER_SIMPLE )
		fgSizer_Devices = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer_Devices.SetFlexibleDirection( wx.BOTH )
		fgSizer_Devices.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.staticText_Audio = wx.StaticText( self.panel_Devices, wx.ID_ANY, u"Audio device defaults", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_Audio.Wrap( -1 )
		
		self.staticText_Audio.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		
		fgSizer_Devices.Add( self.staticText_Audio, 0, wx.ALL, 5 )
		
		self.staticText_Speaker = wx.StaticText( self.panel_Devices, wx.ID_ANY, u"Speaker device:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_Speaker.Wrap( -1 )
		
		fgSizer_Devices.Add( self.staticText_Speaker, 0, wx.ALL, 5 )
		
		choice_SpeakerChoices = [ u"Default", u"Spk 1", u"Spk 2" ]
		self.choice_Speaker = wx.Choice( self.panel_Devices, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choice_SpeakerChoices, 0 )
		self.choice_Speaker.SetSelection( 0 )
		fgSizer_Devices.Add( self.choice_Speaker, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText20 = wx.StaticText( self.panel_Devices, wx.ID_ANY, u"Speaker volume:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )
		
		fgSizer_Devices.Add( self.m_staticText20, 0, wx.ALL, 5 )
		
		self.spinCtrl_Speaker = wx.SpinCtrl( self.panel_Devices, wx.ID_ANY, u"50", wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 100, 50 )
		fgSizer_Devices.Add( self.spinCtrl_Speaker, 0, wx.ALL, 5 )
		
		self.m_staticline3 = wx.StaticLine( self.panel_Devices, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer_Devices.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.staticText_Mic = wx.StaticText( self.panel_Devices, wx.ID_ANY, u"Mic device:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_Mic.Wrap( -1 )
		
		fgSizer_Devices.Add( self.staticText_Mic, 0, wx.ALL, 5 )
		
		choice_MicChoices = [ u"Default", u"Mic 1", u"Mic 2" ]
		self.choice_Mic = wx.Choice( self.panel_Devices, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choice_MicChoices, 0 )
		self.choice_Mic.SetSelection( 0 )
		fgSizer_Devices.Add( self.choice_Mic, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText21 = wx.StaticText( self.panel_Devices, wx.ID_ANY, u"Mic volume:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )
		
		fgSizer_Devices.Add( self.m_staticText21, 0, wx.ALL, 5 )
		
		self.spinCtrl_Mic = wx.SpinCtrl( self.panel_Devices, wx.ID_ANY, u"50", wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 100, 50 )
		fgSizer_Devices.Add( self.spinCtrl_Mic, 0, wx.ALL, 5 )
		
		
		self.panel_Devices.SetSizer( fgSizer_Devices )
		self.panel_Devices.Layout()
		fgSizer_Devices.Fit( self.panel_Devices )
		fgSizer46.Add( self.panel_Devices, 1, wx.ALL, 5 )
		
		self.panel_Overlap = wx.Panel( self.scrolledWindow_Main, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_SIMPLE|wx.TAB_TRAVERSAL )
		fgSizer47 = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer47.AddGrowableCol( 0 )
		fgSizer47.SetFlexibleDirection( wx.BOTH )
		fgSizer47.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText51 = wx.StaticText( self.panel_Overlap, wx.ID_ANY, u"When clients overlap:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )
		
		fgSizer47.Add( self.m_staticText51, 0, wx.ALL, 5 )
		
		choice_OverlapChoices = [ u"Discard latecomers", u"Mix sounds", u"Queue" ]
		self.choice_Overlap = wx.Choice( self.panel_Overlap, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choice_OverlapChoices, 0 )
		self.choice_Overlap.SetSelection( 0 )
		fgSizer47.Add( self.choice_Overlap, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.panel_Overlap.SetSizer( fgSizer47 )
		self.panel_Overlap.Layout()
		fgSizer47.Fit( self.panel_Overlap )
		fgSizer46.Add( self.panel_Overlap, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		fgSizer36.Add( fgSizer46, 1, wx.EXPAND, 5 )
		
		fgSizer38 = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer38.AddGrowableCol( 0 )
		fgSizer38.AddGrowableRow( 2 )
		fgSizer38.SetFlexibleDirection( wx.BOTH )
		fgSizer38.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		fgSizer43 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer43.AddGrowableCol( 1 )
		fgSizer43.SetFlexibleDirection( wx.BOTH )
		fgSizer43.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.panel_Ptt = wx.Panel( self.scrolledWindow_Main, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL|wx.BORDER_SIMPLE )
		fgSizer_Ptt = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer_Ptt.SetFlexibleDirection( wx.BOTH )
		fgSizer_Ptt.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText18 = wx.StaticText( self.panel_Ptt, wx.ID_ANY, u"PTT trigger", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )
		
		self.m_staticText18.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		
		fgSizer_Ptt.Add( self.m_staticText18, 0, wx.ALL, 5 )
		
		m_choice9Choices = [ u"COM1", u"LPT1", u"USB serial" ]
		self.m_choice9 = wx.Choice( self.panel_Ptt, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice9Choices, 0 )
		self.m_choice9.SetSelection( 0 )
		fgSizer_Ptt.Add( self.m_choice9, 0, wx.ALL, 5 )
		
		
		self.panel_Ptt.SetSizer( fgSizer_Ptt )
		self.panel_Ptt.Layout()
		fgSizer_Ptt.Fit( self.panel_Ptt )
		fgSizer43.Add( self.panel_Ptt, 0, wx.ALL, 5 )
		
		self.m_panel13 = wx.Panel( self.scrolledWindow_Main, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_SIMPLE|wx.TAB_TRAVERSAL )
		fgSizer39 = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer39.AddGrowableCol( 0 )
		fgSizer39.SetFlexibleDirection( wx.BOTH )
		fgSizer39.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText_MaxConnections = wx.StaticText( self.m_panel13, wx.ID_ANY, u"Maximum connections", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_MaxConnections.Wrap( -1 )
		
		self.m_staticText_MaxConnections.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		
		fgSizer39.Add( self.m_staticText_MaxConnections, 0, wx.ALL, 5 )
		
		fgSizer40 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer40.AddGrowableCol( 0 )
		fgSizer40.SetFlexibleDirection( wx.BOTH )
		fgSizer40.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.textCtrl_MaxConnections = wx.TextCtrl( self.m_panel13, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer40.Add( self.textCtrl_MaxConnections, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText44 = wx.StaticText( self.m_panel13, wx.ID_ANY, u"(-1 = unlimited)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText44.Wrap( -1 )
		
		self.m_staticText44.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		
		fgSizer40.Add( self.m_staticText44, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		
		fgSizer39.Add( fgSizer40, 1, wx.EXPAND, 5 )
		
		
		self.m_panel13.SetSizer( fgSizer39 )
		self.m_panel13.Layout()
		fgSizer39.Fit( self.m_panel13 )
		fgSizer43.Add( self.m_panel13, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		fgSizer38.Add( fgSizer43, 1, wx.EXPAND, 5 )
		
		self.panel_RecordingPath = wx.Panel( self.scrolledWindow_Main, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_SIMPLE|wx.TAB_TRAVERSAL )
		fgSizer30 = wx.FlexGridSizer( 3, 1, 0, 0 )
		fgSizer30.AddGrowableCol( 0 )
		fgSizer30.SetFlexibleDirection( wx.BOTH )
		fgSizer30.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.staticText_RecordingPath = wx.StaticText( self.panel_RecordingPath, wx.ID_ANY, u"Recording path", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_RecordingPath.Wrap( -1 )
		
		self.staticText_RecordingPath.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		
		fgSizer30.Add( self.staticText_RecordingPath, 0, wx.ALL, 5 )
		
		fgSizer321 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer321.AddGrowableCol( 0 )
		fgSizer321.SetFlexibleDirection( wx.BOTH )
		fgSizer321.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.textCtrl_RecordingPath = wx.TextCtrl( self.panel_RecordingPath, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer321.Add( self.textCtrl_RecordingPath, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.button_RecorderPath = wx.Button( self.panel_RecordingPath, wx.ID_ANY, u"Browse", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer321.Add( self.button_RecorderPath, 0, wx.ALL, 5 )
		
		
		fgSizer30.Add( fgSizer321, 1, wx.EXPAND, 5 )
		
		fgSizer41 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer41.SetFlexibleDirection( wx.BOTH )
		fgSizer41.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText45 = wx.StaticText( self.panel_RecordingPath, wx.ID_ANY, u"Format:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText45.Wrap( -1 )
		
		fgSizer41.Add( self.m_staticText45, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		choice_FormatChoices = [ u"WAV", u"MP3", u"FLAC" ]
		self.choice_Format = wx.Choice( self.panel_RecordingPath, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choice_FormatChoices, 0 )
		self.choice_Format.SetSelection( 0 )
		fgSizer41.Add( self.choice_Format, 0, wx.ALL, 5 )
		
		
		fgSizer30.Add( fgSizer41, 1, wx.EXPAND, 5 )
		
		
		self.panel_RecordingPath.SetSizer( fgSizer30 )
		self.panel_RecordingPath.Layout()
		fgSizer30.Fit( self.panel_RecordingPath )
		fgSizer38.Add( self.panel_RecordingPath, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.panel_Rooms = wx.Panel( self.scrolledWindow_Main, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_SIMPLE|wx.TAB_TRAVERSAL )
		fgSizer42 = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer42.AddGrowableCol( 0 )
		fgSizer42.AddGrowableRow( 1 )
		fgSizer42.SetFlexibleDirection( wx.BOTH )
		fgSizer42.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText46 = wx.StaticText( self.panel_Rooms, wx.ID_ANY, u"Rooms", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText46.Wrap( -1 )
		
		self.m_staticText46.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		
		fgSizer42.Add( self.m_staticText46, 0, wx.ALL, 5 )
		
		listBox_RoomsChoices = []
		self.listBox_Rooms = wx.ListBox( self.panel_Rooms, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, listBox_RoomsChoices, 0 )
		fgSizer42.Add( self.listBox_Rooms, 0, wx.ALL|wx.EXPAND, 5 )
		
		fgSizer44 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer44.AddGrowableCol( 0 )
		fgSizer44.AddGrowableCol( 1 )
		fgSizer44.AddGrowableCol( 2 )
		fgSizer44.SetFlexibleDirection( wx.BOTH )
		fgSizer44.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.button_Delete = wx.Button( self.panel_Rooms, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer44.Add( self.button_Delete, 0, wx.ALL, 5 )
		
		self.button_Save = wx.Button( self.panel_Rooms, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer44.Add( self.button_Save, 0, wx.ALL, 5 )
		
		self.button_Add = wx.Button( self.panel_Rooms, wx.ID_ANY, u"Add", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer44.Add( self.button_Add, 0, wx.ALL, 5 )
		
		
		fgSizer42.Add( fgSizer44, 1, wx.EXPAND, 5 )
		
		
		self.panel_Rooms.SetSizer( fgSizer42 )
		self.panel_Rooms.Layout()
		fgSizer42.Fit( self.panel_Rooms )
		fgSizer38.Add( self.panel_Rooms, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		fgSizer36.Add( fgSizer38, 1, wx.EXPAND, 5 )
		
		
		fgSizer21.Add( fgSizer36, 1, wx.EXPAND, 5 )
		
		self.m_staticline1 = wx.StaticLine( self.scrolledWindow_Main, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer21.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )
		
		fgSizer_BottomWidgets = wx.FlexGridSizer( 0, 4, 0, 0 )
		fgSizer_BottomWidgets.AddGrowableCol( 1 )
		fgSizer_BottomWidgets.SetFlexibleDirection( wx.BOTH )
		fgSizer_BottomWidgets.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.button_Save = wx.Button( self.scrolledWindow_Main, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer_BottomWidgets.Add( self.button_Save, 0, wx.ALL, 5 )
		
		self.checkBox_Autosave = wx.CheckBox( self.scrolledWindow_Main, wx.ID_ANY, u"Autosave on quit", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer_BottomWidgets.Add( self.checkBox_Autosave, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.button_Cancel = wx.Button( self.scrolledWindow_Main, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer_BottomWidgets.Add( self.button_Cancel, 0, wx.ALL, 5 )
		
		self.button_OK = wx.Button( self.scrolledWindow_Main, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer_BottomWidgets.Add( self.button_OK, 0, wx.ALL, 5 )
		
		
		fgSizer21.Add( fgSizer_BottomWidgets, 1, wx.EXPAND, 5 )
		
		
		self.scrolledWindow_Main.SetSizer( fgSizer21 )
		self.scrolledWindow_Main.Layout()
		fgSizer21.Fit( self.scrolledWindow_Main )
		fgSizer_Main.Add( self.scrolledWindow_Main, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( fgSizer_Main )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.button_RecorderPath.Bind( wx.EVT_BUTTON, self.click_recorderpath )
		self.button_Save.Bind( wx.EVT_BUTTON, self.click_save )
		self.button_Cancel.Bind( wx.EVT_BUTTON, self.click_cancel )
		self.button_OK.Bind( wx.EVT_BUTTON, self.click_ok )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def click_recorderpath( self, event ):
		event.Skip()
	
	def click_save( self, event ):
		event.Skip()
	
	def click_cancel( self, event ):
		event.Skip()
	
	def click_ok( self, event ):
		event.Skip()
	

###########################################################################
## Class FrameStats
###########################################################################

class FrameStats ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Pyham Server - Statistics", pos = wx.DefaultPosition, size = wx.Size( 320,160 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		fgSizer45 = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer45.AddGrowableCol( 0 )
		fgSizer45.AddGrowableRow( 0 )
		fgSizer45.SetFlexibleDirection( wx.BOTH )
		fgSizer45.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_scrolledWindow3 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow3.SetScrollRate( 5, 5 )
		fgSizer_Main = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer_Main.SetFlexibleDirection( wx.BOTH )
		fgSizer_Main.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.staticText_Connections = wx.StaticText( self.m_scrolledWindow3, wx.ID_ANY, u"Connections:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_Connections.Wrap( -1 )
		
		fgSizer_Main.Add( self.staticText_Connections, 0, wx.ALL, 5 )
		
		self.m_staticText34 = wx.StaticText( self.m_scrolledWindow3, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )
		
		fgSizer_Main.Add( self.m_staticText34, 0, wx.ALL, 5 )
		
		self.m_staticText35 = wx.StaticText( self.m_scrolledWindow3, wx.ID_ANY, u"Network errors:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText35.Wrap( -1 )
		
		fgSizer_Main.Add( self.m_staticText35, 0, wx.ALL, 5 )
		
		self.m_staticText36 = wx.StaticText( self.m_scrolledWindow3, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText36.Wrap( -1 )
		
		fgSizer_Main.Add( self.m_staticText36, 0, wx.ALL, 5 )
		
		self.m_staticText47 = wx.StaticText( self.m_scrolledWindow3, wx.ID_ANY, u"Network speed:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText47.Wrap( -1 )
		
		fgSizer_Main.Add( self.m_staticText47, 0, wx.ALL, 5 )
		
		self.m_staticText48 = wx.StaticText( self.m_scrolledWindow3, wx.ID_ANY, u"0 KB/s / 0 KB/s", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText48.Wrap( -1 )
		
		fgSizer_Main.Add( self.m_staticText48, 0, wx.ALL, 5 )
		
		self.m_staticText49 = wx.StaticText( self.m_scrolledWindow3, wx.ID_ANY, u"Network data:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText49.Wrap( -1 )
		
		fgSizer_Main.Add( self.m_staticText49, 0, wx.ALL, 5 )
		
		self.m_staticText50 = wx.StaticText( self.m_scrolledWindow3, wx.ID_ANY, u"0 KB / 0 KB", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText50.Wrap( -1 )
		
		fgSizer_Main.Add( self.m_staticText50, 0, wx.ALL, 5 )
		
		
		self.m_scrolledWindow3.SetSizer( fgSizer_Main )
		self.m_scrolledWindow3.Layout()
		fgSizer_Main.Fit( self.m_scrolledWindow3 )
		fgSizer45.Add( self.m_scrolledWindow3, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( fgSizer45 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

