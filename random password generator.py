import random
lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbol="(){}[]:;@#"
number="0123456789"
all=lower+upper+symbol+number
length=5
password="".join(random.sample(all,length))
print("THE GENERATOR PASSWORD IS :",password)

