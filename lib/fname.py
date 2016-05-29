#!/usr/bin/python

"""
generate new CSV file every day with current timestamps
ex: 04262016-135453.csv
"""

# schedule.every().day.at('00.01').do(generate)
schedule.every(1).minutes.do(generate)

if __name__ == '__main__':
    while True:
        schedule.run_pending()
        time.sleep(2)
