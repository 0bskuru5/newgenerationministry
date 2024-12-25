import random
x = random.randint(2,10) # type: ignore
r = x%2
if r == 0:
    print("go home")
else: 
    print("dont")