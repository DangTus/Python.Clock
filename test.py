# import time

# i=1

# while True:

# 	print(i)
# 	i = i+1
# 	time.sleep(2)

# 	if i == 10:
# 		break

def hello1(**var):
	print(var["a"])

a = "hello1"
b = "hello2"

hello1(b = b, a = a)