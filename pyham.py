#!/usr/bin/python

import sys
from datetime import datetime

def log(text):
	print >>sys.stderr, "[" + datetime.now().strftime('%Y/%m/%d %H:%M:%S') + "] " + text

# TODO:
# - log file
