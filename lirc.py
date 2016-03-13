import subprocess
def getids():
 """
 returns a array of all configured devices
 """
 cmd = 'irsend LIST "" ""'
 proc = subprocess.Popen(cmd, shell=True,stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
 tmp = proc.stdout.read()
 ntmp = tmp.replace("irsend: ", "")
 device = ntmp.split("\r\n")
 return device
