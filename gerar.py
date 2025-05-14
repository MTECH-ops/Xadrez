from PIL import Image, ImageDraw, ImageFont

# Função para desenhar as peças em estilo minimalista
def draw_chess_piece(piece, color, size=(100, 100)):
    # Criar uma imagem em branco
    img = Image.new('RGBA', size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)

    # Definir cores para as peças
    if color == 'black':
        piece_color = (0, 0, 0)
    else:
        piece_color = (255, 255, 255)

    # Desenho das peças (formas geométricas simplificadas)
    if piece == 'king':
        # Rei - círculo com uma cruz
        draw.ellipse([25, 10, 75, 60], fill=piece_color)
        draw.line((50, 10, 50, 60), fill=(255, 255, 255) if color == 'black' else (0, 0, 0), width=3)
        draw.line((35, 20, 65, 20), fill=(255, 255, 255) if color == 'black' else (0, 0, 0), width=3)

    elif piece == 'queen':
        # Rainha - círculo simples
        draw.ellipse([25, 25, 75, 75], fill=piece_color)

    elif piece == 'rook':
        # Torre - retângulo com um topo simples
        draw.rectangle([25, 30, 75, 75], fill=piece_color)
        draw.rectangle([30, 20, 70, 30], fill=piece_color)

    elif piece == 'bishop':
        # Bispo - cúpula com um traço vertical
        draw.ellipse([25, 10, 75, 60], fill=piece_color)
        draw.line((50, 20, 50, 60), fill=(255, 255, 255) if color == 'black' else (0, 0, 0), width=3)

    elif piece == 'knight':
        # Cavalo - um triângulo simples representando o pescoço
        draw.polygon([(50, 20), (35, 50), (65, 50)], fill=piece_color)

    elif piece == 'pawn':
        # Peão - círculo simples no topo
        draw.ellipse([40, 10, 60, 30], fill=piece_color)
        draw.rectangle([45, 30, 55, 75], fill=piece_color)

    return img

# Função para salvar as imagens das peças
def save_piece_images():
    pieces = ['king', 'queen', 'rook', 'bishop', 'knight', 'pawn']
    colors = ['black', 'white']

    for color in colors:
        for piece in pieces:
            img = draw_chess_piece(piece, color)
            img.save(f"{piece}_{color}.png")

# Chama a função para gerar as imagens
save_piece_images()
