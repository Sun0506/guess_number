import random
start = int(input('請輸入起始值: '))
end = int(input('請輸入終值: '))

r = random.randint(start, end)
count = 0
while True:
	count += 1
	user = int(input('猜一個數字: '))
	if user == r:
		print('你猜中了!')
		break
	elif user > r:
		print('比答案大')
	elif user < r:
		print('比答案小')
	print('你已經猜了', count, '次')
