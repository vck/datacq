#/usr/bin/python
"""
pekerja utama pemasok data sensor dijalankan dengan schedule
penulis: vickydasta
"""
import serial
import time
import lib.portdetect as pd
import lib.data as parser

def TestJob():
	#target_file = open('/home/pi/datacq/static/'+file_name,'a')
	#csvobj = csv.writer(target_file, delimiter=";")
   	for i in range(101):
   		print 'attempt: ',i
		data = serial.Serial(pd.port().portlist(), 9600).readline()
		if data:
			json_obj = parser.JSONParser(data)
			normal_data = json_obj.normalizer()
		if normal_data is None:pass
		print normal_data['data1'][0]
		print normal_data['data2'][0]
		print normal_data['sensor']
		#print parser.json_loads_byteified(normal_data)

if __name__ == '__main__':
	while True:
   		TestJob()


