from secrets import token_bytes
from typing import Tuple

# For example, the from_bytes() method will take 7bytes (7bytes * 8bit = 56 bit) and convert them into a 56bit integer.
def randoom_key(length: int) -> int:
    # generate length random bytes
    tb: bytes = token_bytes(length)
    # convert those bytes into a bits str and return it 
    return int.from_bytes(tb, "big")

def encrypt(original: str) -> Tuple[int, int]:
    original_bytes: bytes = original.encode()
    dummy: int = randoom_key(len(original_bytes))
    original_key: int = int.from_bytes(original_bytes, "big")
    encrypted: int = original_key ^ dummy # XOR
    return dummy, encrypted

# str can be convert into a sequence of UTF-8 bytes (as bytes type)   through the encode() method.
# a sequence of UTF-8 bytes can be convert back into a str using decode()method on the bytes type.

def decrypt(key1: int, key2: int) -> str:
    decrypted:int = key1 ^ key2 # XOR
    # add 7 before using division (//) to divide by 8 ensure the we "round up", avoid off-by-one error.
    # to_bytes() method, first arg is number of bytes to be converted.
    
    tmp: bytes = decrypted.to_bytes((decrypted.bit_length() + 7) // 8, 'big')
    return tmp.decode()

if __name__ == "__main__":
    key1, key2 = encrypt("One time pad!")
    result: str = decrypt(key1, key2)
    print(result)