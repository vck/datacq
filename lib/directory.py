#!/usr/bin/python
import os
"""
"""
def get_file():
    """get file on current directory"""
    files = []
    for root, dir, files in os.walk('.',topdown=False):
        for f in files:
            files.append(os.path.join(root+f))
    return file

def main():
    print get_file()

if __name__ == '__main__':
    main()
