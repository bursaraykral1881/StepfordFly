# IMPORTANT: Update this path if Tesseract is not found automatically
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
TESSERACT_CMD_PATH = None # Set this to your tesseract.exe path if needed, e.g., r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Define screen regions for OCR and color detection
# Coordinates are (left, top, right, bottom)
# You will need to determine these exact coordinates for your game window.
REGIONS = {
    "next_stop_distance": (248, 996, 327, 1023),
    "light_indicator": (365, 847, 433, 994),
    "current_speed": (1434, 912, 1501, 948),
    "max_speed": (1447, 996, 1490, 1025),
    "aws_warning": (1678, 910, 1881, 962),
    "status_message": (1359, 628, 1908, 682),
    "dialog_message": (22, 730, 318, 814)
}

# HSV color ranges for light detection (example values, adjust for your game)
# Hue (0-179), Saturation (0-255), Value (0-255)
COLOR_RANGES = {
    "red": ([0, 100, 100], [5, 255, 255]),      # Lower Red: Hue 0-5, broader S/V
    "green": ([60, 40, 40], [68, 255, 255]),    # Green: Hue around 63, adjusted S/V range
    "yellow": ([25, 60, 100], [35, 255, 255]),   # Yellow: Hue around 28, adjusted S/V range
    "orange": ([20, 70, 100], [25, 255, 255]),   # Orange: Hue around 23, adjusted S/V range
    # Note: Red also exists at the higher end of the hue spectrum
    "red_alt": ([170, 100, 100], [179, 255, 255])
}

# Threshold to differentiate single yellow from double yellow (percentage of pixels)
# You will need to calibrate this value based on your game's visual representation.
DOUBLE_YELLOW_THRESHOLD = 15 # Example: If more than 15% of the light indicator region is yellow, consider it double yellow
