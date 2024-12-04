from camera import capture_photo
from motion_sensor import detect_motion
from photoresistor import is_light_low
from LED_lighting import enable_led
from email import send_email
from datetime import datetime
import time
import os

def main():
    print("Program started. Monitoring light and motion...")

    last_sent_image = None  # Keep track of the last sent image
    RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL")

    try:
        while True:
            # Print the current timestamp
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]  # Include milliseconds
            print(f"Timestamp: {current_time}")

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
                    if photo_path != last_sent_image:  # Avoid resending the same image
                        subject = "Motion Detected!"
                        body = f"Motion was detected at {current_time}."
                        if send_email(subject, body, photo_path, RECIPIENT_EMAIL):
                            last_sent_image = photo_path  # Update last sent image
                        else:
                            print("Failed to send email.")
                else:
                    print("Failed to capture photo.")

            # Wait for 100 ms before the next iteration
            time.sleep(0.1)

    except KeyboardInterrupt:
        print("Exiting program...")

    finally:
        # Ensure the LED is turned off before exiting
        enable_led(False)
        print("LED turned off. Program terminated.")

if __name__ == "__main__":
    main()
