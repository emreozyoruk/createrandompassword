import string
from random import *
characters = string.ascii_letters + string.punctuation + string.digits
karakterSayisi = input("Karakter sayisi kac olsun? ")
password = ""
for i in range(int(karakterSayisi)):
       password += choice(characters)
print(password)
