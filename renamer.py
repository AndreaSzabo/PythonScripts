# -*- coding: utf-8 -*-

import os
import sys
from shutil import move

if len(sys.argv) != 3:
    print "Na de mégis babám, kivel akarsz szórakozni? Adj meg szépen egy bemeneti mappát és egy kimenetit! :*"
    exit()

in_folder = sys.argv[1]
out_folder = sys.argv[2]

if os.path.exists(in_folder):
    print "letezik"
else:
    print "nem letezik"

rootDir = in_folder
tag = 0
ExtensionsToCopy = ['.jpg', '.nef', '.mov', '.avi', '.mp4']
for dirName, subdirList, fileList in os.walk(rootDir):
    print('Found directory: %s' % dirName)
    if dirName != out_folder:
        for fname in fileList:
            if len([extension for extension in ExtensionsToCopy if extension in fname.lower()]):
                lns = fname.split('.')
                move( dirName + "\\" + fname, out_folder + "\\" + lns[0][:len(lns[0])-4] + str(tag).zfill(4) + "." + lns[1])
                print('\t%s' % fname)
                tag = tag+1

