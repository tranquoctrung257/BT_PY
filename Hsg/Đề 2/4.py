# Câu 4: Viết hàm số f(n) với tham số n là số tự nhiên theo yêu cầu sau:
# a)	Hàm trả lại số các ước số thực sự của n
# b)	Hàm trả lại 1 nếu n là nguyên tố, ngược lại hàm trả về 0
# c)	Hàm đếm số các ước số là lẻ của n
# d)	Hàm đếm số các ước số nguyên tố của n
# e)	Hàm tính tổng tất cả các ước số thực sự của n

# a.
def a(n):
    lst = []
    for i in range(1,n+1):
        if n % i == 0:
            lst.append(i)
    return lst

# b.
def b(n):
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return 0          
    else:
        return 1

# c.
def c(n):
    count = []
    for i in range(1,n+1):
        if n % i == 0:
            if i % 2 != 0:
                count.append(i)
    return len(count)

# d.
def d_(num):
    if num >= 2:
        for i in range(2,int(num**0.5)+1):
            if num % i == 0:
                return False         
        else:
            return True
    else:
        return False
def d(n):
    if not(d(n)):
        return f"{n} ko phải số nguyên tố "
    else:
        count = 0
        for i in range(1,n+1):
            if n%i == 0 and d(n):
                count +=1
        return f"số ước của số nguyên tố {n} là: {count}"        

# e.
def e(n):
    count = 0
    for i in range(1,n+1):
        if n % i == 0:
            count+=i
    return count

