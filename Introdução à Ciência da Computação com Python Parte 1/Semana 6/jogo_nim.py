# Autor: Wirley Almeida
# 18/11/2021
# Introdução à Ciência da Computação com Python Parte 1
# Semana 6
# Jogo do NIM

def computador_escolhe_jogada(n, m):
    jogada_computador = 1
    indicador_de_passagem = True
    while jogada_computador < m and indicador_de_passagem:
        if (n - jogada_computador) % (m+1) == 0:
            indicador_de_passagem = False
        else:
            jogada_computador = jogada_computador + 1
    
    if jogada_computador == 1:
        print('O computador tirou uma peça.')
    else:
        print('O computador tirou ' + str(jogada_computador) + ' peças.')
    
    return jogada_computador


def usuario_escolhe_jogada(n, m):
    jogada_usuario = int(input('Quantas peças você vai tirar? '))
    while jogada_usuario < 1 or jogada_usuario > m:
        print('Oops! Jogada inválida! Tente de novo.')
        jogada_usuario = int(input('Quantas peças você vai tirar? '))
    
    if jogada_usuario == 1:
        print('Você tirou uma peça.')
    else:
        print('Você tirou '+ str(jogada_usuario) + ' peças.')
    
    return jogada_usuario
    

def partida():
    n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogada? '))
    comeca = True

    if n % (m+1) == 0:
        print('Você começa!')
    else:
        print('Computador começa!')
        comeca = False
    
    while n != 0:
        if comeca:
            jogada = usuario_escolhe_jogada(n, m)
            comeca = False            
        else:
            jogada = computador_escolhe_jogada(n, m)
            comeca = True
        
        n = n - jogada
        if n == 0:
            print('Fim do jogo! O computador ganhou!')
        elif n == 1:
            print('Agora resta apenas uma peça no tabuleiro.')
        else:
            print('Agora restam ' + str(n) + ' peças no tabuleiro.')
        
    

def campeonato():
    i = 1
    computador = 0
    usuario = 0
    while i <= 3:
        print('**** Rodada ' + str(i) + ' ****')
        partida()
        i = i + 1
        computador = computador + 1

    print('**** Final do campeonato! ****')
    print('Placar: Você', usuario, 'X', computador, 'Computador')

print('Bem-vindo ao jogo do NIM! Escolha: \n')
print('1 - para jogar uma partida isolada')
print('2 - para jogar um campeonato')
opcao = int(input())

if opcao == 1:
    print('\nVocê escolheu uma partida isolada!')
    partida()
else:
    print('\nVocê escolheu um campeonato!')
    campeonato()
