#gán cho biến a giá trị là 4. Với 4 là kiểu số nguyên (Intergers)
a = 9.6

print(a)

#kiểu dữ liệu của a
print(type(a))

#Lấy toàn bộ nội dung của thư viện decimal
#từ thư viện decimal -> import mọi thứ vào
from decimal import*

#Lấy tối đa 30 chữ số phần nguyên và phần thập phân
getcontext().prec = 30

d = Decimal(10)/Decimal(3)
print(d)
print(type(d))