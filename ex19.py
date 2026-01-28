# Install OpenCV if not installed
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

# Laplacian mask with positive center coefficient
laplacian_pos_kernel = np.array([[0, -1, 0],
                                 [-1, 5, -1],
                                 [0, -1, 0]], dtype=np.float32)

# Apply sharpening
sharpened_pos_img = cv2.filter2D(img_rgb, -1, laplacian_pos_kernel)

# Display results
plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.imshow(img_rgb)
plt.title("Original Image")
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(sharpened_pos_img)
plt.title("Sharpened (Positive Center Laplacian)")
plt.axis('off')

plt.show()
