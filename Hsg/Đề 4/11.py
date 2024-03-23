# Câu 11: Viết chương trình nhập số tự nhiên n và thiết lập:
# -	Dãy A bao gồm các số tự nhiên lẻ nhỏ hơn n
# -	Dãy B bao gồm các số tự nhiên chẵn nhỏ hơn n

n = int(input("nhập số tự nhiên n: "))
c,l = [],[]
for i in range(1,n+1):
    if i % 2 == 0: c.append(i)
    else:l.append(i)
print(c)
print(l)

# hoặc
# print([i  for i in range(1,n+1) if n % 2 == 0 ])