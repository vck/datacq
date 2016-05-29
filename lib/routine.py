#/usr/bin/python
import schedule
import time
import csv
from time import strftime

def WriteFile(r, filename):
	f = open(filename, 'a')
	csvobj = csv.writer(f, delimiter=";")
	for i in range(1, r):
		csvobj.writerow((strftime("%Y-%m-%d %H-%M-%S"), random.choice(data)))
		time.sleep(1)
	print 'done'

def RunJob():
	filename = "data.csv"
	print '[{}] writing to {}'.format(strftime("%Y-%m-%d %H-%M-%S"),filename)
	WriteFile(1000, filename)

schedule.every(1).minutes.do(RunJob)

while True:
	schedule.run_pending()
	time.sleep(1)
