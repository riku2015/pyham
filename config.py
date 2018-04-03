#!/usr/bin/python

# Read/save parameters from/to a config file

# Format:
# parameter = value
#
# Values:
# integer
# string
# 0/1, true/false, on/off, enabled/disabled

from log import log
from os.path import isfile

class Config():
	def __init__(self):
		self.parameters= {}

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
					#	log(key + " = " + self.parameters[key])
			#except FileNotFoundError:
				#log("Error: config file not found.")
			#except PermissionError:
				#log("Error: No permission to read config file.")
			except Exception, e:
				log("Error while reading config file: " + str(e))
		else:
			log("Error: config file not found. Using zero values.")

	def save(self, filename):
		# Generate config file from self.parameters
		log("Saving config file '" + filename + "'...")
		try:
			with open(filename, "w") as file:
				linecount = 0
				for line in self.parameters:
					linecount += 1
					# log(key, value)
					# Iterate trough all variables
					# line = "variable = value"
					#log("Error while saving config file.")
				log(str(linecount) + " lines wrote to config file.")
		except Exception, e:
			log("Error while saving config file: " + str(e))

	def __str__():
		# Return current parameters
		return "TODO"
