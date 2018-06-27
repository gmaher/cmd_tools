import argparse
import os

parser = argparse.ArgumentParser()

parser.add_argument('-file',type=str)
parser.add_argument('-dir',type=str)
parser.add_argument('-extensions', nargs='*', required=True)

args = parser.parse_args()

#########################################
# Code
#########################################
inlines = open(args.file,'r').readlines()

files = os.listdir(args.dir)
files = [args.dir+'/'+f for f in files]

for f in files:
    if not any([e in f for e in args.extensions]): continue

    print(f)

    outlines = open(f,'r').readlines()

    total_lines = inlines+['\n']+outlines

    outfile  = open(f,'w')

    for l in total_lines:
        outfile.write(l)

    outfile.close()
