from PIL import ImageGrab, Image

def capture_screen_region(region):
    """
    Captures a specific region of the screen.
    :param region: A tuple (left, top, right, bottom) defining the screen area.
    :return: A PIL Image object of the captured region.
    """
    try:
        screenshot = ImageGrab.grab(bbox=region)
        return screenshot
    except Exception as e:
        print(f"Error capturing screen region {region}: {e}")
        return None
