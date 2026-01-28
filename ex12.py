gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

edges_canny = cv2.Canny(gray, 100, 200)

plt.imshow(edges_canny, cmap='gray')
plt.title("Canny Edge Detection")
plt.axis('off')
plt.show()
