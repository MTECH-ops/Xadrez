import pygame
import sys

# Inicialização do pygame
pygame.init()

# Tamanho da tela e do quadrado
tamanho_tela = 800
tamanho_quadrado = tamanho_tela // 8

# Cores
cor_branca = (255, 255, 255)
cor_preta = (0, 0, 0)
cor_destaque = (255, 0, 0)

# Variável global para controlar o turno (True para brancas, False para pretas)
turno_brancas = True

# Tabuleiro inicial
tabuleiro = [
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
]

# Tela do jogo
tela = pygame.display.set_mode((tamanho_tela, tamanho_tela))
pygame.display.set_caption("Jogo de Xadrez")

# Função para carregar as imagens das peças
def carregar_imagens():
    pecas = {}
    pecas['P'] = pygame.image.load('imagens/P.png')
    pecas['p'] = pygame.image.load('imagens/p.png')
    pecas['R'] = pygame.image.load('imagens/R.png')
    pecas['r'] = pygame.image.load('imagens/r.png')
    pecas['N'] = pygame.image.load('imagens/N.png')
    pecas['n'] = pygame.image.load('imagens/n.png')
    pecas['B'] = pygame.image.load('imagens/B.png')
    pecas['b'] = pygame.image.load('imagens/b.png')
    pecas['Q'] = pygame.image.load('imagens/Q.png')
    pecas['q'] = pygame.image.load('imagens/q.png')
    pecas['K'] = pygame.image.load('imagens/K.png')
    pecas['k'] = pygame.image.load('imagens/k.png')

    # Redimensionar as imagens para caber nos quadrados
    for chave in pecas:
        pecas[chave] = pygame.transform.scale(pecas[chave], (tamanho_quadrado, tamanho_quadrado))
    return pecas

# Inicializar as imagens
imagens_pecas = carregar_imagens()

# Função para desenhar o tabuleiro
def desenhar_tabuleiro():
    for linha in range(8):
        for coluna in range(8):
            cor = cor_branca if (linha + coluna) % 2 == 0 else cor_preta
            pygame.draw.rect(tela, cor, (coluna * tamanho_quadrado, linha * tamanho_quadrado, tamanho_quadrado, tamanho_quadrado))

    # Desenhar as peças
    for linha in range(8):
        for coluna in range(8):
            peca = tabuleiro[linha][coluna]
            if peca != ' ':
                tela.blit(imagens_pecas[peca], (coluna * tamanho_quadrado, linha * tamanho_quadrado))

# Função para converter coordenadas do mouse para o tabuleiro
def posicao_mouse_para_tabuleiro(pos):
    x, y = pos
    return y // tamanho_quadrado, x // tamanho_quadrado

# Função para verificar se o movimento é válido (lógica básica)
def movimento_valido(origem, destino, peca):
    # Exemplo básico: permitir qualquer movimento para peças não vazias
    linha_origem, coluna_origem = origem
    linha_destino, coluna_destino = destino
    return tabuleiro[linha_destino][coluna_destino] == ' ' or tabuleiro[linha_destino][coluna_destino].islower() != peca.islower()

# Função para mover uma peça
def mover_peça(origem, destino):
    global turno_brancas
    linha_origem, coluna_origem = origem
    linha_destino, coluna_destino = destino

    peca = tabuleiro[linha_origem][coluna_origem]
    if (peca.isupper() and turno_brancas) or (peca.islower() and not turno_brancas):
        if movimento_valido(origem, destino, peca):
            tabuleiro[linha_destino][coluna_destino] = peca
            tabuleiro[linha_origem][coluna_origem] = ' '
            turno_brancas = not turno_brancas  # Alternar turno

# Loop principal do jogo
def main():
    global turno_brancas
    rodando = True
    peca_selecionada = None

    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                linha, coluna = posicao_mouse_para_tabuleiro(pos)

                if peca_selecionada:
                    # Tentar mover a peça
                    mover_peça(peca_selecionada, (linha, coluna))
                    peca_selecionada = None
                else:
                    # Selecionar uma peça
                    peca_selecionada = (linha, coluna)

        # Desenhar o tabuleiro
        desenhar_tabuleiro()

        # Destacar peça selecionada
        if peca_selecionada:
            linha, coluna = peca_selecionada
            pygame.draw.rect(tela, cor_destaque, (coluna * tamanho_quadrado, linha * tamanho_quadrado, tamanho_quadrado, tamanho_quadrado), 5)

        pygame.display.flip()

# Iniciar o jogo
main()