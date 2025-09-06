# main.py
import time
from .ocr_readers import get_next_stop_distance, get_speed_info, get_aws_warning_status, get_game_status_message, get_dialog_message
from .signal_detector import detect_light_color
from .game_controls import apply_brakes, increase_throttle, close_doors_action, open_doors_action, release_emergency_brake, move_forward_slightly

def autopilot_train():
    print("Starting train autopilot...")
    while True:
        # 1. Read Next Stop Distance
        distance_to_next_stop = get_next_stop_distance()
        if distance_to_next_stop is not None:
            print(f"Next Stop Distance: {distance_to_next_stop:.2f} miles")
            # Example logic: if approaching station, apply brakes
            if distance_to_next_stop < 0.5: # within half a mile
                apply_brakes(strength=0.7)
            elif distance_to_next_stop < 0.1: # very close
                apply_brakes(strength=1.0)
            else:
                increase_throttle(strength=0.5) # Maintain speed if far

        # 2. Detect Light Color
        light_color = detect_light_color()
        print(f"Light Color: {light_color}")
        # Example logic based on light color
        if light_color == "Red":
            apply_brakes(strength=1.0)
        elif light_color == "Yellow":
            apply_brakes(strength=0.5)
        elif light_color == "Double Yellow": # Specific logic for double yellow
            apply_brakes(strength=0.3) # Less urgent brake than single yellow
        elif light_color == "Green":
            increase_throttle(strength=0.8)

        # 3. Read Speed with Max Speed
        current_speed, max_speed = get_speed_info()
        print(f"Speed: {current_speed} / {max_speed}")
        # Example logic: Adjust speed to stay within limits
        if current_speed > max_speed * 0.95: # 95% of max speed
            apply_brakes(strength=0.3)
        elif current_speed < max_speed * 0.8:
            increase_throttle(strength=0.4)

        # 4. AWS Warning
        aws_status = get_aws_warning_status()
        print(f"AWS Status: {aws_status}")
        if aws_status == "Emergency Brake Active":
            print("EMERGENCY BRAKE ENGAGED! Attempting to release if safe.")
            release_emergency_brake() # Only if your game has a way to release it
        elif aws_status == "AWS Active/Warning":
            print("AWS Warning detected! Applying slight brakes.")
            apply_brakes(strength=0.2) # Gentle brake response to warning

        # 5. Game Status
        game_status = get_game_status_message()
        print(f"Game Status: {game_status}")
        if game_status == "Stop to load":
            print("Detected 'Stop to Load'. Applying full brakes.")
            apply_brakes(strength=1.0)
            # You might need to add logic here to wait until speed is 0
            # then open doors, wait for 'close doors' then close doors
            # (e.g., using time.sleep() or checking speed repeatedly)
        elif game_status == "Close Doors":
            print("Detected 'Close Doors'. Closing doors.")
            close_doors_action()
        elif game_status == "Depart":
            print("Detected 'Depart'. Increasing throttle.")
            increase_throttle(strength=1.0) # Full throttle to depart

        # 6. Dialog Messages
        dialog_message = get_dialog_message()
        print(f"Dialog Message: {dialog_message}")
        if dialog_message == "Stop Finished":
            print("Detected 'Stop Finished'. Opening doors.")
            open_doors_action() # Or whatever action is needed after stopping
        elif dialog_message == "Move Forward to Platform":
            print("Detected 'Move Forward to Platform'. Moving slightly.")
            move_forward_slightly()
        elif dialog_message == "Train Must Be Stopped To Load":
            print("Detected 'Train Must Be Stopped To Load'. Applying full brakes.")
            apply_brakes(strength=1.0) # Ensure train is fully stopped

        print("-" * 30)
        time.sleep(1) # Adjust the refresh rate as needed (e.g., 0.5 for faster updates)

if __name__ == "__main__":
    print("Train Autopilot Modules Initialized.")
    print("Remember to adjust REGIONS and COLOR_RANGES in config.py for your specific game.")
    print("Also, implement game control actions in game_controls.py if not using direct pyautogui.")
    print("\n--- Important: How to run this script ---")
    print("To avoid 'ImportError', navigate to the PARENT directory of 'StepfordFly'")
    print("(e.g., 'PycharmProjects') and run it as a module:")
    print("python3 -m StepfordFly.main")
    # The original call: autopilot_train() is commented out in this main.py
    # to prevent it from running directly when this file is imported as a module for demonstration.
    # When you run it using 'python3 -m', the 'if __name__ == "__main__"' block will execute.
    # Uncomment the line below to actually start the autopilot loop when run as a module.
    autopilot_train()
