'''
for n in range(5,0,-1):
    print(n)

sum=0
primary = int(input('임의의 양수를 입력하세요 >>>'))
for k in range(1, primary+1):
    sum += k

print('1부터 {}사이 모든 정수의 합계는 {}입니다.' .format(primary, sum))

fr=[]
num = int(input('몇 개의 과일을 보관할까요? >>>'))
for n in range(1, num+1):
    fruit = input('{}번째 과일을 입력하세요 >>>' .format(n))
    fr.append(fruit)
    n += 1

print(fr)
'''

exam = [99, 78, 100, 91, 81, 85, 54, 100, 71, 50]

if exam >=95 (exam = 100):
    exam.append