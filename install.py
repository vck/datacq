#!/usr/bin/env python
# coding=utf-8

import os, sys, subprocess

if sys.id != 0:
    print "must run as root"
    sys.exit(0)

python_modules = ["ino","flask"]

for mods in python_modules:
    print 'installing mods"
    print subprocess.check_output(["pip", "install",mods], output=True)



