import numpy as np
from skimage.color import rgb2gray  # Função para converter imagens de RGB para tons de cinza
from skimage.exposure import match_histograms  # Função para realizar a correspondência de histogramas
from skimage.metrics import structural_similarity  # Função para calcular a similaridade estrutural entre duas imagens

# Função para encontrar a diferença entre duas imagens
def find_difference(image1, image2):
    # Verifica se as duas imagens têm as mesmas dimensões, caso contrário, levanta um erro
    assert image1.shape == image2.shape, "Specify 2 images with the same shape."
    
    # Converte as imagens de RGB para tons de cinza
    gray_image1 = rgb2gray(image1)
    gray_image2 = rgb2gray(image2)
    
    # Calcula o índice de similaridade estrutural (SSIM) entre as duas imagens em tons de cinza
    # O argumento 'full=True' faz com que a função retorne a imagem de diferença
    (score, difference_image) = structural_similarity(gray_image1, gray_image2, full=True)
    
    # Exibe o grau de similaridade entre as imagens (quanto mais próximo de 1, mais similares)
    print("Similarity of the images:", score)
    
    # Normaliza a imagem de diferença para que os valores estejam entre 0 e 1, o que facilita a visualização
    normalized_difference_image = (difference_image - np.min(difference_image)) / (np.max(difference_image) - np.min(difference_image))
    
    # Retorna a imagem de diferença normalizada
    return normalized_difference_image

# Função para transferir o histograma de uma imagem para outra
def transfer_histogram(image1, image2):
    # Usa a função 'match_histograms' para ajustar os valores de cores de 'image1' para combinar com os de 'image2'
    # O parâmetro 'multichannel=True' indica que as imagens possuem múltiplos canais (por exemplo, R, G e B)
    matched_image = match_histograms(image1, image2, multichannel=True)
    
    # Retorna a imagem com o histograma ajustado
    return matched_image
