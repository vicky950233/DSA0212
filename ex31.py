tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

plt.imshow(tophat, cmap='gray'); plt.title("Top Hat"); plt.axis('off')
