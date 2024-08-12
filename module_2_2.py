first = int(input("число:"))
print('first',first)
second = int(input("число:"))
print('second',second)
third = int(input("число:"))
print('third',third)
if first == second == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
else:
    print(0)