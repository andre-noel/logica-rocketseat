tabuleiro = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
    ]

def exibeTabuleiro():
    for linha in tabuleiro:
        print('|'.join(linha))
        print('-' * 5)

def jogada(linha, coluna):
    if (
        not (0 <= linha <= 2) or
        not (0 <= coluna <= 2) or
        tabuleiro[linha][coluna] != ' '
    ):
        print('Jogada inválida')
        return jogador
    tabuleiro[linha][coluna] = jogador
    return 'O' if jogador == 'X' else 'X'

def temGanhador():
    """ Verifica as linhas """
    for linha in range(0, 3):
        if (
            tabuleiro[linha][0] != ' ' and
            tabuleiro[linha][0] == tabuleiro[linha][1] and
            tabuleiro[linha][0] == tabuleiro[linha][2]
        ):
            print(f'{tabuleiro[linha][0]} ganhou!!!')
            return True

    """ Verifica as colunas """
    for coluna in range(0, 3):
        if (
            tabuleiro[0][coluna] != ' ' and
            tabuleiro[0][coluna] == tabuleiro[1][coluna] and
            tabuleiro[0][coluna] == tabuleiro[2][coluna]
        ):
            print(f'{tabuleiro[0][coluna]} ganhou!!!')
            return True
        
    """ Verifica as diagonais """
    if tabuleiro[1][1] != ' ' and (
        (    
            tabuleiro[0][0] == tabuleiro[1][1] and
            tabuleiro[1][1] == tabuleiro[2][2]
        ) or (
            tabuleiro[0][2] == tabuleiro[1][1] and
            tabuleiro[1][1] == tabuleiro[2][0]
        )
    ):
        print(f'{tabuleiro[1][1]} ganhou!!!')
        return True
    return False

def temEmpate():
    for linha in range(0, 3):
        for coluna in range(0, 3):
            if tabuleiro[linha][coluna] == ' ':
                return False
    print('O jogo acabou empatado!')
    return True

jogo = True
jogador = 'X'
while jogo:
    print(f'Jogador da vez: {jogador}')
    try:
        posicaoX = int(input('Digite a coluna da jogada: '))
        posicaoY = int(input('Digite a linha da jogada: '))
        jogador = jogada(posicaoX, posicaoY)
    except (ValueError, IndexError) as e:
        print(f'Entrada inválida!')
        print(f'Digite apenas números entre 0 e 2')
    jogo = not (temGanhador() or temEmpate())
    exibeTabuleiro()