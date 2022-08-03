import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
from matplotlib.patches import Polygon
import numpy as np

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

fig, ax = plt.subplots(1)

polygon = Polygon(np.random.rand(6, 2), closed=True, alpha=1)

collection = PatchCollection([polygon])

ax.add_collection(collection)

plt.show()