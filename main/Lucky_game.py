from random import *
from time import sleep
import sys


def lucky_game():
    regras = ' '
    while regras != 's' and regras != 'n':
        regras = input('Deseja ler as regras? [S/N] ').lower().strip()
        if regras == 's':
            print('=' * 48 + ' R E G R A S ' + '=' * 48)
            print(' ')
            print(f'{">O sistema irá gerar, um número de 0 à 30.":^107}')
            print(f'{">O jogador e seu adversário irão escolher, também, um número de 0 à 30.":^107}')
            print(f'{">Quem chegar mais próximo do valor escolhido pelo sistema irá ganhar a aposta.":^107}')
            print(f'{">O jogador começa com um SALDO de R$500.":^107}')
            print(f'{">Em caso de vitória, o valor retornado é o valor dobrado da aposta, ou seja":^107}')
            print(f'{"se o jogador possui R$500, e apostar R$100, ele recebe os R$100 de volta e ":^107}')
            print(f'{"mais R$100 da mesa,totalizando R$200 e saldo R$600.":^107}')
            print(f'{">Em caso de derrota, o jogador perde o valor apostado, diminuindo o saldo.":^107}')
            print(f'{">Em caso de empate, o saldo permanece o mesmo e uma nova rodada de apostas surge.":^107}')
            print(f'{">O jogo acaba quando seu saldo chega a R$0.":^107}')
            print(f'{">Só é permitido apostar valores múltiplos de R$50, ou seja, R$50, R$100, R$550, R$2500...":^107}')
            print(' ')
            print('=' * 107)
            input('ENTER para sair e começar seu jogo: ')
    print('=' * 70)
    print(' ')
    print(f'{"BEM VINDO AO LUCKY GAME":^60}')
    print(' ')
    print('=' * 70)
    lista = ['JACK', 'ROBERT JOHNSON', 'HARRY KANE', 'JONAS KAHNWALD', 'DEXTER', 'HARLEY', 'JOHNNY DEPP', 'ALEX TURNER',
             'SIR. WINSTON', 'CHARLOTTE ROSE', ' MILES MORALES', 'JOHN TRAVOLTA', 'PHIL HELLMUTH', 'JASON STATHAM',
             'TERRY CREWS', 'LATRELL', 'CHRIS BROWN', 'MAJOR LAZER', 'FREDDIE MERCURY', 'AXEL ROSE', 'HIPPO CAMPUS',
             'REX ORANGE COUNTY', 'ADAM LEVINE', 'THOMAS SHELBY', 'ARTHUR SHELBY', 'CAPITÃO NASCIMENTO', 'ANDRÉ MATIAS']
    nomeadv = sample(lista, 1)
    sleep(1)
    print('=-=' * 20)
    print(f'{"VOCÊ ESTÁ CONTRA,": >33} ', end=' ')
    print(*nomeadv)
    print('=-=' * 20)
    sleep(0.5)
    print(' ')
    print('~~SÃO PERMITIDAS APENAS APOSTAS MÚLTIPLAS DE R$50~~')
    print('  Exemplos: R$50, R$150, R$400, R$650, R$3550... ')
    print(' ')
    saldo = 500
    print('-' * 20)
    print(f'SALDO: R${saldo}')
    print('-' * 20)
    while True:
        adver = randint(0, 30)
        pc = randint(0, 30)
        print(' ')
        quantia = int(input('Digite a quantia da aposta: '))
        while quantia % 50 != 0 or quantia <= 0:
            if quantia == 0:
                print('-' * 70)
                print('OPÇÃO INVÁLIDA. Não é permitido não apostar nenhum valor.')
                print('-' * 70)
            elif quantia < 0:
                print('-' * 70)
                print('OPÇÃO INVÁLIDA. Não é permitido apostar valores menores que R$50.')
                print('-' * 70)
            else:
                print('-' * 70)
                print('OPÇÃO INVÁLIDA. SOMENTE APOSTAS MÚLTIPLAS DE R$50 SÃO ACEITAS')
                print('-' * 70)
            quantia = int(input('Digte a quantia da aposta: '))
        while quantia > saldo:
            print('~' * 70)
            print(f'{"INVÁLIDO":^70}')
            print('~' * 70)
            print(f'Valor apostado (R${quantia}) maior que o saldo atual (R${saldo}).')
            quantia = int(input('Digte a quantia da aposta: '))
        num = int(input('Escolha um número de 0 à 30: '))
        while num > 30 or num < 0:
            num = int(input('Escolha um número de 0 à 30: '))
        print(' ')
        sleep(0.3)
        print('PROCESSANDO...')
        sleep(0.7)
        print(' ')
        print('=-=' * 30)
        print(f'>O computador escolheu --> {pc}')
        print(*nomeadv, end=' ')
        print(f'escolheu --> {adver}')
        result1 = num - pc
        result2 = adver - pc
        if abs(result1) < abs(result2):
            newsaldo = saldo + quantia
            saldo = newsaldo
            print(f'>VOCÊ GANHOU a aposta. '
                  f'\nSeu valor escolhido chegou mais próximo do escolhido pelo sistema')
            print(f'>Você: de {num} para {pc} são [ {abs(result1)} ] números.')
            print('>', end='')
            print(*nomeadv, end=': ')
            print(f'de {adver} para {pc} são [ {(abs(result2))} ].')
            print('-' * 30)
            print(f'>NOVO SALDO: R${newsaldo}')
            print('-' * 30)
        elif abs(result1) > abs(result2):
            print(f'>VOCÊ PERDEU a aposta. '
                  f'\nO valor escolhido pelo seu adversário foi mais próximo do escolhido pelo sistema')
            print(f'>Você: de {num} para {pc} são [ {abs(result1)} ] números.')
            print('>', end='')
            print(*nomeadv, end=': ')
            print(f'de {adver} para {pc} são [ {(abs(result2))} ].')
            newsaldo = saldo - quantia
            saldo = newsaldo
            print('-' * 30)
            print(f'>NOVO SALDO: R${newsaldo}')
            print('-' * 30)
        elif abs(result1) == abs(result2):
            print('>EMPATE')
            print(f'Seu saldo continuou o mesmo: R${saldo}')
        if saldo == 0:
            sleep(5)
            print('#' * 50)
            print(f'{"VOCÊ FALIU!!!":^50}')
            print('#' * 50)
            keep = ' '
            while keep != 's' and keep != 'n':
                keep = input('Reiniciar o jogo? [S/N]: ').lower().strip()
            if keep == 's':
                lucky_game()
            else:
                print('Muito obrigado pelas apostas :) \nFINALIZANDO...')
                input(' ')
                sys.exit()
        print('=-=' * 30)


if __name__ == '__main__':
    lucky_game()
