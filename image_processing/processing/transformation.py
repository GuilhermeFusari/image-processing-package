from skimage.transform import resize  # Função para redimensionar imagens

# Função para redimensionar uma imagem com base em uma proporção fornecida
def resize_image(image, proportion):
    # Garante que a proporção esteja entre 0 e 1. Se não, levanta um erro.
    assert 0 <= proportion <= 1, "Specify a valid proportion between 0 and 1."
    
    # Calcula a nova altura e largura da imagem com base na proporção fornecida
    height = round(image.shape[0] * proportion)  # Calcula a nova altura (shape[0] representa o número de linhas, ou altura, da imagem)
    width = round(image.shape[1] * proportion)   # Calcula a nova largura (shape[1] representa o número de colunas, ou largura, da imagem)
    
    # Redimensiona a imagem para as novas dimensões calculadas
    # O parâmetro 'anti_aliasing=True' ajuda a suavizar a imagem redimensionada, reduzindo possíveis distorções
    image_resized = resize(image, (height, width), anti_aliasing=True)
    
    # Retorna a imagem redimensionada
    return image_resized
