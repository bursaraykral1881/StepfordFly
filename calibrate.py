import pyautogui
import time

print("Starting calibration tool...")
print("Move your mouse to the top-left corner of a region and note the coordinates.")
print("Then, move it to the bottom-right corner and note those coordinates.")
print("Press Ctrl+C to stop.")

try:
    while True:
        x, y = pyautogui.position()
        position_str = f"X: {x:4d}, Y: {y:4d}"
        print(position_str, end='\r')
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nCalibration tool stopped.")

