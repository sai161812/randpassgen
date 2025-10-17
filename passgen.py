import random
word=int(input("Enter the length of your password :"))
num=list("0123456789")
alpha=list("abcdefghijklmnopqrstuvwxyz")
ALPHA=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
specialchar=list("!@#$%&*")
pass3=num+alpha+ALPHA+specialchar
passw=random.sample(pass3,word)
print(*passw,sep="")
