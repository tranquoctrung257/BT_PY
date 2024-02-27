# Câu 5(nâng cao): Viết chương trình nhập thực hiện các công việc sau:
# -	Nhập số tự nhiên N từ bàn phím
# -	Nhập lần lượt N số tự nhiên thành dãy a1,a2,…,aN. Giả sử dãy này gọi là A
# -	Đưa ra dãy con b1,b2,…bK của dãy A gồm các phần từ
# •	Gợi ý: Thực hiện theo ý tưởng của sàng nguyên tố Eratosthenes

def nhap_day(N):
    A = []
    for i in range(N):
        phan_tu = int(input(f"Nhập phần tử thứ {i+1}: "))
        A.append(phan_tu)
    return A

def liet_ke_day_con(A):
    n = len(A)
    for i in range(n):
        for j in range(i+1, n+1):
            print(A[i:j])



if __name__ == "__main__":
    N = int(input("Nhập số tự nhiên N từ bàn phím: "))
    A = nhap_day(N)
    print("các con số của dãy a là")
    liet_ke_day_con(A)