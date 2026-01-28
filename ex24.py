# Crop region from original image
crop = img_rgb[50:200, 50:200]  # y1:y2, x1:x2

# Create a blank image to paste crop
canvas = img_rgb.copy()
canvas[0:150, 0:150] = crop  # Paste at top-left

plt.figure(figsize=(10,5))
plt.subplot(1,2,1), plt.imshow(crop), plt.title("Cropped Region"), plt.axis('off')
plt.subplot(1,2,2), plt.imshow(canvas), plt.title("Pasted Image"), plt.axis('off')
plt.show()
