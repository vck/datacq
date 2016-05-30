#/usr/bin/python
"""
pekerja utama pemasok data sensor dijalankan dengan schedule
penulis: vickydasta
"""
import schedule
import lib.timestamps as timestamps
import serial
import time
import csv
from time import strftime
import lib.portdetect as pd
import lib.data as parser

def TestJob():
	starttime = time.time()
	file_name = timestamps.date_time()+'.csv'
	target_file = open('/home/pi/datacq/static/'+file_name,'a')
	csvobj = csv.writer(target_file, delimiter=";")
   	for i in range(101):
   		print 'attempt: ',i
		data = serial.Serial(pd.port().portlist(),9600).readline()
		json_obj = parser.JSON(data)
		normal_data = json_obj.normalizer()
		if normal_data is None:
			pass
		try:
			print 'attempt {} writing to {} - {} to {}'.format(i, normal_data[u'data1'][0], normal_data[u'data2'][0], file_name)
			csvobj.writerow((strftime("%Y-%m-%d %H-%M-%S"), normal_data[u'data1'][0], normal_data[u'data2'][0]))
		except Exception as err:
			print err
		time.sleep(5)
	target_file.close()

schedule.every(5).minutes.do(TestJob)

if __name__ == '__main__':
   while True:
   	schedule.run_pending()
   	print "waiting another job..."

