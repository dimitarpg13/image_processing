import matplotlib.pyplot as plt

from skimage import data, color
from skimage.transform import rescale, resize, downscale_local_mean

image = color.rgb2gray(data.astronaut())

image_rescaled = rescale(image, 0.25, anti_aliasing=False)

image_resized = resize(
    image, (image.shape[0] // 4, image.shape[1] // 4), anti_aliasing=True
)
image_downscaled = downscale_local_mean(image, (4, 3))

fig, axes = plt.subplots(nrows=2, ncols=2)

axes = axes.ravel()

axes[0].imshow(image, cmap='gray')
axes[0].set_title('Original Image')

axes[1].imshow(image_rescaled, cmap='gray')
axes[1].set_title('Rescaled Image (aliasing)')

axes[2].imshow(image_resized, cmap='gray')
axes[2].set_title('Resized Image (no aliasing)')

axes[3].imshow(image_downscaled, cmap='gray')
axes[3].set_title('Downscaled Image (no aliasing)')

axes[0].set_xlim(0, 512)
axes[1].set_ylim(512, 0)
plt.tight_layout()
plt.show()
