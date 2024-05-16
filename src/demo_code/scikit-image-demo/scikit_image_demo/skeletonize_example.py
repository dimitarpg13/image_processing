from skimage.morphology import skeletonize
from skimage import data
import matplotlib.pyplot as plt
from skimage.util import invert

# invert the horse image
image = invert(data.horse())

# perform skeletonization
skeleton = skeletonize(image)

# display results
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(8, 4), sharex=True, sharey=True)

ax = axes.ravel()

ax[0].imshow(image, cmap='gray')
ax[0].axis('off')
ax[0].set_title('Original Image', fontsize=20)

ax[1].imshow(skeleton, cmap='gray')
ax[1].axis('off')
ax[1].set_title('Skeletonized Image', fontsize=20)

fig.tight_layout()
plt.show()


