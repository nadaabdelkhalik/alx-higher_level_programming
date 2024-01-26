#!/usr/bin/python3
def uppercase(str):
  
    for i in str:
        upper=chr(ord(i)-32)if 'a' <= i <= 'z' else i
        print("{}".format(upper), end='')
    print()
