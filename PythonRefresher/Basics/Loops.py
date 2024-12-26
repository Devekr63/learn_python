my_list = [1,2,3,4,5]

for num in my_list:
    print(num)

for x in range(1,5):
    print(x)

ind = 0
total = 0

while ind < len(my_list):
    total += my_list[ind]
    ind += 1

print(total)

i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)
else: print("Now number is greater than 5")