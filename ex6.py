# Install OpenCV
!pip install opencv-python-headless

import cv2
import matplotlib.pyplot as plt
from google.colab import files
import numpy as np

# Upload image
uploaded = files.upload()
img_path = list(uploaded.keys())[0]

# Read image
img = cv2.imread(img_path)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Get image size
rows, cols = img_rgb.shape[:2]

# Translation values
tx = 100   # move right (x-direction)
ty = 50    # move down (y-direction)

# Translation matrix
M = np.float32([[1, 0, tx],
                [0, 1, ty]])

# Apply translation
moved_img = cv2.warpAffine(img_rgb, M, (cols, rows))

# Display results
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.imshow(img_rgb)
plt.title("Original Image")
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(moved_img)
plt.title("Moved Image (Translated)")
plt.axis('off')

plt.show()
