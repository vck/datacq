#/usr/bin/python
# start all bot process
"""
author: vickydasta
"""

import sys
import time
import json
import sys

class JSONParser:
	"""
	data parser for arduino json-ized data
	(i've doubt if jsonized is even a word.)
	"""
	
	def __init__(self, data):
		self.data = data	
	def normalizer(self):
		try:
			if self.data:
				json_data = json.loads(self.data.strip('\r'))
				return json_data 
		except Exception as err:
			print err 
