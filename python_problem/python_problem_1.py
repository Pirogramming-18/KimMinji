num = 0

while True:
    num = input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : ')
    if num.isdigit() == True and 1 <= int(num) <= 3:
        break
    elif num.isdigit() == False:
        print('정수를 입력하세요')
    else:
        print('1, 2, 3 중 하나를 입력하세요')