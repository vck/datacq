#!/usr/bin/env python
# coding=utf-8

import os, sys, subprocess

python_modules = ["ino","flask"]
debian_modules = ["python-serial","arduino-core"]

print 'installing mods'
for mods in python_modules:
	print "installing %s"%mods
   	subprocess.check_output(["sudo","pip", "install",mods], output=True)

print 'installing debian packages...'
for mods in debian_modules:	
	print "installing %s"%mods
	subprocess.check_output(["sudo","apt-get","install", mods])





