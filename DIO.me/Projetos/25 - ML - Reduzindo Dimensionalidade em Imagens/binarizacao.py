from pathlib import Path
from PIL import Image
import cv2


# NOTE: Aplicando a binarização com OpenCV
def binarizar_imagem_com_opencv(caminho_entrada: Path, caminho_saida: Path) -> None:

    # Carrega a imagem em escala de cinza
    imagem = cv2.imread(str(caminho_entrada), cv2.IMREAD_GRAYSCALE)

    # Aplicar binarização (threshold)
    _, binarizada = cv2.threshold(imagem, 127, 255, cv2.THRESH_BINARY)

    # Salva  a imagem binarizada
    cv2.imwrite(caminho_saida, binarizada)


# NOTE: Aplicando a binarização com Pillow
def binarizar_imagem_com_pillow(caminho_entrada: Path, caminho_saida: Path) -> None:

    # Carrega a imagem
    imagem = Image.open(str(caminho_entrada)).convert('L')  # Converte para escala de cinza

    # Aplicar binarização
    limiar = 127
    binarizada = imagem.point(lambda p: 255 if p > limiar else 0, mode='1')

    # Salvar a imagem
    binarizada.save(str(caminho_saida))


# NOTE: Aplicando a binarização sem bibliotecas
def binarizar_imagem_sem_bibliotecas(caminho_entrada: Path, caminho_saida: Path) -> None:

    def salvar_imagem(caminho: Path, largura: int, altura: int, pixels: bytes) -> None:

        # Criar arquivo PPM (formato simples para RGB)
        with open(caminho, "wb") as f:
            f.write(b"P5\n") 
            f.write(f"{largura} {altura}\n".encode())
            f.write(b"255\n")
            f.write(bytearray(pixels))


    def binarizar_imagem(caminho_entrada: Path, caminho_saida: Path, limiar=127) -> None:

        # Ler a imagem como tons de cinza (supondo um formato PGM simples)
        with open(caminho_entrada, "rb") as f:
            header = f.readline()      # P5
            dimensions = f.readline()  # Largura e altura
            max_value = f.readline()   # Máximo (255)
            
            largura, altura = map(int, dimensions.split())
            pixels = list(f.read())

        # Aplica a binarização
        pixels_binarizados = [255 if pixel > limiar else 0 for pixel in pixels]

        # Salva a imagem binarizada
        salvar_imagem(caminho_saida, largura, altura, pixels_binarizados)

    binarizar_imagem(caminho_entrada, caminho_saida)




if __name__ == '__main__':
    BASE_PATH = Path(__file__).parent
    JPG_IMG_PATH = BASE_PATH / 'imagens/jwst_first_image.jpg'
    PGM_IMG_PATH = BASE_PATH / 'imagens/jwst_first_image.pgm'

    binarizar_imagem_sem_bibliotecas(PGM_IMG_PATH, Path(BASE_PATH / 'imagem_binarizada_sem_bibliotecas.pgm'))
    binarizar_imagem_com_opencv(JPG_IMG_PATH, Path(BASE_PATH / 'imagem_binarizada_com_opencv.jpg'))
    binarizar_imagem_com_pillow(JPG_IMG_PATH, Path(BASE_PATH / 'imagem_binarizada_com_pillow.jpg'))
    