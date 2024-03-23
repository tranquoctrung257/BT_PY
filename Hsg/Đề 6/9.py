# Câu 9: Nhập từ bàn phím họ tên một người. Viết chương trình tách và in ra họ, đệm, tên của người này

# Ví dụ: c : output sẽ là: họ - Lê, đệm – Văn, tên – Nam

def tach(chuoi):
    ho = chuoi.split()[0]
    ten = chuoi.split()[-1]
    dem = chuoi.split()[1:-1]
    temp = []
    if len(dem) > 1:
        for i in dem:
            temp.append(i)
        temp = " ".join(temp) 
        print("họ - %s, đệm - %s, tên - %s"%(ho,temp,ten))
    else:         
        print("họ - %s, đệm - %s, tên - %s"%(ho,*dem,ten))


if __name__ == "__main__":
    tach("võ nguyễn hồng ân")
    tach("Lê Văn Nam")