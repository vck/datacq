#!/usr/bin/python
import schedule
import time
import timestamps


schedule.every(5).minutes.do(create_zip)

if __name__ == '__main__':
    while True:
        schedule.run_pending()
        time.sleep(2)
        print 'waiting...'
