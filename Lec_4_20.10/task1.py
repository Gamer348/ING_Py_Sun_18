a = int(input())
b = int(input())
c = int(input())

total_amount = 0
for class_s in [a,b,c]:
    if class_s % 2 != 0:
        total_amount += class_s//2 + 1
    else:
        total_amount += class_s//2

print(total_amount)