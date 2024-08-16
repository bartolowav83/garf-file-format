from PIL import Image
import struct

def garf_to_png(garf_file, png_file):
    # Open the .garf file
    with open(garf_file, 'rb') as f:
        # Read and decompose the header
        header = f.read(16)  # 4s for 'GARF', 4x3 for width, height and garfiance lol
        _, width, height, _ = struct.unpack('4sIII', header)
        
        # Read pixels
        pixels = []
        for _ in range(width * height):
            pixel_data = f.read(3)  # Lire les données RGB
            pixels.append(tuple(struct.unpack('BBB', pixel_data)))
    
    # Create PNG image from pixels
    img = Image.new('RGB', (width, height))
    img.putdata(pixels)
    img.save(png_file)
    
    print(f"Conversion de {garf_file} en {png_file} terminée.")

# Example of use
garf_to_png('output.garf', 'output.png')
