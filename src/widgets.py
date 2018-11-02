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
		self.__width = width
		self.__height = height

class VU(Widget):
	def __init__(self, parent):
		Widget.__init__(self, parent)
		#self.Bind(wx.EVT_SIZE, self.OnSize)
		#self.Bind(wx.EVT_PAINT, self.OnPaint)

	def reset(self):
		self.__value = None

	def set_value(self, value):
		self.__value = value

	def draw(self):
		dc.SetBrush(wx.Brush(wx.BLACK, wx.SOLID))
		dc.Clear()
		for x in range(self.__width / 100 * self.__value):	# Maybe we should use floats instead of ints?
			if x < self.__width * 0.5:
				color = wx.Colour(0, 200, 0)	# Green
			elif x < self.__width * 0.75:
				color = wx.Colour(200, 200, 0)	# Yellow
			elif x <= self.__width:
				color = wx.Colour(200, 0, 0)	# Red
		dc.SetBrush(wx.Brush(color, wx.SOLID))
		dc.SetPen(wx.Pen(wx.BLUE, 1, wx.SOLID))
		dc.DrawRectangle(2, 2, 20, 20)

	def OnSize(self, event):
		self.__pixbuf = wx.Bitmap(self.__width, self.__height)
		memdc = wx.MemoryDC()
		memdc.SelectObject(self.__pixbuf)
		self.draw()

	def OnPaint(self, event):
		dc = wx.PaintDC(self)
		dc.DrawBitmap(self.__pixbuf, 0, 0, True)

# Scope
# Graphical scope for sound

class Scope(Widget):
	def __init__(self):
		pass

	def reset(self):
		self.__data = None

	def set_value(self, value):
		self.__value = value

	def draw(self):
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
		#self.__data = None
		pass

	def set_value(self, value):
		self.__value = value	# TODO: Append to self.__data and cycle old value out

	def draw(self):
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

	def set_value(self, value):
		self.__value = value

	def draw(self):
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

	def set_value(self, value):
		self.__value = value

	def draw(self):
		# needle_center =
		# needle_point = sin()
		# draw line from needle_center to needle_point
		pass

	def OnSize(self, event):
		pass

	def OnPaint(self, event):
		pass
