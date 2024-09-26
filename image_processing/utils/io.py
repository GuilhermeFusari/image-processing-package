from skimage.io import imread, imsave  # Funções para ler e salvar imagens

# Função para ler uma imagem de um arquivo
# 'path' é o caminho da imagem, 'is_gray' é um booleano para indicar se a imagem deve ser carregada em tons de cinza
def read_image(path, is_gray=False):
    # Lê a imagem do caminho especificado. Se 'is_gray' for True, a imagem será carregada em tons de cinza
    image = imread(path, as_gray=is_gray)
    return image  # Retorna a imagem carregada

# Função para salvar uma imagem em um arquivo
# 'image' é a imagem a ser salva, e 'path' é o caminho onde a imagem será armazenada
def save_image(image, path):
    # Salva a imagem no caminho especificado
    imsave(path, image)
