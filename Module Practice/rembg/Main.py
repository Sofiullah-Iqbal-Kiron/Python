from rembg import remove
from PIL import Image

inputFile = "input.png"
outFile = "output.png"
input = Image.open(inputFile)
output = remove(input)
output.save(outFile)
input.close()
