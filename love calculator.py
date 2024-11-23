name1 = input("enter your name: ")
name2 = input("enter your name: ")
 
conbined_name= name1 + name2
lower= conbined_name.lower()

t=lower.count("t")
r=lower.count("r")
u=lower.count("u")
e=lower.count("e")

true= t+r+u+e

l=lower.count("l")
o=lower.count("o")
v=lower.count("v")
e=lower.count("e")

love=l+o+v+e
total=str(true) + str(love)
tot = int(total)
if tot > 90:
  print(f"your love score is  {tot}, you go together like coke and mentos ")
elif tot<90 and tot >=70:
  print(f"your love score is {tot}, you are alright together")
elif tot>=50:
  print(f"your love score is {tot}, you are not too much")
elif tot<50:
  print(f"your score is {tot}, you are fucked")