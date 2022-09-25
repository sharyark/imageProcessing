import matplotlib.pyplot as plt
from skimage import io
from skimage.filters.rank import entropy
from skimage.morphology import disk
import numpy as np
from skimage.filters import threshold_otsu


img = io.imread('./A.png')
entropy_img = entropy(img,disk(10))
thresh = threshold_otsu(entropy_img)
Binary = thresh <= entropy_img
plt.imshow(entropy_img)
plt.imshow(Binary)
plt.show()
# print(entropy_img)
# print(thresh)