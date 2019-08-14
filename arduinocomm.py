import serial
try:
    with open('setup.config') as search:
        for line in search:
            line = line.rstrip()  # remove '\n' at end of line
            if "comport" in line:
                com=line.replace('comport ','')

    if com == ' ':
        def write(msg):
            return ''
            exit()
    elif com == '':
        def write(msg):
            return ''
            exit()
    serialComm=serial.Serial('COM{}'.format(com),9600)
    def write(msg):
        for i in range(1000):
            serialComm.write(msg.encode())
        return ""
except:
    print("")
    def write(msg):
        return ""
