from rembg import remove
from PIL import Image

# Testing
input = Image.open('dog.jpg')

output = remove(input)

output.save('out.png')
# It works