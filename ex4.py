# Install OpenCV
!pip install opencv-python-headless

import cv2
import matplotlib.pyplot as plt
from google.colab import files

# Upload image
uploaded = files.upload()
img_path = list(uploaded.keys())[0]

# Read image
img = cv2.imread(img_path)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Scaling (Resize)
bigger = cv2.resize(img_rgb, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)
smaller = cv2.resize(img_rgb, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

# Display results
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.imshow(img_rgb)
plt.title("Original Image")
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(bigger)
plt.title("Bigger Image (2x)")
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(smaller)
plt.title("Smaller Image (0.5x)")
plt.axis('off')

plt.show()
