import cv2
import matplotlib.pyplot as plt
from google.colab import files

# Upload video
uploaded = files.upload()
video_path = list(uploaded.keys())[0]

cap = cv2.VideoCapture(video_path)
fgbg = cv2.createBackgroundSubtractorMOG2()

ret, frame = cap.read()
fgmask = fgbg.apply(frame)

# Threshold
_, thresh = cv2.threshold(fgmask, 200, 255, cv2.THRESH_BINARY)

# Find contours
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    if cv2.contourArea(cnt) > 500:
        x,y,w,h = cv2.boundingRect(cnt)
        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)

cap.release()

plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
plt.title("Vehicle Detection")
plt.axis("off")
