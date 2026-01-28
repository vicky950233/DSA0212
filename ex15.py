sobel_xy = cv2.Sobel(gray, cv2.CV_64F, 1, 1, ksize=3)
sobel_xy = cv2.convertScaleAbs(sobel_xy)

plt.imshow(sobel_xy, cmap='gray')
plt.title("Sobel Edge Detection - XY Axis")
plt.axis('off')
plt.show()
