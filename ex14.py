sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
sobel_y = cv2.convertScaleAbs(sobel_y)

plt.imshow(sobel_y, cmap='gray')
plt.title("Sobel Edge Detection - Y Axis")
plt.axis('off')
plt.show()
