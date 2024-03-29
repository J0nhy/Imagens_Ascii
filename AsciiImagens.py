import PIL

#Caracteres Ascii
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

#Redimensionar as imagens
def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return(resized_image)

#Converter cada pixel para escala preto e branco
def grayify(image):
    grayscale_image = image.convert("L")
    return(grayscale_image)

#Converter os pixeis para caracteres Ascii
def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])

def main(new_width=100):
    #Tentativa de abrir a imagem
    path = input("Insira um directório válido:\n")
    try:
        image = PIL.Image.open(path)
    except:
        print(path, "não é um directório válido")

    new_image_data = pixels_to_ascii(grayify(resize_image(image)))

    #formato
    pixel_count = len(new_image_data)
    ascii_image = "\n".join(new_image_data[i:(i+new_width)] for i in range(0, pixel_count, new_width))

    #Executar resultado
    print(ascii_image)

    #Salvar resultado
    with open(ascii_image.txt, "w") as f:
        f.write(ascii_image)

main()
        