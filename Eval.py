# WORK IN PROGRESS, NOT YET COMPLETE

# To evaluate log file and generate graph of results over time period

import re
import sys, os, time
import easygui
import matplotlib.pyplot as plt

d_results = []
u_results = []
timestamp = []
d_fin = []
u_fin = []
ts = []
#open logfile

print('Choose log file to parse')
time.sleep(3)
path = easygui.fileopenbox()
f = open (path, 'r')

#loop to find download speeds and append to lists for plotting

for line in f:
    if line.startswith('Download'):
        d_results.append(re.findall('\d+\.\d+', line))
    elif line.startswith('Upload'):
        u_results.append(re.findall('\d+\.\d+', line))
    elif line.startswith('2017'):
        timestamp.append(line)

f.close()

#formatting for matplotlib
for i in range(len(d_results)):
    d_fin.append(d_results[i])

for e in range(len(u_results)):
    u_fin.append(u_results[e])

for g in range (len(timestamp)):
    ts.append(timestamp[g])

#plot graph
graph = plt.plot(d_fin), plt.plot(u_fin)
plt.suptitle('Speedtest', fontsize=14, fontweight='bold')
plt.xlabel('Timestamp')
plt.ylabel('Speed (Mbps)')
plt.show(graph)
