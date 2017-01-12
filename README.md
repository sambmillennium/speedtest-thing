# speedtest-thing

Run speedtest.py on remote device and save results to a logfile in the directory this script is located. The goal is to eventually implement functionality to create graphs based on repeated speedtests on the same node etc (still working on this at the moment). Currently the script creates an entry with the hostname, timestamp, download and upload speed (see example log file below).

eval.py in the test branch currently takes the results of the log file and roughly plots these onto a graph. This is early days but will soon feature timestamps and generally be more readable for the end user etc.

This requires the following in order to work:


paramiko https://github.com/paramiko/paramiko

easygui https://github.com/robertlugg/easygui

speedtest.py from sivel installed on the remote device https://github.com/sivel/speedtest-cli

matplotlib: https://github.com/matplotlib/matplotlib
 


______________________________________________

# Example output of the logfile

###### Node1

2017-01-09 12:25:25

Share results: http://www.speedtest.net/result/%yoururl%

Download: 226.54 Mbit/s

Upload: 204.97 Mbit/s




###### Node2

2017-01-09 12:26:38

Share results: http://www.speedtest.net/result/%yoururl%

Download: 242.61 Mbit/s

Upload: 231.54 Mbit/s

