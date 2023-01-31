#!python3

from sys import argv
contents = open(argv[1]).readlines()

print (argv[1])
print(contents)
# contents = open(os.path(argv[1])).readlines()
# input_file = with open()
headers = contents[:1]
trailers = contents[-1:]
records = contents[1:-1]

f= open(argv[2],'w',newline="\n")
for line in records:
     output = line[4:7] + line [11:12] + "\n"
     f.write(output)
f.close()

