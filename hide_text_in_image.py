from PIL import Image

def cacher_texte_dans_image(image_path, texte, image_de_sortie_path):
    image = Image.open(image_path)
    largeur, hauteur = image.size

    texte_binaire = ''.join(format(ord(char), '08b') for char in texte)
    texte_binaire += '1111111111111110'  

    index_texte = 0

    for y in range(hauteur):
        for x in range(largeur):
            pixel = list(image.getpixel((x, y)))

            for couleur in range(3):  
                if index_texte < len(texte_binaire):
                    pixel[couleur] = pixel[couleur] & 254 | int(texte_binaire[index_texte])
                    index_texte += 1

            image.putpixel((x, y), tuple(pixel))

            if index_texte >= len(texte_binaire):
                break

        if index_texte >= len(texte_binaire):
            break

    image.save(image_de_sortie_path)

image_source = "image.jpg"
texte_a_cacher = "Hello World!"
image_cachee = "hidden_image.png"

cacher_texte_dans_image(image_source, texte_a_cacher, image_cachee)
