import RPi.GPIO as GPIO
import time
from signal import pause


def detect_motion(MOTION_SENSOR_PIN):
    """
    Detects motion using a PIR sensor.

    Returns:
        bool: True if motion is detected, False otherwise.
    """
    try:

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(MOTION_SENSOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        if GPIO.input(MOTION_SENSOR_PIN):  # Motion detected
            print("Motion sensor triggered!")
            return True
        else:
            return False
    except Exception as e:
        print(f"Error detecting motion: {e}")
        return False
