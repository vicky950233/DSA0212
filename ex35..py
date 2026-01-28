import cv2
import matplotlib.pyplot as plt
from google.colab import files

# Upload image
uploaded = files.upload()
img_path = list(uploaded.keys())[0]

img = cv2.imread(img_path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Binary threshold
_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

# Find contours (Colab compatible)
contours, hierarchy = cv2.findContours(
    thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)

# Draw rectangles and extract objects
for cnt in contours:
    if cv2.contourArea(cnt) > 500:
        x,y,w,h = cv2.boundingRect(cnt)
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        roi = img[y:y+h, x:x+w]  # extracted object

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Object Extraction")
plt.axis("off")
