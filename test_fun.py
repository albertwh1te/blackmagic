import random
# s = random.randint(1,10)
s = 10
n = 0
while True:
  tmp = input('请输入一个数字：')
  guess = int(tmp)
  if guess == s:
    print('恭喜你答对了') 
    break
  if guess > s:
    print('你输入的数字大了-----')
  if guess < s:
    print('你输入的数字小了-----')
  n = n + 1
  if n == 3:
    print('失败，游戏结束')
    break
