# Câu 2: Cho trước dãy A bao gồm N phần tử.Sử dụng các hàm của module random để viết thủ tục sinh một hoán vị ngẫu nhiên của dãy A. Đưa kết quả lên màn hình

import random
a = [1,"a","c",22,3,4,5]

def ran_dom(a):
    print(random.choice(a))

ran_dom(a)