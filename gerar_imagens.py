import os
from PIL import Image, ImageDraw, ImageFont
import platform
def verificar_fonte(fonte_nome):
    caminhos_fontes = [
        "C:/Windows/Fonts",  # Caminho padrão no Windows
        "/usr/share/fonts",  # Caminho padrão no Linux
        "/Library/Fonts",    # Caminho padrão no macOS
    ]

    for caminho in caminhos_fontes:
        fonte_caminho = os.path.join(caminho, fonte_nome)
        if os.path.exists(fonte_caminho):
            print(f"Fonte encontrada: {fonte_caminho}")
            return fonte_caminho

    print(f"Fonte '{fonte_nome}' não encontrada no sistema.")
    return None

# Verificar se arial.ttf está disponível
fonte_caminho = verificar_fonte("arial.ttf")

# Testar carregamento da fonte com Pillow
if fonte_caminho:
    try:
        fonte = ImageFont.truetype(fonte_caminho, 72)
        print("Fonte carregada com sucesso!")
    except Exception as e:
        print(f"Erro ao carregar a fonte: {e}")
else:
    print("Usando fonte padrão do Pillow.")
    fonte = ImageFont.load_default()

# Criar o diretório "imagens" se não existir
if not os.path.exists('imagens'):
    os.makedirs('imagens')

# Tamanho da imagem de cada peça
tamanho_imagem = 100

# Fonte para desenhar as peças (ajuste o caminho se necessário)
try:
    fonte = ImageFont.truetype("arial.ttf", 72)
except IOError:
    fonte = ImageFont.load_default()

# Dicionário de peças e seus caracteres Unicode
pecas_unicode = {
    'P': '\u2659',  # Peão Branco
    'R': '\u2656',  # Torre Branca
    'N': '\u2658',  # Cavalo Branco
    'B': '\u2657',  # Bispo Branco
    'Q': '\u2655',  # Rainha Branca
    'K': '\u2654',  # Rei Branco
    'p': '\u265F',  # Peão Preto
    'r': '\u265C',  # Torre Preta
    'n': '\u265E',  # Cavalo Preto
    'b': '\u265D',  # Bispo Preto
    'q': '\u265B',  # Rainha Preta
    'k': '\u265A',  # Rei Preto
}

# Criar imagens para cada peça
for nome_arquivo, unicode_char in pecas_unicode.items():
    # Determinar a cor do fundo e do texto com base na peça
    if nome_arquivo.isupper():  # Peças brancas
        cor_fundo = (255, 255, 255)  # Fundo branco
        cor_texto = (0, 0, 0)        # Texto preto
    else:  # Peças pretas
        cor_fundo = (0, 0, 0)        # Fundo preto
        cor_texto = (255, 255, 255)  # Texto branco

    # Criar uma nova imagem
    imagem = Image.new('RGB', (tamanho_imagem, tamanho_imagem), cor_fundo)
    draw = ImageDraw.Draw(imagem)

    # Desenhar o caractere Unicode
    bbox = draw.textbbox((0, 0), unicode_char, font=fonte)
    largura_texto, altura_texto = bbox[2] - bbox[0], bbox[3] - bbox[1]
    posicao_texto = ((tamanho_imagem - largura_texto) // 2, (tamanho_imagem - altura_texto) // 2)
    draw.text(posicao_texto, unicode_char, fill=cor_texto, font=fonte)

    # Salvar a imagem
    caminho_arquivo = os.path.join('imagens', f'{nome_arquivo}.png')
    imagem.save(caminho_arquivo)

print("Imagens Unicode das peças criadas no diretório 'imagens'.")