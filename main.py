from camera import capture_photo
from motion_sensor import detect_motion
from photoresistor import is_light_low
from LED_lighting import enable_led

def main():
    print("Program started. Monitoring light and motion...")

    try:
        while True:
            # Check the light level
            if is_light_low():
                print("Light level low. Turning on LED.")
                enable_led(True)  # Turn on LED
            else:
                print("Sufficient light. Turning off LED.")
                enable_led(False)  # Turn off LED

            # Check motion and trigger camera
            if detect_motion():
                print("Motion detected! Capturing photo...")
                photo_path = capture_photo()
                if photo_path:
                    print(f"Photo saved to: {photo_path}")
                else:
                    print("Failed to capture photo.")

    except KeyboardInterrupt:
        print("Exiting program...")

    finally:
        # Ensure the LED is turned off before exiting
        enable_led(False)
        print("LED turned off. Program terminated.")

if __name__ == "__main__":
    main()
