import random

passlen = int(input("enter the length of password:"))

s = "abcdefghijklmnopqrstuvwsxyz0123456789ABDETRYYJUIHKML!@#$%^&*"
p = "".join(random.sample(s,passlen))
print(p)

