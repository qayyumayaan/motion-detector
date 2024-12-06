import RPi.GPIO as GPIO
import time

def detect_motion(MOTION_SENSOR_PIN):
    """
    Detects motion using a PIR sensor.

    Returns:
        bool: True if motion is detected, False otherwise.
    """
    try:
        if GPIO.input(MOTION_SENSOR_PIN):  # Motion detected
            print("Motion sensor triggered!")
            return True
        else:
            return False
    except Exception as e:
        print(f"Error detecting motion: {e}")
        return False
