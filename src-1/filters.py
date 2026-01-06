import cv2

def mean_filter(image, ksize):
    return cv2.blur(image, (ksize, ksize))


def median_filter(image, ksize):
    return cv2.medianBlur(image, ksize)


def gaussian_filter(image, ksize, sigma):
    return cv2.GaussianBlur(image, (ksize, ksize), sigma)
