#!/usr/bin/python

# Read/save parameters from/to a config file

# Format:
# parameter = value
#
# Values:
# 	integer
# 	string
# 	boolean:
# 		1/0, true/false, on/off, enabled/disabled

# TODO:
# - on/off, 1/0, true/false (case insensitive)
# - Parse value arrays (for presets)
# - Accessors to values
# - Use configparser library
# - Try to create new config file (with folders) during save if file does not exist before

#import configparser
from log import log, error
from os.path import isfile

class Config():
	def __init__(self, parameters={}):
		self.parameters = parameters

	def load(self, filename):
		# Read file and parse values into self.parameters
		# TODO: Read multiple parameters inside square brackets
		log("Opening config file '" + filename + "'...")
		# Check if file exists:
		if isfile(filename):
			try:
				with open(filename, "r") as file:
					linecount = 0
					for line in file:
						linecount += 1
						l = line.strip()
						if len(l) > 0 and l[0] != '#':
							i = l.find('=')
							if i != -1 and len(l[i:]) > 0:
								parameter = l[:i-1].strip()
								value = l[i+1:].strip()
								self.parameters[parameter] = value
					log(str(linecount) + " lines read from config file.")
					#if verbose:
					#log("Parameters:")
					#for key in self.parameters:
						#log(key + " = " + self.parameters[key])
			#except FileNotFoundError:
				#log("Error: config file not found.")
			#except PermissionError:
				#log("Error: No permission to read config file.")
			except Exception as e:
				error(self, "while reading config file: " + str(e))
		else:
			error(self, "config file not found. Using zero values.")

	def save(self, filename):
		# Generate config file from self.parameters
		# TODO: preserve comments, newlines, indents etc.
		log("Saving config file '" + filename + "'...")
		try:
			with open(filename, "w") as file:
				linecount = 0
				for key in self.parameters:
					file.write(key + " = " + self.parameters[key] + "\n")
					linecount += 1
				log(str(linecount) + " lines wrote to config file.")
		except Exception as e:
			error(self, "while saving config file: " + str(e))

	def __str__(self):
		# Return current parameter array as text
		string = ""
		for key in self.parameters:
			string += (key + " = " + self.parameters[key] + "\n")
		return string
