count = 0

def fib(n):
    global count
    if n ==2:
        count += 1
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def testFib(n):
    for i in range(n+1):
        print("fib of", i, "=", fib(i))

testFib(20)
print(count)
