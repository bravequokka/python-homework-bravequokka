n = int(input('정수를 입력하세요 >>>'))

if n<=0:
    print('잘못된 입력입니다.')

k=1
while k<=n:
    print('{}번째 Hello' .format(k))
    k +=1

z=1
while z>=1 and z<=100:
    if z%7 ==0:
        print(z)
    z +=1

coin = int(input('자판기에 얼마를 넣을까요? >>>'))
c =1    
while coin>=300:
    print('커피 {}잔, 잔돈{}원' .format(c, coin-300))
    c +=1
    coin -= 300

num = int(input('0 ~9 사이 정수를 입력하세요 >>>'))
set = {num}
while len(set)<=4:
    num = int(input('0 ~9 사이 정수를 입력하세요 >>>'))
    set.add(num)

print('모두 입력되었습니다.')
print('입력된 값은 {}입니다.' .format(set)) 

number = 1
while number <= 100:
    print('{}		{}		{}		{}		{}		{}		{}		{}		{}		{}' .format(number, number+1, number+2, number+3, number+4, number+5, number+6, number+7, number+8, number+9))
    number += 10

dan = 2
dan_1 = 1
while dan <=9:
    while dan_1<=9:
        print('{}x{}={}		{}x{}={}		{}x{}={}		{}x{}={}		{}x{}={}		{}x{}={}		{}x{}={}		{}x{}={}' .format(dan, dan_1, dan_1*dan, dan+1, dan_1, (dan+1)*dan_1, dan+2, dan_1, (dan+2)*dan_1, dan+3, dan_1, (dan+3)*dan_1, dan+4, dan_1, (dan+4)*dan_1, dan+5, dan_1, (dan+5)*dan_1, dan+6, dan_1, (dan+6)*dan_1, dan+7, dan_1, (dan+7)*dan_1))
        dan_1 +=1
    dan +=1

