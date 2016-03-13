def getids():
 """
 returns a array of all configured devices
 """
 cmd = 'irsend LIST "" ""'
 proc = subprocess.Popen(cmd, shell=True,stderr=subprocess.STDOUT, stdout=sub$
 tmp = proc.stdout.read()
 ntmp = tmp.replace("irsend: ", "")
 device = ntmp.split("\r\n")
 return device
