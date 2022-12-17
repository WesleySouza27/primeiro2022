num1 = int(input('digite um numero!'))
num2 = int(input('digite outro numero!'))
num3 = int(input('último numero!!'))

if num1 > num2 and num1 > num3:
    print(f'{num1} é o maior numero!')
elif num2 > num1 and num2 > num3:
    print(f'{num2} é o maior numero!')
elif num3 > num1 and num3 > num2:
    print(f'{num3} é o maior numero!')

if num1 < num2 and num1 < num3:
    print(f'{num1} é o menor numero')
elif num2 < num1 and num2 < num3:
    print(f'{num2} é o menor numero!')
elif num3 < num1 and num3 < num2:
    print(f'{num3} é o menor numero!')
