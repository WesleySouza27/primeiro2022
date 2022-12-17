ano = int(input('qual é o ano? '))
'''if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print('o ano que voçê informou é bisexto!')
        else:
            print('o ano não é bisexto!')
    else:
        print('o ano que voçê digitou é bisexto!')
else:
    print('o ano não é bisexto!')'''
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'o ano {ano} é bisexto')
else:
    print(f'o ano {ano} não é bisexto')
