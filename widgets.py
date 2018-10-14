#!/usr/bin/python

# TODO: console/ncurses versions

# VU
# VU meter for volume

class VU:
	def __init__(self):
		pass

	def setvalue(self, value):
		pass

	def draw(self):
		pass

# Scope
# Graphical scope for sound

class Scope:
	def __init__(self):
		pass

	def draw(self, sound_data):
		# Return pixel array in some sort of wxwidget
		pass

# Spectrum
# Graphical spectrum analyzer from sound

class Spectrum:
	def __init__(self):
		pass

	def draw(self, sound_data):
		# Return pixel array in some sort of wxwidget
		pass

# HistoryGraph
# A bit like Scope but for history graph (ping, transferred data, amount of connections etc.)

class HistoryGraph:
	def __init__(self):
		pass

	def draw(self, sound_data):
		# Return pixel array in some sort of wxwidget
		pass
