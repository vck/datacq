#!/usr/bin/python
import os

"""
pustaka pencarian berkas
"""

def getfile(filter):
    """"""
    filelist = []
    for root, dir, files in os.walk('.', topdown=False):
        for file in files:
            if filter in file:
                filelist.append(os.path.join(root, file))
    return filelist



def get_csv():
    files = getfile('.csv')
    return files

def get_zip():
    files = getfile('.zip')
    return files

def main():
    print get_file()

if __name__ == '__main__':
    main()
