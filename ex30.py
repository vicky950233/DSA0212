gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

plt.imshow(gradient, cmap='gray'); plt.title("Morphological Gradient"); plt.axis('off')
