import math
a = [2,19,30,45,100,101,103,105,257,890,1001,10101]
# a = [5]
b = []
n =  100



for j in a:
    for i in range(2,int(j**0.5)+1):
        if j % i == 0:
            break
    else:
        b.append(j)

print(a)
print(b)


