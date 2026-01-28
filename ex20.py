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

# Gaussian blur
blurred = cv2.GaussianBlur(img_rgb, (7,7), 0)

# Unsharp masking
alpha = 1.5
unsharp_img = cv2.addWeighted(img_rgb, 1 + alpha, blurred, -alpha, 0)

# Display
plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.imshow(img_rgb)
plt.title("Original Image")
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(unsharp_img)
plt.title("Sharpened (Unsharp Mask)")
plt.axis('off')

plt.show()
