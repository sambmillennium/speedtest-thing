from __future__ import print_function
import base64
import paramiko
from easygui import passwordbox
from string import replace
from time import gmtime, strftime


log = ('log', 'a')
command = base64.b64decode('c3BlZWR0ZXN0IC0tc2hhcmU=', None)
# device to connect to
host = raw_input('enter host: ' + '\n')
user = raw_input('enter user: ' + '\n')
pw = passwordbox('enter password: ' + '\n')


print('running speedtest.......')

 # Create SSH connection to device and run command
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=user, password=pw)
stdin, stdout, stderr = client.exec_command(command)

 # get download and upload speed from stdout
result = []
for line in stdout:
    result.append(line.strip('\n'))
client.close()


 # cleanup stdout results and print to log file
res = result[6]
res2 = result[8]
graphic = result[9]

print(host, file=log)
print(strftime("%Y-%m-%d %H:%M:%S", gmtime()), file=log)
print(graphic, file=log)
print(res + '\n' + res2 + '\n' + '\n', file=log)

print('speedtest for ' + host + ' complete. To see the results navigate to the log file or follow this link: ' '\n' '\n' + graphic)
