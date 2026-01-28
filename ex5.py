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

# Get image center
(h, w) = img_rgb.shape[:2]
center = (w // 2, h // 2)

# Rotation angles
angle_cw = -45    # Clockwise rotation
angle_ccw = 45    # Counter-clockwise rotation

# Rotation matrix
M_cw = cv2.getRotationMatrix2D(center, angle_cw, 1.0)
M_ccw = cv2.getRotationMatrix2D(center, angle_ccw, 1.0)

# Apply rotation
rotated_cw = cv2.warpAffine(img_rgb, M_cw, (w, h))
rotated_ccw = cv2.warpAffine(img_rgb, M_ccw, (w, h))

# Display results
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.imshow(img_rgb)
plt.title("Original Image")
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(rotated_cw)
plt.title("Clockwise Rotation (45°)")
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(rotated_ccw)
plt.title("Counter-Clockwise Rotation (45°)")
plt.axis('off')

plt.show()
