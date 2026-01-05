import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

from noise_models import add_gaussian_noise, add_salt_pepper_noise

# ===============================
# Paths & Directories
# ===============================
IMAGE_DIR = "../workspace/images"
OUTPUT_NOISE_DIR = "../data/noisy"
OUTPUT_FIG_DIR = "../results"

os.makedirs(OUTPUT_NOISE_DIR, exist_ok=True)
os.makedirs(OUTPUT_FIG_DIR, exist_ok=True)

# ===============================
# Load One Image Safely
# ===============================
images = sorted(os.listdir(IMAGE_DIR))
assert len(images) > 0, "No images found in IMAGE_DIR"

image_name = images[0]   # deterministic choice
image_path = os.path.join(IMAGE_DIR, image_name)

img_bgr = cv2.imread(image_path)
if img_bgr is None:
    raise ValueError("Image could not be loaded")

# OpenCV loads in BGR → convert to RGB
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

# ===============================
# Convert to Grayscale
# f(x, y)
# ===============================
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)

# ===============================
# Add Noise
# ===============================
gaussian_10 = add_gaussian_noise(img_gray, sigma=10)
gaussian_20 = add_gaussian_noise(img_gray, sigma=20)
salt_pepper = add_salt_pepper_noise(img_gray, prob=0.02)

# Ensure valid image format before saving
gaussian_10 = np.clip(gaussian_10, 0, 255).astype(np.uint8)
gaussian_20 = np.clip(gaussian_20, 0, 255).astype(np.uint8)
salt_pepper = np.clip(salt_pepper, 0, 255).astype(np.uint8)

# ===============================
# Visualization: Original vs Grayscale
# ===============================
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
plt.savefig(
    os.path.join(OUTPUT_FIG_DIR, "original_vs_grayscale.png"),
    dpi=300
)
plt.close()

# ===============================
# Visualization: Noise Models
# ===============================
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.imshow(gaussian_10, cmap="gray")
plt.title("Gaussian Noise (σ = 10)")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(gaussian_20, cmap="gray")
plt.title("Gaussian Noise (σ = 20)")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(salt_pepper, cmap="gray")
plt.title("Salt & Pepper Noise (p = 0.02)")
plt.axis("off")

plt.tight_layout()
plt.savefig(
    os.path.join(OUTPUT_FIG_DIR, "noise_visualization.png"),
    dpi=300
)
plt.close()

# ===============================
# Save Noisy Images
# ===============================
cv2.imwrite(
    os.path.join(OUTPUT_NOISE_DIR, "gaussian_sigma_10.png"),
    gaussian_10
)
cv2.imwrite(
    os.path.join(OUTPUT_NOISE_DIR, "gaussian_sigma_20.png"),
    gaussian_20
)
cv2.imwrite(
    os.path.join(OUTPUT_NOISE_DIR, "salt_pepper_p_002.png"),
    salt_pepper
)

print("✅ Step 1 completed successfully.")
print("Saved:")
print("- original_vs_grayscale.png")
print("- noise_visualization.png")
print("- noisy images in ../data/noisy/")
