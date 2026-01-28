# Structuring element
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
eroded = cv2.erode(gray, kernel, iterations=1)

plt.figure(figsize=(8,4))
plt.subplot(1,2,1), plt.imshow(gray, cmap='gray'), plt.title("Original"), plt.axis('off')
plt.subplot(1,2,2), plt.imshow(eroded, cmap='gray'), plt.title("Eroded"), plt.axis('off')
plt.show()
