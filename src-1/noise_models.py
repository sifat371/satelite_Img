import numpy as np
import cv2
import os

def add_gaussian_noise(image, sigma):
    """
    image: grayscale image (uint8)
    sigma: standard deviation of Gaussian noise
    """
    noise = np.random.normal(0, sigma, image.shape)
    noisy = image.astype(np.float32) + noise
    noisy = np.clip(noisy, 0, 255)
    return noisy.astype(np.uint8)


def add_salt_pepper_noise(image, prob):
    """
    prob: probability of noise
    """
    noisy = image.copy()
    h, w = image.shape

    num_pixels = int(prob * h * w)

    # Salt (white)
    coords = [np.random.randint(0, i, num_pixels) for i in image.shape]
    noisy[coords[0], coords[1]] = 255

    # Pepper (black)
    coords = [np.random.randint(0, i, num_pixels) for i in image.shape]
    noisy[coords[0], coords[1]] = 0

    return noisy
