#!/usr/bin/python
"""
data acquistion module for ur-senselab project
"""

import serial
import time
import glob

class ArduinoSerialPort:
	def __init__(self):
		pass 

	def get_serial(self):
		ports = glob.glob('/dev/tty[A-Za-z]*')
		res = []
		for port in ports:
			try:
				s = serial.Serial(port)
				s.close()
				res.append(p
			except:
				pass
		return res[0] 

class DataFetcher:
	def __init__():
		self.port = ArduinoSerialPort().get_serial()
		self.BaudRate = 9600

	def GetData(self):
		try:
			ard = serial.Serial(self.port, BaudRate)
		except Exception as err:
			print err


def main():
	pass


if __name__ == '__main__':
	main()



