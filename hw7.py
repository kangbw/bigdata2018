# Assignment Number ...: 7
# Student Name ........: 강병욱
# File Name ...........: hw7_강병욱
# Program Description..: 제어문(if-else ,while, for)을 활용하는 법을 익힌다.

print('''[전략 게임 : 연애?! 할 수 있어!! 야~~ 너두]
 게임 규칙:
   (1) 애정도, 돈, 체력 수준이 0에 도달하거나 바람 수준이 5에 도달하면 연애는 종료된다. 
       (* baby 사건이 발생해도 연애는 종료된다. - baby지수는 연속으로 3번 항목을 선택하면 발생하는 이벤트다.) 
   (2) 12 개월 후 연애는 종료된다.
''') # print를 이용하여 게임명, 게임규칙을 설명하였다.

your_name = input("당신의 이름을 입력하세요 : ") # input함수를 이용하여 이름에 대한 입력값을 받았다.

print('\n{}의 연애를 시작합니다'.format(your_name)) # 게임시작을 알리는 문구를 프린터하였다.

status = [['love', 5], ['stamina', 5], ['money', 5], ['girl', 0]] # 게임지수와 수치를 리스트형태로 매핑하여 초기화하였다.
baby = 0 # 게임지수중 하나인 baby지수를 0으로 초기화하였다.

def date(): # 1번 항목에 대한 함수를 생성하였다.
    global status # 전역변수 status의 각 항목을 직접 제어하기 위해 global 명령어를 이용하였다.
    global baby # 전역변수 baby을 직접 제어하기 위해 global 명령어를 이용하였다.
    baby = 0 # 함수가 호출될때마다 baby를 0으로 재정의 하였다.
    for i in range(len(status)): # for문을 이용하여 status의 리스트 갯수만큼 for문을 실행하였다.
        if status[i][0] == 'love': # status 리스트의 첫번째 항목값(지수)가 'love'이면 1을 증가 하였다.
            status[i][1] += 1
        else : # 그 외의 모든 지수들은 -1씩 감소하도록 정의하였다.
            status[i][1] -= 1
    print('애정 1 감소, 체력, 자금, 바람이 1씩 상승하였습니다.\n') # 게임 수치의 변화를 프린터하였다.
    return status # status의 새로운 상태를 반환하였다.
            
def rest(): # 2번 항목에 대한 함수를 생성하였다.
    global status # 전역변수 status의 각 항목을 직접 제어하기 위해 global 명령어를 이용하였다.
    global baby  # 전역변수 baby을 직접 제어하기 위해 global 명령어를 이용하였다.
    baby = 0 # 함수가 호출될때마다 baby를 0으로 재정의 하였다.
    for i in range(len(status)): # for문을 이용하여 status의 리스트 갯수만큼 for문을 실행하였다.
        if status[i][0] == 'love': # status 리스트의 첫번째 항목값(지수)가 'love'이면 2 감소하였다.
            status[i][1] -= 2
        elif status[i][0] == 'stamina' or status[i][0] == 'money' : # 마찬가지로 'stamina'와 'money'는 2씩 증가하도록 하였다.
            status[i][1] += 2 # 순환문을 돌기 때문에 or함수를 써도 둘중 하나를 만족하면 해당 수치가 증가한다.
    print('애정 2 감소, 체력, 자금이 2씩 상승하였습니다\n') # 게임 수치의 변화를 프린터하였다.
    return status  # status의 새로운 상태를 반환하였다.

def make_love(): # 3번 항목에 대한 함수를 생성하였다.
    global status # 전역변수 status의 각 항목을 직접 제어하기 위해 global 명령어를 이용하였다.
    global baby  # 전역변수 baby을 직접 제어하기 위해 global 명령어를 이용하였다.
    baby += 1 # 함수가 호출될때마다 baby를 1씩 증가 하도록 정의 하였다.
    for i in range(len(status)):
        if status[i][0] == 'stamina': # status 리스트의 첫번째 항목값(지수)가 'stamina'이면 2 감소하였다.
            status[i][1] -= 2
        elif status[i][0] == 'money': # status 리스트의 첫번째 항목값(지수)가 'money'이면 1 감소하였다.
            status[i][1] -= 1
        elif status[i][0] == 'love': # status 리스트의 첫번째 항목값(지수)가 'love'이면 3 증가하였다.
            status[i][1] += 3
    print('체력이 2 감소, 자금 1 감소, 애정이 3 상승하였습니다.\n') # 게임 수치의 변화를 프린터하였다.
    return status # status의 새로운 상태를 반환하였다.

def club():  # 4번 항목에 대한 함수를 생성하였다.
    global status # 전역변수 status의 각 항목을 직접 제어하기 위해 global 명령어를 이용하였다.
    global baby # 전역변수 baby을 직접 제어하기 위해 global 명령어를 이용하였다.
    baby = 0 # 함수가 호출될때마다 baby를 0으로 재정의 하였다.
    for i in range(len(status)):# for문을 이용하여 status의 리스트 갯수만큼 for문을 실행하였다.
        if status[i][0] == 'girl': # status 리스트의 첫번째 항목값(지수)가 'girl'이면 2 증가하였다.
            status[i][1] += 2
        else : # 나머지 항목은 1씩 증가하였다.
            status[i][1] += 1
    print('바람이 2 상승, 애정, 자금, 체력이 1씩 상승하였습니다.\n') # 게임 수치의 변화를 프린터하였다.
    return status  # status의 새로운 상태를 반환하였다.

