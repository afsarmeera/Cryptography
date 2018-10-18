# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 06:32:10 2018

@author: MohamedAfsar
"""
import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi
    
    while e > 0:
        temp1 = temp_phi/e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2
        
        x = x2- temp1* x1
        y = d - temp1 * y1
        
        x2 = x1
        x1 = x
        d = y1
        y1 = y
    
    if temp_phi == 1:
        return d + phi



p=3
print "p is:"
print (p)

q=5
print "q is:"
print(q)

n = p * q
print "n is:"
print(n)

phi = (p-1) * (q-1)
print "phi is:"
print(phi)
e = random.randrange(1, phi)

#public
g = gcd(e, phi)
while g != 1:
   e = random.randrange(1, phi)
g = gcd(e,phi)

#private
d = multiplicative_inverse(e, phi)
  

print "public key is:"  
print(e)  
print "Private key is:"
print(d)


a=2
print("message")
print(a)

b = a ** e % n

print("Cipher:")
print(b)

c= b ** d % n
print("decrypted")
print(c)