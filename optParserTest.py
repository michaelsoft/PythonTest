import optparse

parser = optparse.OptionParser("Usage: ./optParserTest.py -f <file name> -d <folder name>")
parser.add_option('-f', dest='fName', type='string', help='File name')
parser.add_option('-d', dest='dName', type='string', help='Directory name')
(opts, args) = parser.parse_args()
if (opts.fName == None) | (opts.dName == None):
    print (parser.usage)
else:
    print('fName=%s,dName=%s' % (opts.fName, opts.dName))
