import socket

hosts = ["10.2.8.111", "10.2.8.113"]
ports = [80, 4200, 8080]

for host in hosts:
  for port in ports:
      try:
        s = socket.socket()
        #s.settimeout(60)

        s.connect_ex((host, port))
        s.send(b'hi')
        banner = s.recv(256)
        if banner:
            print(f'[+] {host} - {port} opened \n')
        s.close()
      except Exception as err:
        print(f'[-] {host} - {port} closed \n')
        #print(err)
