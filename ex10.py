import cv2
import numpy as np
import matplotlib.pyplot as plt

# Source & destination points
src_pts = np.float32([[0,0], [w,0], [w,h], [0,h]])
dst_pts = np.float32([[100,50], [w-50,20], [w-80,h-40], [80,h-60]])

# Homography matrix
H, status = cv2.findHomography(src_pts, dst_pts)

homography_img = cv2.warpPerspective(img, H, (w,h))

plt.subplot(1,2,1), plt.imshow(img), plt.title("Original"), plt.axis('off')
plt.subplot(1,2,2), plt.imshow(homography_img), plt.title("Homography Transform"), plt.axis('off')
plt.show()
