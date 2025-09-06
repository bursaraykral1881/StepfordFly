import pyautogui

def apply_brakes(strength=1):
    print(f"Applying brakes with strength: {strength}")
    pyautogui.press('down')
    # Depending on game, you might need to press multiple times or hold:
    # if strength > 0.5: pyautogui.press('down', presses=2, interval=0.1)
    pass

def increase_throttle(strength=1):
    print(f"Increasing throttle with strength: {strength}")
    pyautogui.press('up')
    # if strength > 0.5: pyautogui.press('up', presses=2, interval=0.1)
    pass

def close_doors_action():
    print("Closing doors.")
    pyautogui.press('t') # Assuming 't' key for closing doors
    pass

def open_doors_action():
    print("Opening doors.")
    pyautogui.press('t') # Assuming 't' key for opening doors
    pass

def release_emergency_brake():
    print("Releasing emergency brake.")
    pyautogui.press('q') # Assuming 'q' key for releasing emergency brake
    pass

def move_forward_slightly():
    print("Moving forward slightly to platform.")
    pyautogui.press('up', presses=1, interval=0.1) # Short throttle burst
    pass
