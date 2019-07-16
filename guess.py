import random
r = random.randint(1,100)
while True:
	user = int(input('請猜 1~100 正整數: '))
	if user == r:
		print('你猜中了!')
		break
	elif user > r:
		print('比答案大')
	elif user < r:
		print('比答案小')
