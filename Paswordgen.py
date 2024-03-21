#Cognorise Infotech Python Development Internship
#Task 2:PASSWORD GENERATOR

import string
import random
s1=string.ascii_lowercase
s2=string.ascii_uppercase
s3=string.digits
s4=string.punctuation
length=int(input("Enter the length of desired password\n"))
s=[]
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))
print("Your password is: ")
print("".join(random.sample(s, length)))
      
