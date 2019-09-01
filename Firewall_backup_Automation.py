from subprocess import Popen, PIPE
from datetime import datetime

with open ('ipconfig.txt', 'rt') as myfile:
timestamp = datetime.now().strftime('%m-%d-%Y %H-%M-%S')
for line in myfile:
# FIRST
p1 = Popen(['pscp', 'socadmin@'+line.strip()+':fgt-config', 'c:\config\\'+line.strip()+'time'+timestamp+'.conf'],stdin=PIPE,stdout=PIPE,stderr=PIPE,shell=True)
s1 = p1.communicate()
err1 = str(s1[1])
print(err1)
   
if "fingerprint" in err1:
	print("fingerprint")
	p2 = Popen(['pscp', 'socadmin@'+line.strip()+':fgt-config', 'c:\config\\'+line.strip()+'time'+timestamp+'.conf'],stdin=PIPE,stdout=PIPE,stderr=PIPE,shell=True)
	p2.stdin.write(b'y')
	print(p2.communicate())
	p3 = Popen(['pscp', 'socadmin@'+line.strip()+':fgt-config', 'c:\config\\'+line.strip()+'time'+timestamp+'.conf'],stdin=PIPE,stdout=PIPE,stderr=PIPE,shell=True)
	p3.stdin.write(b'27InfoTask@&\r\n')
	print(p3.communicate())
	print("successful after giving yes")
else:
	p4 = Popen(['pscp', 'socadmin@'+line.strip()+':fgt-config', 'c:\config\\'+line.strip()+'time'+timestamp+'.conf'],stdin=PIPE,stdout=PIPE,stderr=PIPE,shell=True)
	p4.stdin.write(b'27InfoTask@&\r\n')
	print(p4.communicate())
	print("Successful")
