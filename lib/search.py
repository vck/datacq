#!/usr/bin/python
import os
import time

"""
pustaka pencarian berkas
"""

def file_modified_info(filename):
    (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(file)
    return time.ctime(mtime)

def locate_file(filter):
    """cari file berdasarkan saringan"""
    filelist = []
    for root, dir, files in os.walk('.', topdown=False):
        for file in files:
            if filter in file:
                filelist.append(os.path.join(root, file))
    return filelist

def locate_with_folder(rootdir, filter):
    """cari berkas berdasarkan folder dan kata kunci"""
    file_list = []
    for root, dir, files in os.walk(rootdir, topdown=False):
        for file in files:
            if filter in file:
                file_list.append( (root.strip('.'), file, '{}'.format(os.path.getsize(root+'/'+file)/1024) ))
    return file_list

def delete_file(file):
    os.system('rm %s'%file)

def get_csv():
    files = locate_file('.csv')
    return files

def get_zip():
    files = locate_file('.zip')
    return files

def main():
    data = locate_with_folder('./static', '.csv')
    print data

if __name__ == '__main__':
    main()
