# Install OpenCV
!pip install opencv-python-headless

import cv2
import numpy as np
import matplotlib.pyplot as plt
from google.colab import files

# Upload image
uploaded = files.upload()
img_path = list(uploaded.keys())[0]

# Read image
img = cv2.imread(img_path)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Laplacian kernel including diagonal neighbors
laplacian_diag_kernel = np.array([[1, 1, 1],
                                  [1, 8, 1],
                                  [1, 1, 1]], dtype=np.float32)

# Apply filter using cv2.filter2D
sharpened_diag_img = cv2.filter2D(img_rgb, -1, laplacian_diag_kernel)

# Display results
plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.imshow(img_rgb)
plt.title("Original Image")
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(sharpened_diag_img)
plt.title("Sharpened (Diagonal Laplacian)")
plt.axis('off')

plt.show()
