# speedtest-thing

Run speedtest.py on remote device and save results to a logfile in the directory this script is located. The goal is to eventually implement functionality to create graphs based on repeated speedtests on the same node etc. Could be useful for central log of speedtests throughout a network.

This requires the following in order to work:


paramiko https://github.com/paramiko/paramiko

easygui https://github.com/robertlugg/easygui

speedtest.py from sivel installed on the remote device https://github.com/sivel/speedtest-cli


 


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

