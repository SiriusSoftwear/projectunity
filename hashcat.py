import os
hashfile=''
def startHashcatRound():
    for i in range(0,1000):
        os.system('type example.dict | hashcat64\hashcat64.exe -m 400 '+hashfile+' --outfile output\\'+str(i)+'.txt --outfile-format 2')
startHashcatRound()

