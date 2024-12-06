from camera import capture_photo
from motion_sensor import detect_motion
from photoresistor import is_light_low
# from LED_lighting import enable_led
from email_sending import send_email
from datetime import datetime
import time
import os

def main():
    print("Program started. Monitoring light and motion...")

    last_sent_image = None  # Keep track of the last sent image

    try:
        while True:
            # Print the current timestamp
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]  # Include milliseconds
            print(f"Timestamp: {current_time}")

            # Turn on light
            is_light_low()

            # Check motion and trigger camera
            if detect_motion():
                print("Motion detected! Capturing photo...")
                photo_path = capture_photo()
                if photo_path:
                    print(f"Photo saved to: {photo_path}")
                    
                    # Send email function call
                    if photo_path != last_sent_image:  # Avoid resending the same image
                        subject = "Motion Detected!"
                        body = f"Motion was detected at {current_time}."
                        if send_email(subject, body, photo_path):
                            last_sent_image = photo_path  # Update last sent image
                        else:
                            print("Failed to send email.")
                
                else:
                    print("Failed to capture photo.")

            # Wait for a little bit before the next iteration
            time.sleep(10)

    except KeyboardInterrupt:
        print("Exiting program...")

    finally:
        # Ensure the LED is turned off before exiting
        GPIO.cleanup()  # Reset GPIO pins to a safe state
        print("LED turned off. Program terminated.")

if __name__ == "__main__":
    main()
