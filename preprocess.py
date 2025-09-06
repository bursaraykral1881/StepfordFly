import cv2
import numpy as np
from PIL import Image # Only imported for type hinting in comments

def preprocess_image_for_ocr(image_pil, scale_factor=2.0):
    """
    Pre-processes a PIL image for Tesseract OCR.
    Converts to grayscale, applies thresholding, and scales up for better recognition.
    :param image_pil: PIL Image object.
    :param scale_factor: Factor to scale up the image (e.g., 2.0 for double size).
    :return: OpenCV image (numpy array) ready for OCR.
    """
    if image_pil is None:
        return None

    # Convert PIL Image to OpenCV format (numpy array)
    img_cv = np.array(image_pil.convert('RGB'))
    img_cv = cv2.cvtColor(img_cv, cv2.COLOR_RGB2BGR)

    # Scale up the image (e.g., for small text)
    if scale_factor > 1.0:
        img_cv = cv2.resize(img_cv, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_CUBIC)

    # Convert to grayscale
    gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)

    # Apply adaptive thresholding (good for varying light conditions)
    # Adjust blockSize and C for optimal results
    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY, 11, 2)

    # Optional: Noise reduction (e.g., Gaussian blur)
    # blur = cv2.GaussianBlur(thresh, (3, 3), 0) # Small blur might help with some fonts

    return thresh

def preprocess_image_for_color_detection(image_pil):
    """
    Pre-processes a PIL image for color detection.
    :param image_pil: PIL Image object.
    :return: OpenCV image (numpy array) in HSV format.
    """
    if image_pil is None:
        return None
    img_cv = np.array(image_pil.convert('RGB'))
    img_cv = cv2.cvtColor(img_cv, cv2.COLOR_RGB2BGR)
    hsv = cv2.cvtColor(img_cv, cv2.COLOR_BGR2HSV)
    return hsv
