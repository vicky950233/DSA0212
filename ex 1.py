# Install OpenCV
!pip install opencv-python-headless

# Import libraries
import cv2
import matplotlib.pyplot as plt
from google.colab import files

# Upload image
uploaded = files.upload()
image_path = list(uploaded.keys())[0]

# Read image
img = cv2.imread(image_path)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# a) Grayscale conversion
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# b) Gaussian Blur
blur = cv2.GaussianBlur(img, (7, 7), 0)

# c) Canny Edge Detection
edges = cv2.Canny(gray, 100, 200)

# Structuring element
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

# d) Dilation
dilated = cv2.dilate(edges, kernel, iterations=1)

# e) Erosion
eroded = cv2.erode(edges, kernel, iterations=1)

# Display results
titles = ['Original Image', 'Grayscale', 'Gaussian Blur',
          'Canny Edge', 'Dilated Image', 'Eroded Image']
images = [img_rgb, gray, blur, edges, dilated, eroded]

plt.figure(figsize=(12, 8))
for i in range(6):
    plt.subplot(2, 3, i+1)
    if len(images[i].shape) == 2:
        plt.imshow(images[i], cmap='gray')
    else:
        plt.imshow(images[i])
    plt.title(titles[i])
    plt.axis('off')

plt.tight_layout()
plt.show()
