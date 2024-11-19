import argparse
from cryptography.fernet import Fernet
import string
import os
import hmac
import hashlib
import time
import sys


def is_hexadecimal(toCheck: str):
    return (all(c in string.hexdigits for c in toCheck) == True)


def encryptKey(key: str, toEncrypt: str):
    fernet = Fernet(key)
    encrypted = fernet.encrypt(bytes.fromhex(toEncrypt))
    return encrypted

def decryptKey(key: str, toDecrypt: str):
    fernet = Fernet(key)
    decrypted = fernet.decrypt(toDecrypt)
    return decrypted


def CheckExtension(filename):
    return filename.split('.')[-1] == 'hex'


def storeKey(path: str, key: str) -> bool:
    try:
        assert path != None and CheckExtension(path), "key file with wrong extension expected .hex"
        assert os.path.isfile(path), "must be a path to a file"
    except Exception as e:
        print(e)
        return False
    
    try:
        with open(path, "r") as keyFile:
            line = keyFile.readline().strip()
            if (not is_hexadecimal(line)):
                print("key must be in hexadecimal")
                return False
            if (len(line) < 64):
                print("./ft_otp: error: key must be 64 hexadecimal characters.")
                return False
        
        with open("ft_otp.key", "wb") as otpFile:
            encrypted = encryptKey(key, line)
            otpFile.write(encrypted + "\n0")
            print("Key was successfully saved in ft_otp.key.")
    except Exception as e:
        print(e)
        print(f"fail to open the file: {path}")
        return False

    return True


def genNewKey(keyFile: str, key: str, digit: int):
    with open(keyFile, "r") as file:
        crypted = file.readline()
        decrypted = decryptKey(key, crypted)
        print(decrypted)
        val = int(time.time())
        hmac_result = hmac.new(decrypted, bytearray(val), hashlib.sha1).digest()
        offset = hmac_result[-1] & 0xf
        bin_code = (hmac_result[offset] & 0x7f) << 24 | (hmac_result[offset+1] & 0xff) << 16 | (hmac_result[offset+2] & 0xff) <<  8 | (hmac_result[offset+3] & 0xff)
        bin_code = bin_code % (10**digit)
        ret = str(bin_code)
        while (len(ret) < digit):
            ret += "0"
        print(ret)
    return


def main():
    parser = argparse.ArgumentParser(prog='ft_otp',
                    description=' a program that allows you to store an initial password in file, and that is capable of generating a new one time password every time it is requested',
                    epilog='./ft_otp [-gk]')
    parser.add_argument('-g', default=None,type=str, help="Hexadecimal key of at least 64 characters, stores this key safely in a file called ft_otp.key")
    parser.add_argument('-k', default=None,type=str, help="Generates a new temporary password based on the key given as argument and prints it on the standard output")
    args = parser.parse_args()
    key = "4-ky663vt5tKzExszIzBgDzh9yo6Fv6BvpCnjvEoNHA="
    
    try:
        assert args.g != None or args.k != None, "Function must have a argument -g or -k"
    except Exception as e:
        print(e)
        return
    
    if (args.g != None):
        if (not storeKey(args.g, key)):
            return

    if (args.k != None):
        genNewKey(args.k, key, 6)

if __name__ == "__main__":
    main()