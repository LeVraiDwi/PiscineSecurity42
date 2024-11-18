import argparse
from PIL import Image, ExifTags
import re
import os
import hmac
import hashlib
import time
import sys

def is_hexadecimal(string):
    pattern = r'^[0-9A-Fa-f]+$'
    return bool(re.match(pattern, string))


def CheckExtension(filename):
    return filename.split('.')[-1] == 'hex'


def storeKey(key: str) -> bool:
    try:
        assert key != None and CheckExtension(key), "key file with wrong extension expected .hex"
        assert os.path.isfile(key), "must be a path to a file"
    except Exception as e:
        print(e)
        return False
    
    try:
        with open(key, "r") as keyFile:
            line = keyFile.readline().strip()
            if (not is_hexadecimal(line)):
                print("key must be in hexadecimal")
                return False
            if (len(line) < 64):
                print("./ft_otp: error: key must be 64 hexadecimal characters.")
                return False
        
        with open("ft_otp.key", "wb") as otpFile:
            val = int(time.time())
            array = bytearray(val.to_bytes(8, sys.byteorder))
            hashed = hmac.new(array, bytes.fromhex(line), hashlib.sha1).digest()
            otpFile.write(hashed)
            print("Key was successfully saved in ft_otp.key.")
    except Exception as e:
        print(e)
        print(f"fail to open the file: {key}")
        return False

    return True


def genNewKey():
    return


def main():
    parser = argparse.ArgumentParser(prog='ft_otp',
                    description=' a program that allows you to store an initial password in file, and that is capable of generating a new one time password every time it is requested',
                    epilog='./ft_otp [-gk]')
    parser.add_argument('-g', default=None,type=str, help="Hexadecimal key of at least 64 characters, stores this key safely in a file called ft_otp.key")
    parser.add_argument('-k', default=None,type=str, help="Generates a new temporary password based on the key given as argument and prints it on the standard output")
    args = parser.parse_args()

    try:
        assert args.g != None or args.k != None, "Function must have a argument -g or -k"
    except Exception as e:
        print(e)
        return
    
    if (args.g != None):
        if (not storeKey(args.g)):
            return


if __name__ == "__main__":
    main()