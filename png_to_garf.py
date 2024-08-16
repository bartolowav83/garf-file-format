from PIL import Image
import struct

def png_to_garf(png_file, garf_file):
    # Open PNG image
    img = Image.open(png_file)
    img = img.convert("RGB")  # Convert to RGB if necessary
    width, height = img.size
    pixels = list(img.getdata())
    
    # Create a header for the .garf file
    header = struct.pack('4sIII', b'GARF', width, height, 42)  # 42 is the arbitrary trust level
    
    # Write header and pixels to .garf file
    with open(garf_file, 'wb') as f:
        f.write(header)
        for pixel in pixels:
            f.write(struct.pack('BBB', *pixel))  # Stores each pixel in RGB
    
    print(f"Converted {png_file} into {garf_file} finished.")

# Example of use
png_to_garf('input.png', 'output.garf')
