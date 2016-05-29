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
	jsondata = None
	def __init__(self, data):
		self.data = data
	def normalizer(self):
		jsondata = None
		try:
			jsondata = json.loads(self.data)
		except Exception as err:
			pass
		return jsondata

class DataFetcher:
	def __init__(self, port):
		self.BaudRate = 9600
		self.port = port

	def GetData(self):
		data = None
		ard = None
		try:
			ard = serial.Serial(self.port, self.BaudRate)
		except Exception as err:
			print err
		try:
			data = ard.readline()
		except Exception:
			pass
		return data