#coding: utf8
import sys
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex

class prpcrypt():
def __init__(self, key):
   self.key = key
   self.mode = AES.MODE_CBC

#Encryption function, if text is not a multiple of 16 [encrypted text text must be a multiple of 16! ], then make up to #a multiple of 16

def encrypt(self, text):
   cryptor = AES.new(self.key, self.mode, self.key)

#The length of the key here must be 16 (AES-128), 24 (AES-192), or 32 (AES-256) Bytes length. Currently AES-128 is #sufficient

length = 16
count = len(text)
if(count % length != 0) :
    add = length - (count % length)
else:
    add = 0
    text = text + ('\0' * add)
    self.ciphertext = cryptor.encrypt(text)

#Because the string obtained during AES encryption is not necessarily in the ascii character set, there may be problems #when outputting to the terminal or saving
#So here we uniformly convert the encrypted string into a hexadecimal string

    return b2a_hex(self.ciphertext)

#After decryption, remove the supplementary spaces and remove them with strip()

def decrypt(self, text):
    cryptor = AES.new(self.key, self.mode, self.key)
    plain_text = cryptor.decrypt(a2b_hex(text))
    return plain_text.rstrip('\0')

if __name__ == '__main__':
    pc = prpcrypt('keyskeyskeyskeys') #initialize key
    e = pc.encrypt("0123456789ABCDEF")
 
    d = pc.decrypt(e)
    print e, d
    e = pc.encrypt("00000000000000000000000000")
    d = pc.decrypt(e)
    print e, d
