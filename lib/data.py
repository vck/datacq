#/usr/bin/python
# start all bot process
"""
author: vickydasta
"""

import sys
import schedule
import os
import lib.timestamps as timestamps
import serial
import time
import glob
import json
import csv
import sys
from time import strftime
try:
	import lib.portdetect as portdetect
except ImportError:
	sys.exit('cannot import portdetect')

class JSON:
	"""JSON parser"""
	
	def __init__(self, data):
		self.data = data
		self.jsondata = ""
	def normalizer(self):
		try:
			self.jsondata = json.loads(self.data)
		except Exception as err:
			pass
		return self.jsondata

"""
class DataFetcher:
	def __init__(self, port):
		self.BaudRate = 9600
		self.port = port

	def GetData(self):
		ard = serial.Serial(self.port, self.BaudRate)
        data = ard.readline()
        return data
"""

