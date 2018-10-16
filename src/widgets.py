#!/usr/bin/python

# FIXME:
# - RuntimeError: super-class __init__() of type VU was never called

# VU
# VU meter for volume

import wx

class Widget(wx.Window):
	def __init__(self, parent):
		self.parent = parent

	def set_size(self, width, height):
		self.width = width
		self.height = height

class VU(Widget):
	def __init__(self, parent):
		Widget.__init__(self, parent)
		#self.Bind(wx.EVT_SIZE, self.OnSize)
		#self.Bind(wx.EVT_PAINT, self.OnPaint)

	def set_value(self, value):
		self.value = value

	def draw(self):
		dc.SetBrush(wx.Brush(wx.BLACK, wx.SOLID))
		dc.Clear()
		for x in range(self.width / 100 * self.value):
			if x < self.width * 0.5:
				color = wx.Colour(0, 200, 0)	# Green
			elif x < self.width * 0.75:
				color = wx.Colour(200, 200, 0)	# Yellow
			elif x <= self.width:
				color = wx.Colour(200, 0, 0)	# Red
		dc.SetBrush(wx.Brush(color, wx.SOLID))
		dc.SetPen(wx.Pen(wx.BLUE, 1, wx.SOLID))
		dc.DrawRectangle(2, 2, 20, 20)

	def OnSize(self, event):
		self.pixbuf = wx.Bitmap(self.width, self.height)
		memdc = wx.MemoryDC()
		memdc.SelectObject(self.pixbuf)
		self.draw()

	def OnPaint(self, event):
		dc = wx.PaintDC(self)
		dc.DrawBitmap(self.pixbuf, 0, 0, True)

# Scope
# Graphical scope for sound

class Scope(Widget):
	def __init__(self):
		pass

	def draw(self, sound_data):
		pass

	def OnSize(self, event):
		pass

	def OnPaint(self, event):
		pass

# Spectrum
# Graphical spectrum analyzer from sound

class Spectrum(Widget):
	def __init__(self):
		#self.solid = False;		# Draw only outline if false, draw area between value and zero if true
		pass

	def draw(self, sound_data):
		pass

	def OnSize(self, event):
		pass

	def OnPaint(self, event):
		pass

# HistoryGraph
# A bit like Scope but for history graph (ping, transferred data, amount of connections etc.)

class HistoryGraph(Widget):
	def __init__(self):
		pass

	def draw(self, sound_data):
		pass

	def OnSize(self, event):
		pass

	def OnPaint(self, event):
		pass

# PointerGauge
# Clock-like "viisarimittari"

class PointerGauge(Widget):
	def __init__(self):
		pass

	def draw(self, sound_data):
		pass

	def OnSize(self, event):
		pass

	def OnPaint(self, event):
		pass
