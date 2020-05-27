import glob
import os
import sys

folder = sys.argv[1]

files = glob.glob(f"{folder}/*/*")
files.sort()

f = open(f"{folder}/image.lst", "w")

for i, path in enumerate(files):
    file = path[len(folder)+1:]
    cls = int(file[:3])-1
    f.write(f"{i}\t{cls}\t{file}\n")
