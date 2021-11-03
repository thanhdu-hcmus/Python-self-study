'''
Định dạng chuỗi trong Python
'''
#Dùng %s
a = 'My team is %s' %('Kteam')
a = 'My team is %s %s years old' %('1','2')
print(a)

s = '%s %s'
result = s %('1','2')
print(result)

#Dùng %f
f = '%.f' %(3.99999)
print(f)

#Dùng f-string
f = f'HowKteam.com - Free Education'
print(f)
print(f'a\tb')

k = 'Kteam'
result = f'{k} - Free education'
print(result)

name = 'Kteam'
address = 'Da Lat'
phone = '0123456789'
result = f'student: {{name}}\n{{address}}\n{phone}'
print(result)

#Định dạng format
print('a: {1}, b: {2}, c: {0}'.format('one','two','three'))
print('1:{one},2:{two}'.format(one=111,two=222))
print('How {:*^50} Free education'.format('Kteam'))

#Ví dụ:
# phần định dạng
row_1 = '+ {:-<6} + {:-^15} + {:->10} +'.format('', '', '')
row_2 = '| {:<6} | {:^15} | {:>10} |'.format('ID', 'Ho va ten', 'Noi sinh')
row_3 = '| {:<6} | {:^15} | {:>10} |'.format('123', 'Yui Hatano', 'Japanese')
row_4 = '| {:<6} | {:^15} | {:>10} |'.format('6969', 'Sunny Leone', 'Canada')
row_5 = '+ {:-<6} + {:-^15} + {:->10} +'.format('', '', '')
# phần xuất kết quả
print(row_1)
print(row_2)
print(row_3)
print(row_4)
print(row_5)

#Bài tập
# phần định dạng
row_1 = '+ {:-<6} + {:-^15} + {:->10} +'.format('', '', '')
row_2 = '| {:<6} | {:^15} | {:>10} |'.format('ID', 'Ho va ten', 'Noi sinh')
row_3 = '| {:<6} | {:^15} | {:>10} |'.format('123', 'Yui Hatano', 'Japanese')
row_4 = '| {:<6} | {:^15} | {:>10} |'.format('6969', 'Sunny Leone', 'Canada')
row_5 = '+ {:-<6} + {:-^15} + {:->10} +'.format('', '', '')
result = row_1 + '\n' + row_2 + '\n' + row_3 + '\n' + row_4 + '\n' + row_5
# phần xuất kết quả
print(result)

