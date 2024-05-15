import matplotlib.pyplot as plt

from skimage.morphology import convex_hull_image
from skimage import data
from skimage.util import invert, img_as_float

# the original image is inverted as the object must be white
image = invert(data.horse())

chull = convex_hull_image(image)

fig, axes = plt.subplots(1, 2, figsize=(8, 4))
ax = axes.ravel()

ax[0].set_title('Original Image')
ax[0].imshow(image, cmap='gray')
ax[0].axis('off')

ax[1].set_title('Convex Hull')
ax[1].imshow(chull, cmap='gray')
ax[1].axis('off')

plt.tight_layout()
plt.show()

# second plot for the difference
chull_diff = img_as_float(chull.copy())
chull_diff[image] = 2

fig, ax = plt.subplots()
ax.imshow(chull_diff, cmap='gray')
ax.set_title('Convex Hull Difference')
plt.show()

