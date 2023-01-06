num = 0

def playerA():
    global num
    while True:
        numbers = input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : ')
        if numbers.isdigit() == True and 1 <= int(numbers) <= 3:
            break
        elif numbers.isdigit() == False:
            print('정수를 입력하세요')
        else:
            print('1, 2, 3 중 하나를 입력하세요')
    numbers = int(numbers)
    for i in range(numbers):
        num+=1
        print('playerA :', num)
        if num == 31:
            break

def playerB():
    global num    
    while True:
        numbers = input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : ')
        if numbers.isdigit() == True and 1 <= int(numbers) <= 3:
            break
        elif numbers.isdigit() == False:
            print('정수를 입력하세요')
        else:
            print('1, 2, 3 중 하나를 입력하세요')
    numbers = int(numbers)
    for i in range(numbers):
        num+=1
        print('playerB :', num)
        if num == 31:
            break

while True:
    playerA()
    if num == 31:
        break
    playerB()
    if num == 31:
        break