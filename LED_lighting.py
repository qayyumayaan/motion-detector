import RPi.GPIO as GPIO

def enable_led(state):
    """
    Enable or disable an LED.
    Args:
        state (bool): True to turn the LED on, False to turn it off.
    """
    led_pin = 17  # Define the GPIO pin for the LED here
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led_pin, GPIO.OUT)

    # Turn the LED on or off based on state
    GPIO.output(led_pin, GPIO.HIGH if state else GPIO.LOW)
    if state:
        print(f"LED on pin {led_pin} is ON.")
    else:
        print(f"LED on pin {led_pin} is OFF.")
