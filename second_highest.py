#印出成績第二高的，如果有相同就印出人名

students = [['Tom', 38], ['Jerry', 37],['Akriti', 90], ['Justin', 100], ['Leo', 90]]

def second_highest(students):
	c = len(students) 
	n1 = 0 #比對項目
	n2 = 0 #沒有交換的次數
	while True:
		if n1 < c-1: #需要比對的次數
			if students[n1][1] < students[n1 + 1][1]:
				stay = students[n1]
				students[n1] = students[n1 + 1]
				students[n1 + 1] = stay
			else:
				n2 += 1 #沒有交換位置的話+1
			n1 += 1
		elif n2 == c-1: #一輪過都沒交換就跳出迴圈
			break
		elif n1 == c-1: #經過一輪清零再來
			n1 = 0 
			n2 = 0
	# print(students)
	
	n3 = 2 #開始比較的位置
	print(students[1][0])
	while True: 
		if students[1][1] == students[n3][1]: #如果有成績相同的
			print(students[n3][0])
			n3 += 1 #下一次的位置
		else:
			break

second_highest(students)



