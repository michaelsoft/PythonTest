f=open('TestFile.txt','r')
text = f.readlines()
for line in text:
    print(line.strip())