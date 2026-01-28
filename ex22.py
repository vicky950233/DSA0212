import cv2
import numpy as np
import matplotlib.pyplot as plt
from google.colab import files

# Upload image
uploaded = files.upload()
img_path = list(uploaded.keys())[0]

img = cv2.imread(img_path)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)

# Gradient mask (Sobel-based)
grad_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
grad_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
grad = cv2.convertScaleAbs(grad_x + grad_y)

# Sharpening using gradient
sharpened_grad = cv2.addWeighted(gray, 1.0, grad, 1.0, 0)

plt.figure(figsize=(10,5))
plt.subplot(1,2,1), plt.imshow(gray, cmap='gray'), plt.title("Original Gray"), plt.axis('off')
plt.subplot(1,2,2), plt.imshow(sharpened_grad, cmap='gray'), plt.title("Gradient Sharpened"), plt.axis('off')
plt.show()
