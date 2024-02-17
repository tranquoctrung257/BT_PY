# Câu 2: Viết chương trình nhập từ bàn phím số tự nhiên ss tính theo giây, sau đó đổi số giây này ra thành giờ, phút, giây và thông báo trên màn hình. Ví dụ nhập ss=3740 thì kết quả hiển thị như sau:
# 3740 giây=1 giờ 2 phút 20 giây
# (Gợi ý: Sử dụng hàm phép tính nâng cao : hàm divmod()
# ==>	Ý nghĩa hàm divmod(): Như ta đã biết có phép // và % trong python. Thì // tương ứng là div, còn % tương ứng là mod. Vậy hàm divmod() thay thế cho cả 2 phép tính trên.
# ==>	Công thức: divmod(x,y)=x//y, x%y
# ==>	Ví dụ: divmod(12.5, 2) sẽ cho kết quả là: (6.0, 0.5)

ss = int(input("nhập số giây từ bàn phím: "))
# ss = 3740

h = 3600
m = 60

hour = divmod(ss,h)

# ss // 3060 ==> phần chia lấy phần nguyên là giờ
# ss % 3060 ==> phần dư là số giây để tính phút

minute = divmod(hour[-1],m)

# hour[-1] lấy phần tử cuối cùng, 
# tức là lấy phần dư của hour chia lấy phần nguyên cho 60 ==> số phút
# hour[-1] % 60 ==> số giây


print(f"{hour[0]} giờ {minute[0]} phút {minute[-1]} giây.")