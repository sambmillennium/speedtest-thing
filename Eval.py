# WORK IN PROGRESS, NOT YET COMPLETE

# To evaluate log file and generate graph of results over time period

import re
import sys, os, time
import easygui

d_results = []
u_results = []

# open logfile

print('Choose log file to parse')
time.sleep(3)
path = easygui.fileopenbox()
f = open (path, 'r')

# Seperate download speeds from rest of the information and add to d_results (download) or u_results (upload)

for line in f:
    if line.startswith('Download'):
        d_results.append(re.findall('\d+\.\d+', line))
    elif line.startswith('Upload'):
        u_results.append(re.findall('\d+\.\d+', line))
    break
f.close()
