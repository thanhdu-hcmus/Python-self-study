'''
Ôn tập các bài trước.
1. Kiểu string, dấu '',"", escape sequence
2. Toán tử, indexing
3. Format cho string: %s, f-string, .format
4. Các phương thức cho kiểu string
'''

a = 'how kteam free education'
c = '5'
d = '   k   '
b = a.split(' ', 2)
b = a.rsplit(' ', 2)
b = a.partition('kteam')
b = a.rpartition('y')
b = a.count('e',0,13)
b = a.startswith('h',0,9)
b = a.endswith('n')
b = a.find('t')
b = a.rfind('t')
b = a.index('h')
b = a.islower()
b = a.isupper()
b = a.istitle()
b = c.isdigit()
b = d.isspace()
print(a)
print(b)

s = 'aaaAAaaaooaaneu mot Ngay naO Doaaaaaaa'
tmp = s.upper().strip('A').lstrip('OA').title()
print(tmp)