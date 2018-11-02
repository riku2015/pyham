#!/usr/bin/python

# curses terminal user interface with widgets such as buttons etc.

class Input():
	def __init__(self):
		self.__value = None

	def get_value(self):
		return self.__value

	def set_value(self, value):
		self.__value = value

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

	def get_item():
		return self.selecteditem
