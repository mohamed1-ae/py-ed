import sys
import os

filename = sys.argv[1]

with open(filename, 'r') as r:
    if os.stat(filename).st_size == 0:
        pass
    else:
        print(r.read())

with open(filename, 'a') as f:
    if os.stat(filename).st_size == 0:
        f.write(input(': '))
    else:
        f.write('\n')
        f.write(input(': '))

with open(filename, 'r') as r:
    print(r.read())
