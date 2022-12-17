import random
print(35 * '=')
print('vamos jogar pedra papel e tesoura?')
print(35 * '=')
print('digite 1 para pedra!')
print('digite 2 para papel!')
print('digite 3 para tesoura!')
print(40 * '=')
resposta = int(input('digite o numero referente a sua escolha: '))
pedra = 1
papel = 2
tesoura = 3
lista = [pedra, papel, tesoura]
escolhido = random.choice(lista)
if resposta == pedra and escolhido != papel:
    print('você venceu meus parabéns!')
elif resposta == papel and escolhido != tesoura:
    print('você venceu meus parabéns!')
elif resposta == tesoura and escolhido != pedra:
    print('você venceu meus parabéns!')
else:
    print('você perdeu sinto muito rsrs!')

