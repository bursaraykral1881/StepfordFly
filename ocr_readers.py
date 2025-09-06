
import pytesseract
import re
from . import config
from .capture import capture_screen_region
from .preprocess import preprocess_image_for_ocr

def _read_text_from_region(region_name, scale_factor=2.0):
    """A helper function to capture, preprocess, and OCR a screen region."""
    region = config.REGIONS.get(region_name)
    if not region:
        print(f"Region '{region_name}' not found in config.")
        return ""

    screenshot = capture_screen_region(region)
    if screenshot is None:
        return ""

    preprocessed_image = preprocess_image_for_ocr(screenshot, scale_factor=scale_factor)
    if preprocessed_image is None:
        return ""

    # Use pytesseract to extract text
    # --psm 7: Treat the image as a single text line.
    custom_config = r'--oem 3 --psm 7'
    try:
        text = pytesseract.image_to_string(preprocessed_image, config=custom_config)
        return text.strip()
    except pytesseract.TesseractNotFoundError:
        print("Tesseract Error: The Tesseract executable was not found.")
        print("Please make sure Tesseract is installed and configured in 'config.py' (TESSERACT_CMD_PATH).")
        return ""
    except Exception as e:
        print(f"An error occurred during OCR: {e}")
        return ""

def get_next_stop_distance():
    """Reads the distance to the next stop and returns it as a float."""
    text = _read_text_from_region("next_stop_distance")
    if text:
        # Use regex to find a floating-point number in the text
        match = re.search(r'(\d+\.\d+)', text)
        if match:
            try:
                return float(match.group(1))
            except ValueError:
                return None
    return None

def get_speed_info():
    """Reads the current and max speed, returning them as a tuple of integers."""
    current_speed_text = _read_text_from_region("current_speed")
    max_speed_text = _read_text_from_region("max_speed")

    current_speed = 0
    max_speed = 0

    if current_speed_text.isdigit():
        current_speed = int(current_speed_text)

    if max_speed_text.isdigit():
        max_speed = int(max_speed_text)

    return current_speed, max_speed

def get_aws_warning_status():
    """Reads the AWS warning status message."""
    return _read_text_from_region("aws_warning")

def get_game_status_message():
    """Reads the general game status message."""
    return _read_text_from_region("status_message")

def get_dialog_message():
    """Reads any dialog box messages."""
    return _read_text_from_region("dialog_message")

if config.TESSERACT_CMD_PATH:
    pytesseract.pytesseract.tesseract_cmd = config.TESSERACT_CMD_PATH
