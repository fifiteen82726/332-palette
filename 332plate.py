from PIL import Image
import numpy as np

class ColorQuantization():
  def __init__(self, img):
    self.block_value = [
      [16, 48, 80, 112, 144, 176, 208, 240],
      [16, 48, 80, 112, 144, 176, 208, 240],
      [32, 96, 160, 192]
    ]
    self.img = img
    self.quantilize()

  def quantilize(self):
    rows, cols, d = self.img.shape
    img = np.copy(self.img)
    for i in xrange(rows):
      for j in xrange(cols):
        r, g, b = self.img[i][j]
        r = self.block_value[0][int(r / 32)]
        g = self.block_value[1][int(g / 32)]
        b = self.block_value[2][int(b / 64)]
        img[i][j] = [r, g, b]

    self.save_image(img)

  def save_image(self, img):
    name = 'image332.jpg'
    Image.fromarray(img).save(name)

image = np.array(Image.open('color-blue.jpg').convert('RGB'))
ColorQuantization(image)
