# Read image
img = cv2.imread(img_path)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Add watermark text
watermarked = img_rgb.copy()
cv2.putText(watermarked, 'cv', (50,50), cv2.FONT_HERSHEY_SIMPLEX,
            2, (255,0,0), 3, cv2.LINE_AA)

plt.figure(figsize=(8,4))
plt.subplot(1,2,1), plt.imshow(img_rgb), plt.title("Original"), plt.axis('off')
plt.subplot(1,2,2), plt.imshow(watermarked), plt.title("Watermarked"), plt.axis('off')
plt.show()
