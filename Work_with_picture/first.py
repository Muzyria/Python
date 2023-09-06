from rembg import remove
from PIL import Image

input_path = 'my_picture.jpg'
output_path = 'output_1.png'

input = Image.open(input_path)
output = remove(input)
output.save(output_path)
