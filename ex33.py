img_color = cv2.imread(list(uploaded.keys())[0])
gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

# Using circle detection (common for watch dials)
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 100)

if circles is not None:
    circles = np.uint16(np.around(circles))
    for x,y,r in circles[0]:
        cv2.circle(img_color, (x,y), r, (0,255,0), 3)

plt.imshow(cv2.cvtColor(img_color, cv2.COLOR_BGR2RGB))
plt.title("Watch Detection"); plt.axis('off')
