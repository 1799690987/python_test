import os
import chardet
import sys, getopt
import time

from PIL import Image

if __name__ == '__main__':
    a=True
    b=False
    if a and not b:
        print()

    Image.open(file_path)
    opts, args = getopt.getopt(sys.argv[1:], '-h:-f:', ['help', 'filepath='])
    for opt_name, opt_value in opts:
        if opt_name in ('-h', '--help'):
            print("[*] Help info")
        if opt_name in ('-f', '--filename'):
            fileName = opt_value
            print("[*] Filename is ", fileName)
            # do something
            exit()

