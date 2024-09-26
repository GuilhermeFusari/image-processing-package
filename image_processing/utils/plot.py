import matplotlib.pyplot as plt  # Biblioteca para gerar gráficos e visualizações

# Função para exibir uma única imagem
def plot_image(image):
    plt.figure(figsize=(12, 4))  # Define o tamanho da figura
    plt.imshow(image, cmap='gray')  # Exibe a imagem; 'cmap' define a coloração (usando escala de cinza)
    plt.axis('off')  # Remove os eixos da imagem
    plt.show()  # Mostra a imagem na tela

# Função para exibir múltiplas imagens lado a lado e rotulá-las
def plot_result(*args):
    number_images = len(args)  # Conta o número de imagens passadas como argumento
    fig, axis = plt.subplots(nrows=1, ncols=number_images, figsize=(12, 4))  # Cria uma figura com subplots para cada imagem
    names_lst = ['Image {}'.format(i) for i in range(1, number_images)]  # Cria uma lista de nomes para as imagens
    names_lst.append('Result')  # O último título será 'Result'
    
    # Itera sobre cada eixo do subplot, nome e imagem ao mesmo tempo
    for ax, name, image in zip(axis, names_lst, args):
        ax.set_title(name)  # Define o título de cada subplot
        ax.imshow(image, cmap='gray')  # Exibe a imagem no subplot usando escala de cinza
        ax.axis('off')  # Remove os eixos de cada imagem
    
    fig.tight_layout()  # Ajusta o layout da figura para evitar sobreposição
    plt.show()  # Mostra a figura com todas as imagens

# Função para exibir o histograma de uma imagem RGB separadamente para cada canal de cor
def plot_histogram(image):
    fig, axis = plt.subplots(nrows=1, ncols=3, figsize=(12, 4), sharex=True, sharey=True)  # Cria subplots para os três canais de cor
    color_lst = ['red', 'green', 'blue']  # Define os nomes das cores para os canais RGB
    
    # Itera sobre os índices dos canais de cor, eixos e nomes das cores ao mesmo tempo
    for index, (ax, color) in enumerate(zip(axis, color_lst)):
        ax.set_title('{} histogram'.format(color.title()))  # Define o título de cada subplot com o nome da cor
        ax.hist(image[:, :, index].ravel(), bins=256, color=color, alpha=0.8)  # Cria o histograma para o canal de cor atual
        
    fig.tight_layout()  # Ajusta o layout da figura
    plt.show()  # Mostra o histograma
