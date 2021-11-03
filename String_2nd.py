#Chuỗi trần là chuỗi không quan tâm đến Escape Sequence
#Quan trọng khi dùng regular expression
print(r'Haizz, \neu mot ngay nao do')

#Toán tử cho String
strA = "HowKteam"
strB = strA[len(strA)-1] #Python bắt đầu từ 0
# strC = strA + "\n" + strB
# strC = strA*5
strC = strB in strA
print(strB)

#Toán tử in sẽ nhận được trong 2 đáp án (True or False)
#Kiểm tra chuỗi có nằm trong một chuỗi khác hay không.

#Indexing và Cắt chuỗi từ trái qua phải
strA = "HowKteam"
# strB = strA[1:5]			#owKt
# strB = strA[-2]			#a
# strB = strA[1:len(strA)]  #owKteam
# strB = strA[None:5]		#HowKt
# strB = strA[None:None] 	#HowKteam
strB = strA[:]				#HowKteam
strC = strB in strA
print(strB)

#Cắt chuỗi từ phải qua trái
strA = "HowKteam"
strB = strA[None:5:2]		#Hwt
strC = strA[None:5:-1]		#ma
print(strB)

#Ghép chuỗi và Ép kiểu
strA = int(6.9) #Lấy nguyên, bỏ phần thập phân
strA = float("6.9")
strA = int("69") + 5
strB = str(69) + "5"
print(strA)
print(strB)

#Indexing
strA = "HowKteam.com"
#Ngôn ngữ khác thì có thể strA[1] = '0'
strA = strA[None:1] + "0" + strA[2:None]
print(hash(strA))
#Tại sao lại có chuyện này?
#Chúng ta không thể thay đổi nội dung chuỗi
#Vì nó là một hashtable object(immune)
#trong một lần chạy python, giá trị của hàm hash không đổi
#khi chạy một lần khác, thì giá trị hàm hash thay đổi

#Bài tập
s = r'\gte\teng\n\vz\adf\t'
print(s)
s = 'abc xyz'
print(s[1:1])