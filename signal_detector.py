# signal_detector.py
import cv2
import numpy as np
from . import config # Corrected: Relative import for config
from .capture import capture_screen_region # Corrected: Relative import for capture
from .preprocess import preprocess_image_for_color_detection # Corrected: Relative import for preprocess

def detect_light_color():
    """
    Detects the color of the light indicator, distinguishing single and double yellow.
    """
    img_pil = capture_screen_region(config.REGIONS["light_indicator"])
    hsv_image = preprocess_image_for_color_detection(img_pil)
    if hsv_image is None:
        return "Unknown"

    # To properly detect "double yellow", ensure REGIONS["light_indicator"] covers
    # the area where both yellow lights would appear.
    # We'll use a threshold on the percentage of yellow pixels to infer "double yellow".

    for color_name, (lower, upper) in config.COLOR_RANGES.items():
        lower_bound = np.array(lower, dtype=np.uint8)
        upper_bound = np.array(upper, dtype=np.uint8)

        mask = cv2.inRange(hsv_image, lower_bound, upper_bound)
        pixel_count = cv2.countNonZero(mask)
        total_pixels = hsv_image.shape[0] * hsv_image.shape[1]
        color_percentage = (pixel_count / total_pixels) * 100

        # If a significant portion of the region matches a color, return it
        if color_percentage > 5:  # Base threshold for any color detection
            if color_name == "yellow":
                # Check for double yellow if a high percentage of yellow is detected
                if color_percentage > config.DOUBLE_YELLOW_THRESHOLD:
                    return "Double Yellow"
                else:
                    return "Yellow"
            elif color_name in ["red", "red_alt"]: # Combine red and red_alt detection
                return "Red"
            else:
                return color_name
    return "Unknown"
