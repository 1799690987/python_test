import os
import chardet

if __name__ == '__main__':
    utf8 = "Hello, World!".encode()
    print(utf8)
    print(utf8.decode())