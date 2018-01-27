#!/usr/bin/python

from log import log

class Config():
	def __init__(self):
		self.parameters = []

	def load(self, filename):
		log("Loading config file '" + filename + "'.")
		file = open(filename, "r")
		# Read file and parse values into self.parameters
			# split by "#"
			# split by "="
			# crop
			# left = variable, right = value
		# if successful, replace current parameters from read parmeters
		# if unsuccessful, preserve current parameters and give error
		# log("Error loading config file.")
		file.close()

	def save(self, filename):
		log("Saving config file '" + filename + "'.")
		file = open(filename, "w")
		# Generate config file from self.parameters
		# Iterate trough all variables
			# line = "variable = value"
		file.close()
