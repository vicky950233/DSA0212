import cv2
import numpy as np
import matplotlib.pyplot as plt
from google.colab import files

# Upload image
uploaded = files.upload()
img_path = list(uploaded.keys())[0]

img = cv2.imread(img_path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
h, w = img.shape[:2]

# Define source points (4 corners)
src_pts = np.array([[0,0],[w-1,0],[w-1,h-1],[0,h-1]], dtype=float)

# Define destination points (warped quadrilateral)
dst_pts = np.array([[50,50],[w-50,30],[w-30,h-50],[30,h-30]], dtype=float)

# Compute Homography using DLT
H, status = cv2.findHomography(src_pts, dst_pts, method=0)  # method=0 → DLT

dlt_img = cv2.warpPerspective(img, H, (w,h))

plt.subplot(1,2,1), plt.imshow(img), plt.title("Original"), plt.axis('off')
plt.subplot(1,2,2), plt.imshow(dlt_img), plt.title("DLT Transformation"), plt.axis('off')
plt.show()
