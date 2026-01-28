blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

plt.imshow(blackhat, cmap='gray'); plt.title("Black Hat"); plt.axis('off')
