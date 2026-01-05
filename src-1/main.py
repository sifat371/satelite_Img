import cv2
import matplotlib.pyplot as plt
import os

# ---------- Load one image ----------
IMAGE_DIR = "../workspace/images"
image_name = os.listdir(IMAGE_DIR)[60]  # take first image
image_path = os.path.join(IMAGE_DIR, image_name)

img_bgr = cv2.imread(image_path)
if img_bgr is None:
    raise ValueError("Image could not be loaded")

# OpenCV loads images in BGR format
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

# ---------- Convert to Grayscale ----------
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)

# ---------- Display ----------
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.imshow(img_rgb)
plt.title("Original RGB Satellite Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(img_gray, cmap="gray")
plt.title("Grayscale Image f(x, y)")
plt.axis("off")

plt.tight_layout()
plt.savefig("satellite_image_comparison.png", dpi=300)
