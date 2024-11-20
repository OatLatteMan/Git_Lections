import hashlib

a = 'Lorem ipsum dolor sit amet consectetur'
b = a.encode()
c = hashlib.sha256(b)
d = c.hexdigest()

print(a)
print(b)
print(c)
print(d)
print(hashlib.sha256(b).hexdigest())