import sys
import os

print(sys.argv[0]) # This file name

fileName = 'TestFile.txt'

if not os.path.isfile(fileName):
    print('[-] File not exist.')
else:
    print('[+] File exist')

if not os.access(fileName, os.R_OK):
    print('[-] Not accessible.')
else:
    print('[+] Accessible')

exit(0)

