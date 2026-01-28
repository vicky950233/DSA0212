# Install OpenCV
!pip install opencv-python-headless

import cv2
from google.colab import files
from IPython.display import Video, display

# Upload captured video
uploaded = files.upload()
video_path = list(uploaded.keys())[0]

# Read video
cap = cv2.VideoCapture(video_path)

fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Video writers
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

normal_out = cv2.VideoWriter('normal.mp4', fourcc, fps, (width, height))
slow_out = cv2.VideoWriter('slow.mp4', fourcc, fps/2, (width, height))
fast_out = cv2.VideoWriter('fast.mp4', fourcc, fps*2, (width, height))

# Process frames
while True:
    ret, frame = cap.read()
    if not ret:
        break
    normal_out.write(frame)
    slow_out.write(frame)
    fast_out.write(frame)

cap.release()
normal_out.release()
slow_out.release()
fast_out.release()

# Display videos
print("▶ Normal Speed Video")
display(Video("normal.mp4", embed=True))

print("▶ Slow Motion Video")
display(Video("slow.mp4", embed=True))

print("▶ Fast Motion Video")
display(Video("fast.mp4", embed=True))
