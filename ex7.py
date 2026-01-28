!pip install opencv-python-headless

import cv2
import numpy as np
import matplotlib.pyplot as plt
from google.colab import files

uploaded = files.upload()
img_path = list(uploaded.keys())[0]

img = cv2.imread(img_path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

rows, cols = img.shape[:2]

# Source and destination points
pts1 = np.float32([[50,50], [200,50], [50,200]])
pts2 = np.float32([[10,100], [200,50], [100,250]])

# Affine matrix
M = cv2.getAffineTransform(pts1, pts2)

affine_img = cv2.warpAffine(img, M, (cols, rows))

plt.subplot(1,2,1), plt.imshow(img), plt.title("Original"), plt.axis('off')
plt.subplot(1,2,2), plt.imshow(affine_img), plt.title("Affine Transformed"), plt.axis('off')
plt.show()
