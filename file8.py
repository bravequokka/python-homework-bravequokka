'''
def adder(*args):
    print('{}의 합은 {}입니다.' .format(args, sum(args)))

adder(1, 2)
adder(1, 2, 3)
adder(1,2, 3, 4)

def coffe_machine(money, pick):
    print('{}원에 {}를 선택하셨습니다.' .format(money, pick))
    menu = {
        '아메리카노' : 1000,
        '카페라떼' : 1500,
        '카푸치노' : 2000
    }
    if pick not in menu:
        print('{}는 판매하지 않습니다.' .format(pick))
        return money, '없는 메뉴'
    elif menu[pick] > money:
        print('{}는 {}원입니다.' .format(pick, menu[pick]))
        return money, '금액부족'
    else:
        return money-menu[pick], pick
    
order = input('커피를 선택하세요. (아메리카노, 카페라떼, 카푸치노) >>>')
pay = int(input('얼마를 내시나요? >>>'))

change, coffee = coffe_machine(pay, order)
print('잔돈 {}원, 커피 {}' .format(change, coffee))

beverage = 0
def vending_machine(money):
    for beverage in range(0, money//700 +1):
        print('음료수 = {}개, 잔돈 = {}원' .format(beverage, money))
        beverage += 1
        money -= 700

vending_machine(3000)

def get_average(marks):
    values = list(marks.values())
    total_sum = sum(values)
    return total_sum / len(marks)

marks = {'국어' : 90, '영어' : 80, '수학' : 85}
average = get_average(marks)
print('평균은 {}점입니다.' .format(average))
'''
total = 0
def gift(dic, who, money):
    wedding = {who : money}
    total = sum(dic.values())
    return wedding, total

wedding = {}
gift(wedding, '영희', 5)
gift(wedding, '철수', 3)
gift(wedding, '이모', 10)
print('축의금 명단 : {}' .format(wedding))
print('전체 축의금 : {}' .format(total))