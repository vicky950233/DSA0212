sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobel_x = cv2.convertScaleAbs(sobel_x)

plt.imshow(sobel_x, cmap='gray')
plt.title("Sobel Edge Detection - X Axis")
plt.axis('off')
plt.show()
