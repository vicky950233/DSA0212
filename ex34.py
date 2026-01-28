from IPython.display import Video, display

uploaded = files.upload()
video_path = list(uploaded.keys())[0]

cap = cv2.VideoCapture(video_path)
frames = []

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frames.append(frame)

cap.release()

h, w = frames[0].shape[:2]
out = cv2.VideoWriter("reverse.mp4",
                      cv2.VideoWriter_fourcc(*'mp4v'),
                      30, (w,h))

for frame in reversed(frames):
    out.write(frame)

out.release()
display(Video("reverse.mp4", embed=True))
