#!/usr/bin/python

# curses terminal user interface with widgets such as buttons etc.

class Window():
	def __init__(self):
		pass

class Button():
	def __init__(self):
		pass

class Textarea():
	def __init__(self):
		pass

class Checkbox():
	def __init__(self):
		pass

class Radiobutton():
	def __init__(self):
		pass

class Radiogroup():
	def __init__(self):
		pass

class Slider():
	def __init__(self):
		pass

class Label():
	def __init__(self):
		pass

class Scrollbar():
	def __init__(self):
		pass

class Chooser():
	def __init__(self):
		self.items = {}
		self.selecteditem = 0

	def set_item(index, value):
		self.items[index] = value
