from pathlib import Path
from PIL import Image
import cv2
import struct


# NOTE: Aplicando a conversão para escala de cinza com OpenCV
def escala_de_cinza_com_opencv(caminho_entrada: Path, caminho_saida: Path) -> None:

    # Carrega a imagem em escala de cinza
    imagem = cv2.imread(str(caminho_entrada))

    # Converte para escala de cinza
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    # Salva  a imagem binarizada
    cv2.imwrite(caminho_saida, imagem_cinza)


# NOTE: Aplicando a conversão para escala de cinza com Pillow
def escala_de_cinza_com_pillow(caminho_entrada: Path, caminho_saida: Path) -> None:

    # Carrega a imagem
    imagem = Image.open(str(caminho_entrada))

    # Converte para escala de cinza
    imagem_cinza = imagem.convert('L')

    # Salvar a imagem
    imagem_cinza.save(str(caminho_saida))


# NOTE: Aplicandoa conversão para escala de cinza sem bibliotecas
def escala_de_cinza_sem_bibliotecas(caminho_entrada: Path, caminho_saida: Path) -> None:

    def ler_bmp(caminho: Path):
        # Abrir o arquivo BMP em modo binário
        with open(caminho, 'rb') as f:
            dados = f.read()
        
        # Cabeçalho do BMP
        tipo = dados[:2].decode()  # Deve ser 'BM'
        if tipo != 'BM':
            raise ValueError("O arquivo não é um BMP válido.")

        # Obter informações do cabeçalho
        tamanho = struct.unpack('<I', dados[2:6])[0]  # Tamanho do arquivo
        offset = struct.unpack('<I', dados[10:14])[0]  # Offset onde os dados da imagem começam
        largura = struct.unpack('<I', dados[18:22])[0]
        altura = struct.unpack('<I', dados[22:26])[0]
        bpp = struct.unpack('<H', dados[28:30])[0]  # Bits por pixel

        if bpp != 24:
            raise ValueError("Apenas imagens BMP de 24 bits são suportadas.")

        # Obter os pixels
        pixels = bytearray(dados[offset:])

        return largura, altura, pixels, dados[:offset]


    def converter_para_cinza(largura, altura, pixels):
        # Converter cada pixel RGB para tons de cinza
        for i in range(0, len(pixels), 3):
            r, g, b = pixels[i+2], pixels[i+1], pixels[i]  # BMP usa ordem BGR
            # Fórmula para escala de cinza
            gray = int(0.299 * r + 0.587 * g + 0.114 * b)
            pixels[i] = pixels[i+1] = pixels[i+2] = gray  # Substituir pelos valores de cinza
        return pixels


    def salvar_bmp(caminho, cabecalho, pixels):
        # Salvar os dados de volta no formato BMP
        with open(caminho, 'wb') as f:
            f.write(cabecalho + pixels)


    largura, altura, pixels, cabecalho = ler_bmp(caminho_entrada)
    pixels_cinza = converter_para_cinza(largura, altura, pixels)
    salvar_bmp(caminho_saida, cabecalho, pixels_cinza)




if __name__ == '__main__':
    BASE_PATH = Path(__file__).parent
    JPG_IMG_PATH = BASE_PATH / 'imagens/jwst_first_image.jpg'
    BMP_IMG_PATH = BASE_PATH / 'imagens/jwst_first_image.bmp'

    escala_de_cinza_sem_bibliotecas(BMP_IMG_PATH, Path(BASE_PATH / 'imagem_em_escala_de_cinza_sem_bibliotecas.bmp'))
    escala_de_cinza_com_opencv(JPG_IMG_PATH, Path(BASE_PATH / 'imagem_em_escala_de_cinza_com_opencv.jpg'))
    escala_de_cinza_com_pillow(JPG_IMG_PATH, Path(BASE_PATH / 'imagem_em_escala_de_cinza_com_pillow.jpg'))
    