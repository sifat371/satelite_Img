import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

from noise_models import add_gaussian_noise, add_salt_pepper_noise

from filters import mean_filter, median_filter, gaussian_filter


IMAGE_DIR = "../workspace/images"

OUTPUT_NOISE_DIR = "../data/noisy"
OUTPUT_DENOISED_DIR = "../data/denoised"
OUTPUT_FIG_DIR = "../results"

os.makedirs(OUTPUT_NOISE_DIR, exist_ok=True)
os.makedirs(OUTPUT_DENOISED_DIR, exist_ok=True)
os.makedirs(OUTPUT_FIG_DIR, exist_ok=True)


image_files = sorted(os.listdir(IMAGE_DIR))
assert len(image_files) > 0, "❌ No images found in IMAGE_DIR"

print(f"📂 Found {len(image_files)} satellite images.")



for idx, image_name in enumerate(image_files):

    print(f"\n🔄 Processing [{idx+1}/{len(image_files)}]: {image_name}")

    image_path = os.path.join(IMAGE_DIR, image_name)

    
    img_bgr = cv2.imread(image_path)
    if img_bgr is None:
        print("⚠️ Skipping image (could not load)")
        continue

    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)


    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)


    gaussian_10 = add_gaussian_noise(img_gray, sigma=10)
    gaussian_20 = add_gaussian_noise(img_gray, sigma=20)
    salt_pepper = add_salt_pepper_noise(img_gray, prob=0.02)


    gaussian_10 = np.clip(gaussian_10, 0, 255).astype(np.uint8)
    gaussian_20 = np.clip(gaussian_20, 0, 255).astype(np.uint8)
    salt_pepper = np.clip(salt_pepper, 0, 255).astype(np.uint8)


# plt.figure(figsize=(10, 4))

# plt.subplot(1, 2, 1)
# plt.imshow(img_rgb)
# plt.title("Original RGB Satellite Image")
# plt.axis("off")

# plt.subplot(1, 2, 2)
# plt.imshow(img_gray, cmap="gray")
# plt.title("Grayscale Image f(x, y)")
# plt.axis("off")

# plt.tight_layout()
# plt.savefig(
#     os.path.join(OUTPUT_FIG_DIR, "original_vs_grayscale.png"),
#     dpi=300
# )
# plt.close()


# plt.figure(figsize=(12, 4))

# plt.subplot(1, 3, 1)
# plt.imshow(gaussian_10, cmap="gray")
# plt.title("Gaussian Noise (σ = 10)")
# plt.axis("off")

# plt.subplot(1, 3, 2)
# plt.imshow(gaussian_20, cmap="gray")
# plt.title("Gaussian Noise (σ = 20)")
# plt.axis("off")

# plt.subplot(1, 3, 3)
# plt.imshow(salt_pepper, cmap="gray")
# plt.title("Salt & Pepper Noise (p = 0.02)")
# plt.axis("off")

# plt.tight_layout()
# plt.savefig(
#     os.path.join(OUTPUT_FIG_DIR, "noise_visualization.png"),
#     dpi=300
# )
# plt.close()


    # Save noisy images
base_name = os.path.splitext(image_name)[0]

cv2.imwrite(os.path.join(OUTPUT_NOISE_DIR, f"{base_name}_gaussian_10.png"), gaussian_10)
cv2.imwrite(os.path.join(OUTPUT_NOISE_DIR, f"{base_name}_gaussian_20.png"), gaussian_20)
cv2.imwrite(os.path.join(OUTPUT_NOISE_DIR, f"{base_name}_salt_pepper.png"), salt_pepper)

#Apply Filters
mean_3 = mean_filter(gaussian_10, 3)
mean_5 = mean_filter(gaussian_10, 5)

median_3 = median_filter(salt_pepper, 3)
median_5 = median_filter(salt_pepper, 5)

gauss_3 = gaussian_filter(gaussian_10, 3, sigma=1)
gauss_5 = gaussian_filter(gaussian_10, 5, sigma=1.5)


    # Save denoised outputs
cv2.imwrite(os.path.join(OUTPUT_DENOISED_DIR, f"{base_name}_mean_3.png"), mean_3)
cv2.imwrite(os.path.join(OUTPUT_DENOISED_DIR, f"{base_name}_mean_5.png"), mean_5)

cv2.imwrite(os.path.join(OUTPUT_DENOISED_DIR, f"{base_name}_median_3.png"), median_3)
cv2.imwrite(os.path.join(OUTPUT_DENOISED_DIR, f"{base_name}_median_5.png"), median_5)

cv2.imwrite(os.path.join(OUTPUT_DENOISED_DIR, f"{base_name}_gaussian_3.png"), gauss_3)
cv2.imwrite(os.path.join(OUTPUT_DENOISED_DIR, f"{base_name}_gaussian_5.png"), gauss_5)


print("\n✅ Step 3 completed successfully.")
print("Saved:")
print("- Noisy images → ../data/noisy/")
print("- Denoised images → ../data/denoised/")
print("- Visual comparisons → ../results/")
print("Applied filters:")
print("- Mean (3×3, 5×5)")
print("- Median (3×3, 5×5)")
print("- Gaussian (3×3, 5×5)")


