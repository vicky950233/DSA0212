import cv2
import numpy as np
import matplotlib.pyplot as plt

h, w = img.shape[:2]

pts1 = np.float32([[0,0], [w-1,0], [0,h-1], [w-1,h-1]])
pts2 = np.float32([[50,50], [w-100,20], [80,h-50], [w-50,h-80]])

# Perspective matrix
M = cv2.getPerspectiveTransform(pts1, pts2)

perspective_img = cv2.warpPerspective(img, M, (w, h))

plt.subplot(1,2,1), plt.imshow(img), plt.title("Original"), plt.axis('off')
plt.subplot(1,2,2), plt.imshow(perspective_img), plt.title("Perspective Transform"), plt.axis('off')
plt.show()
