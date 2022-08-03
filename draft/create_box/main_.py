# !pip install matplotlib
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw



img = Image.open('white_img.png')


coord = [[1,1], [2,1], [2,2], [1,2], [0.5,1.5]]
coord.append(coord[0]) # repeat the first point to create a 'closed loop'

xs, ys = zip(*coord) # create lists of x and y values
plt.imshow(img)
plt.show()
plt.figure()
plt.plot(xs,ys)
