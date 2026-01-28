closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

plt.imshow(closing, cmap='gray'); plt.title("Closing"); plt.axis('off')
