import cv2, numpy as np, matplotlib.pyplot as plt
from google.colab import files

uploaded = files.upload()
img = cv2.imread(list(uploaded.keys())[0], 0)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

plt.imshow(opening, cmap='gray'); plt.title("Opening"); plt.axis('off')
