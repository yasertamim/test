#i have replaced the variable name
for j in range(1,11):
    print(j,end=' ')
print("\n")
for j in range(2,22,2):
    print(j,end=' ')
print("\n")
for k in range(1,20,2):
    print(k,end=' ')
print("\n")
for l in range(1,50,3):
    print(l,end=' ')
print("\n")
for m in range(40,1,-4):
    print(m,end=' ')
print("\n")
for Number in range (1, 101):
    count = 0
    for i in range(2, (Number//2 + 1)):
        if(Number % i == 0):
            count = count + 1
            break

    if (count == 0 and Number != 1):
        print(" %d" %Number, end = '')
