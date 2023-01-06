import random
num = 0

def brGame():
    global numbers
    while True:
        numbers = input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : ')
        if numbers.isdigit() == True and 1 <= int(numbers) <= 3:
            break
        elif numbers.isdigit() == False:
            print('정수를 입력하세요')
        else:
            print('1, 2, 3 중 하나를 입력하세요')
    numbers = int(numbers)

while True:
    
    numCom = random.randint(1, 3)
    for i in range(numCom):
        num+=1
        print('computer', num)
        if num == 31:
            break
    if num == 31:
        print('player win!')
        break
 
    brGame()
    for i in range(numbers):
        num+=1
        print('player', num)
        if num == 31:
            break
    if num == 31:
        print('computer win!')
        break