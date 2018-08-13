
"""
input_dict = {'x':13,'y':5,'z':20}
odd_list = []
even_list = []

for value in input_dict.values():
    if value%2 == 0:
        even_list.append(value)
    else:
        odd_list.append(value)

print("odd is :" + str(odd_list))
print("even is :" + str(even_list))

print("max odd is :" + str(max(odd_list)))
"""
odd_list = []
even_list = []

for i in range(10):
    input_num = int(input('Plese input a number :'))
    if input_num % 2 == 0:
        even_list.append(input_num)
    else:
        odd_list.append(input_num)   

print("odd is :" + str(odd_list))
print("even is :" + str(even_list))

if odd_list:
    print("max odd is :" + str(max(odd_list)))
else:
    print("odd is nothing")
