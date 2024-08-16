from PIL import Image
import struct

def png_to_garf(png_file, garf_file):
    # Ouvrir l'image PNG
    img = Image.open(png_file)
    img = img.convert("RGB")  # Convertir en RGB si nécessaire
    width, height = img.size
    pixels = list(img.getdata())
    
    # Créer un en-tête pour le fichier .garf
    header = struct.pack('4sIII', b'GARF', width, height, 42)  # 42 est le niveau de garfiance arbitraire
    
    # Écrire l'en-tête et les pixels dans le fichier .garf
    with open(garf_file, 'wb') as f:
        f.write(header)
        for pixel in pixels:
            f.write(struct.pack('BBB', *pixel))  # Stocke chaque pixel en RGB
    
    print(f"Conversion de {png_file} en {garf_file} terminée.")

# Exemple d'utilisation
png_to_garf('input.png', 'output.garf')
