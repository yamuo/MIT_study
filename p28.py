s = '1.23,2.4,3.123'
s_list = s.split(',')
total = 0

for i in s_list:
    total += float(i)

print(total)

