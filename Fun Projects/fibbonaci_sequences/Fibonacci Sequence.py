
n = int(input("How many ranks would you like to output?:  "))
a, b = 0, 1
print(f'calculating {n} ranks')
for i in range(n):
    print(a)
    a, b = b, a + b
print(f'{n} ranks calculated')
