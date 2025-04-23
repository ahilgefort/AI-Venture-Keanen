yes = 0 
while yes == 0:
    no = input()
    if no == "yep":
        yes = 1
        print("you said",no)
    if no == "nope":
        yes = 0
        print("you said",no)
        continue