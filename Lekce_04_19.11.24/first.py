import hashlib

b = b'Lorem ipsum dolor sit amet consectetur'
print(hashlib.sha256(b).hexdigest())