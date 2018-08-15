"""
x = 0.0
for i in range(10):
    x = x + 0.1
if x == 1.0:
    print(x,'= 1.0')
else:
    print(x,'is not 10')
"""

n = 11
str_n = str(n)
len_n = len(str_n)
dex = 0

for i in str_n:
    dex += 2**(len_n - 1) * int(i)
    len_n -= 1

print(dex)
