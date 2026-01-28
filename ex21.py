# High-boost sharpening
k = 1.8  # High-boost factor >1

high_boost_img = cv2.addWeighted(img_rgb, k, blurred, -(k-1), 0)

# Display
plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.imshow(img_rgb)
plt.title("Original Image")
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(high_boost_img)
plt.title("High-Boost Sharpened Image")
plt.axis('off')

plt.show()
