'''
Phương thức của kiểu chuỗi
'''
a = '12'
print(int(a))
print(type(a))

a = "**how Kteam - Free education**"
b = a.capitalize()
b = a.upper()
b = a.lower()
b = a.swapcase()
b = a.title() #Viet hoa chu cai dau
b = a.center(50, '-')
b = a.rjust(50,'*')
b = a.ljust(50,'*')
b = a.encode(encoding='utf-8', errors='strict')
b = a.replace('K', 'ó')
b = a.strip('*') #loại bỏ hết kí tự ở hai đầu
b = a.lstrip('*')
b = a.rstrip('*')
print(a)
print(b)