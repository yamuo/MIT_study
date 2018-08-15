a = "dit"
b = "dit"

def isIn(a,b):
    if a in b:
        print(b, "is including", a)
    if b in a:
        print(a, "is including", b)
    else:
        print("nothing")

isIn(a,b)
