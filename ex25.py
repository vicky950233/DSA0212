# Boundary detection kernel
kernel = np.array([[-1,-1,-1],
                   [-1,8,-1],
                   [-1,-1,-1]], dtype=np.float32)

boundary = cv2.filter2D(gray, -1, kernel)

plt.imshow(boundary, cmap='gray')
plt.title("Image Boundary"), plt.axis('off')
plt.show()
