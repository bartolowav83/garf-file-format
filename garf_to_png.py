from PIL import Image
import struct

def garf_to_png(garf_file, png_file):
    # Ouvrir le fichier .garf
    with open(garf_file, 'rb') as f:
        # Lire et décomposer l'en-tête
        header = f.read(16)  # 4s pour 'GARF', 4x3 pour largeur, hauteur et garfiance
        _, width, height, _ = struct.unpack('4sIII', header)
        
        # Lire les pixels
        pixels = []
        for _ in range(width * height):
            pixel_data = f.read(3)  # Lire les données RGB
            pixels.append(tuple(struct.unpack('BBB', pixel_data)))
    
    # Créer l'image PNG à partir des pixels
    img = Image.new('RGB', (width, height))
    img.putdata(pixels)
    img.save(png_file)
    
    print(f"Conversion de {garf_file} en {png_file} terminée.")

# Exemple d'utilisation
garf_to_png('output.garf', 'output.png')
