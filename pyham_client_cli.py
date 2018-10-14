#!/usr/bin/python

# Pyham CLI
# Command line interface without wxWidgets, with ncurses and without

# Commands:
# connect, disconnect, nick, description

class ClientCLI:
	def __init__(self, filename):
		line = ""

		while line != "quit":
		line = input("Prompt: ")
		# TODO: parse command
		#print (line)