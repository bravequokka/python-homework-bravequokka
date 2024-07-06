money = 50000
offer = input('명령을 입력하세요')
list = []
while money>=0:
    if offer == 'a':
        pswd = input('비밀번호를 입력하세요')
        if pswd == 'admin':
            print('관리자 모드 전환')
        elif pswd != 'admin':
            print('비밀번호가 틀렸습니다.')
            break
    elif offer == 'b':
        print('현재 잔액 : {}' .format(money))
        continue
    elif offer == 'c':
        print('현재 구매한 상품 목록 : {}' .format())
        continue
    elif offer == '1':
        print('스타벅스 5천원 상품권이 나왔습니다.')
        money -= 5000
        list.append('스타벅스 5천원권')
        continue
    elif offer == '2':
        print('올리브영 1만원 상품권이 나왔습니다.')
        money -= 10000
        list.append('올리브영 1만원 상품권')
        continue
    elif offer == '3':
        print('신세계상품권 5만원이 나왔습니다.')
        money -= 50000
        list.append('신세계상품권 5만원')
        continue
    else:
        print('다시 입력하세요')
        continue


    

