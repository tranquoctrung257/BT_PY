# Câu 1: Viết chương trình tạo list gồm 10 số Fibonacci đầu tiên.

def fibo(n):
    lst = [0,1]
    fn1,fn2 = 1,0
    for i in range(2,n):
        fn = fn1 + fn2
        lst.append((fn))
        fn2,fn1 = fn1,fn
    return lst

if __name__ == "__main__":
    print(fibo(10))