import matplotlib.image as mg
import matplotlib.pyplot as plt


img = mg.imread('./a.jpg')
plt.imshow(img)
plt.show()
# print(img)

a = input('enter for terminate')