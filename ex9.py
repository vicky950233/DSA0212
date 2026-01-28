!pip install opencv-python-headless

import cv2
import numpy as np
from google.colab import files
from IPython.display import Video, display

uploaded = files.upload()
video_path = list(uploaded.keys())[0]

cap = cv2.VideoCapture(video_path)

fps = cap.get(cv2.CAP_PROP_FPS)
w = int(cap.get(3))
h = int(cap.get(4))

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter("perspective_video.mp4", fourcc, fps, (w,h))

pts1 = np.float32([[0,0], [w,0], [0,h], [w,h]])
pts2 = np.float32([[50,50], [w-50,30], [80,h-60], [w-80,h-40]])

M = cv2.getPerspectiveTransform(pts1, pts2)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.warpPerspective(frame, M, (w,h))
    out.write(frame)

cap.release()
out.release()

display(Video("perspective_video.mp4", embed=True))
