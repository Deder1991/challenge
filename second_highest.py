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


# def second_highest(students):
#     grades = [s[1] for s in students] # 只把成績拿出來
#     grades = sorted(grades, reverse=True)
#     second = grades[1] # grades[0]是最高，grades[1]是第二高
    
#     # 再下來找誰是這個分數
#     # 底下這句話的意思是拿到 所有分數跟第二高一樣的人的"人名"也就是s[0]的部分
#     # 記得嗎 參數的這個students清單裡面的東西，s[0]是人名，s[1]是分數
#     second_high_students = [s[0] for s in students if s[1] == second]
#     for student in second_high_students:
#         print(student)



