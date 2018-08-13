x = int(input("Enter an integer:"))
root = 1
pwr = 1
match = 0

for i in range(2,6):
    pwr = i
    root = 1
    while x > root**pwr:
        if root**pwr == x:
            break
        root += 1
    
    if root**pwr == x:
        print("root:",root,"pwe:",pwr)
        match += 1
    elif pwr == 5 and match == 0:
        print("nothing")
        print(match)

print("total matches:",match)
