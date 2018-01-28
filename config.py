#!/usr/bin/python

from log import log
from os.path import isfile

class Config():
	def __init__(self):
		self.parameters = []

	def load(self, filename):
		# Read file and parse values into self.parameters
		log("Opening config file '" + filename + "'...")
		# Check if file exists:
		if isfile(filename):
			try:
				with open(filename, "r") as file:
					linecount = 0
					for line in file:
						linecount += 1
						if '#' not in line:
							# TODO: String parsing, allow # in strings
							# Split by '=' to get parameter and value:
							pair = line.split('=')
							if len(pair) == 2 and len(pair[0]) > 0 and len(pair[1]) > 0:
								parameter = pair[0].strip()
								value = pair[1].strip()
								# self.parameters[parameter = value]
							elif pair[0] != "\n":
								log("Error in config file at line " + str(linecount) + ":" + "\n" + line.strip())
					log(str(linecount) + " lines read from config file.")
			#except FileNotFoundError:
				#log("Error: config file not found.")
			#except PermissionError:
				#log("Error: No permission to read config file.")
			except:
				log("Error while reading config file.")
		else:
			log("Error: config file not found.")

	def save(self, filename):
		# Generate config file from self.parameters
		log("Saving config file '" + filename + "'...")
		try:
			with open(filename, "w") as file:
				linecount = 0
				for line in self.parameters:
					linecount += 1
					# Iterate trough all variables
					# line = "variable = value"
					#log("Error while saving config file.")
				log(str(linecount) + " lines wrote to config file.")
		except:
			log("Error while saving config file.")

	def __str__():
		# Return current parameters
		return "TODO"
