num = 0

while True:
    numbers = input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : ')
    if numbers.isdigit() == True and 1 <= int(numbers) <= 3:
        break
    elif numbers.isdigit() == False:
        print('정수를 입력하세요')
    else:
        print('1, 2, 3 중 하나를 입력하세요')

numbers = int(numbers)
for num in range(numbers):
    num+=1
    print('playerA :', num)