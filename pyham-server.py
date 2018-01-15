#!/usr/bin/python

# pyham server program

programName = "pyham server"
programVersion = "0.001"

import sys
from datetime import datetime

timestamp = datetime.now()
print >>sys.stderr, "[" + timestamp.strftime('%Y/%m/%d %H:%M:%S') + "] Server started."
print >>sys.stderr, "[" + timestamp.strftime('%Y/%m/%d %H:%M:%S') + "] Server stopped."
