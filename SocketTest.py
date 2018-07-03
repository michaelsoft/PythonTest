import socket

def retBanner(ip, port):
    s = socket.socket()
    socket.setdefaulttimeout(2)
    try:
        s.connect((ip,port))
        banner = s.recv(1024)
        return banner
    except:
        return

def testSocket():
    ip = '10.9.101.73'
    ports = [21,22,25,80,110,443]
    for port in ports:
        banner = retBanner(ip, port)
        if banner:
            print('[+]:%d %s' % (port,banner))
        else:
            print('[-]:%d'% port)

if __name__ == '__main__':
    testSocket()