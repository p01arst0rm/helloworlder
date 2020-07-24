import sys, os, errno

out = os.path.dirname(sys.argv[2])

with open(sys.argv[2],'w+') as w:
    data = '#include "{}"'.format(sys.argv[1])
    w.write(data)