def end_function(baby_n, stats, iterates): # 게임 종료 조건시 결과를 프린터하는 함수를 매개변수 3개로 생성하였다.
    if baby_n >= 3: # 전달인자 baby지수가 3이상이면 발생하도록 baby_n 매개변수로 결과문을 프린터 하였다.
        print('{} 주니어가 탄생하였습니다. 사랑이 격하셨어요ㅠ 이제 연애할 일 없으니 취업이나 합시다~~'.format(your_name))
    elif stats[0][1]<=0 : # 전달인자 status의 'love'지수가 0이하이면 발생하도록 stats 매개변수로 결과문을 프린터 하였다.
        print('{}가 0이 되었습니다. 애정이 식어버렸군요 ㅠㅠ 이제 공부나 합시다~~'.format(stats[0][0]))
    elif stats[2][1] <= 0 : # 전달인자 status의 'money'지수가 0이하이면 발생하도록 stats 매개변수로 결과문을 프린터 하였다.
        print('{}이 0이 되었습니다. 돈도 없고, 나가서 할게 없네요ㅠㅠ 이제 공부나 합시다~~'.format(stats[2][0]))
    elif stats[1][1] <= 0: # 전달인자 status의 'stamina'지수가 0이하이면 발생하도록 stats 매개변수로 결과문을 프린터 하였다.
        print('{}이 0이 되었습니다. 연애가 힘드네요 ㅠㅠ 나가지 말고 공부나 합시다~~'.format(stats[1][0]))
    elif stats[3][1] >= 5: # 전달인자 status의 'girl'지수가 5이상이면 발생하도록 stats 매개변수로 결과문을 프린터 하였다.
        print('{}이 5를 초과하였습니다. 바람피다 걸려버렸네요 ㅠㅠ 연애고 뭐고 공부나 합시다~~'.format(stats[3][0]))
    elif iterates == 12: # 전달인자 i(순환값)가 12이면 발생하도록 iterates 매개변수로 결과문을 프린터 하였다.
        print('12개월 동안 연애를 지속하였습니다. 대다나다~~~~!!!')

def count_function(count): # 게임 종료시 결론을 프린터하는 함수를 매개변수(count)로 생성하였다.
    if count<= 5: # 전달인자(i)의 값이 5이하이면 발생하도록 count 매개변수로 결론문을 프린터 하였다.
        print('당신은 연애 하수~~ 연애를 글로 배웠어요~ (내가 연애 ㄱㅈ라니~~!!!)')
    elif count <= 8 : # 전달인자(i)의 값이 5이상, 8이하이면 발생하도록 count 매개변수로 결론문을 프린터 하였다.
        print('당신은 연애 중수~~ 연애맛 좀 본 당신... 뭔가 좀 부족하다ㅠ')
    else : # 전달인자(i)의 값이 8이상이면 발생하도록 count 매개변수로 결론문을 프린터 하였다.
        print('당신은 연애 고수~~ 연애좀 해봤는걸~ 지도편달 부탁드립니다~ㅎㅎ')
 
i = 0 # 12개월을 순환하기 위한 변수로써 i=0으로 초기화 하였다.

while i<= 12: # while문을 이용하여 i가 12개월 이상이면 연애를 종료하도록 하였다.
    print("""*** 당신의 상태 ***
애정 : {}
자금 : {}
체력 : {}
바람 : {}

당신의 행동을 선택해주세요
1 - 데이트 콩닥콩닥~
2 - 자기야 미안~ 오늘은 집에서 좀 쉴래ㅠ
3 - 오늘밤 집에 가기 싫어~ 잇힝~~ 싸랑해!!
4 - 친구가 쏜다 ㄱㄱ 나이트 부비부비~~
""".format(status[0][1],status[2][1], status[1][1], status[3][1])) # 삼중따옴표와 format을 이용하여 게임지수의 수치를 인덱싱하여 지정하였다.
    try: # 예외처리를 이용하여 번호 선택하는 입력값이 문자열이거나 5이상의 번호를 입력하면 예외처리 되도록 하였다.
        choice = int(input('번호를 입력하세요 => ')) # 번호 선택 입력값을 정수로 변환시키도록 input함수를 이용하였다.
        i += 1 # try 문을 실행할 때 순환값(i)는 1씩 증가하도록 하였다.
        if choice > 4 : # 번호 선택이 4를 넘어갈때 ValueError에러를 발생하도록 하였다.
            raise ValueError
        if choice == 1: # 번호 1번을 선택하였을 때 date함수가 실행하도록 하였다.
            date()
        elif choice == 2: # 번호 2번을 선택하였을 때 rest함수가 실행하도록 하였다.
            rest()
        elif choice == 3: # 번호 3번을 선택하였을 때 make_love함수가 실행하도록 하였다.
            make_love()
        elif choice == 4: # 번호 4번을 선택하였을 때 club함수가 실행하도록 하였다.
            club()
    except ValueError: # try문에서 입력값이 문자이거나 4를 초과할때 순환값(i)는 -1을 하고 번호를 다시 입력하도록 프린터 하였다.
        i -= 1
        print('번호가 잘못 입력되었습니다.\n')
    
    if status[0][1]<=0 or status[2][1] <= 0 or status[1][1] <= 0 or status[3][1] >= 5 or baby >= 3 or i == 12: #수치가 게임 종료 조건을 만족시킬 때 발생하도록 하였다.
        print('연애가 종료 되었습니다.\n\n결과 : \n') # 게임 종료 조건을 만족하면 연애 종료 안내문을 프린터 하도록 하였다.
        end_function(baby, status, i) # end_function의 전달인자로 baby, status, i를 대입하여 해당 결과문을 프린터 하도록 하였다.
        print('\n결 론\n') # 결론을 프린터 하도록 하였다.
        count_function(i) # count_function함수를 이용하여 연애 종료까지의 기간에 따른 연애 등급을 프린터 하도록 하였다.
        break # 게임 종료 조건을 만족 시키면 while문을 빠져나오도록 하였다.
