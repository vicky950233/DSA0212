dilated = cv2.dilate(gray, kernel, iterations=1)

plt.figure(figsize=(8,4))
plt.subplot(1,2,1), plt.imshow(gray, cmap='gray'), plt.title("Original"), plt.axis('off')
plt.subplot(1,2,2), plt.imshow(dilated, cmap='gray'), plt.title("Dilated"), plt.axis('off')
plt.show()
