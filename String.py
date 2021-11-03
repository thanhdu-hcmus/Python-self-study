#Sự khác nhau giữa '' và ""
#Tức là khi bên trong chuỗi có sử dụng dấu '' và ngược lại

#Trong chuỗi vừa có nháy đơn và dấu nháy kép thì code làm sao?

strHowKteam = "I'm Beginner"
strHowKteam = '"I am Beginner"'
print(strHowKteam)
print(type(strHowKteam))
#string

#Chuỗi nhiều dòng ''' ''' """ """
#Ứng dụng của chuỗi nhiều dòng, darkstring
'''
Đây là chú thích đầu file py
còn muốn ghi gì thì cứ ghi
Nó giống như comment
'''

str = """How Kteam.com\nFree education\nShare to be better"""
print(str)

#\ gọi là Escape Sequence, kí tự đặc biệt.
#Một số kí tự đặc biệt, \n, \t, \',\",\\

print('\a')
print('dong 1\ndong 2')
print('Hello\tfriend')
print('I\'m beginner')
print('I\\m beginner')
#Chuẩn SOLID
