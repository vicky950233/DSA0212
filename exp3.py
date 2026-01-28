import cv2
import time

# Open webcam (0 = default camera)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Webcam not accessible")
    exit()

print("Press:")
print("  n - Normal speed")
print("  s - Slow motion")
print("  f - Fast motion")
print("  q - Quit")

mode = 'n'  # default mode

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Display mode text
    cv2.putText(frame, f"Mode: {mode.upper()}",
                (20, 40), cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 255, 0), 2)

    cv2.imshow("Webcam Video", frame)

    # Speed control
    if mode == 's':       # slow motion
        time.sleep(0.15)
    elif mode == 'f':     # fast motion
        time.sleep(0.01)
    else:                 # normal
        time.sleep(0.05)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break
    elif key == ord('n'):
        mode = 'n'
    elif key == ord('s'):
        mode = 's'
    elif key == ord('f'):
        mode = 'f'

cap.release()
cv2.destroyAllWindows()
