import RPi.GPIO as GPIO
import time

# Threshold value in milliseconds
threshold = 200  # Adjust this value based on your requirements

def is_light_low(resistorPin, ledPin):
    """
    Determine if the light level is low.
    Returns:
        bool: True if light is low, False otherwise.
    """
    # Charge the capacitor
    GPIO.setup(resistorPin, GPIO.OUT)
    GPIO.output(resistorPin, GPIO.LOW)
    time.sleep(0.1)

    # Discharge the capacitor
    GPIO.setup(resistorPin, GPIO.IN)
    currentTime = time.time()
    diff = 0

    while(GPIO.input(resistorPin) == GPIO.LOW):
        diff = time.time() - currentTime

    # Convert time to milliseconds
    diff_ms = diff * 1000
    print(f"Measured time: {diff_ms:.2f} ms")

    # Check if the measured time exceeds the threshold
    if diff_ms > threshold:
        print('LIGHT ON')
        GPIO.output(ledPin, GPIO.HIGH)  # Turn on LED
    else:
        print('LIGHT OFF')
        GPIO.output(ledPin, GPIO.LOW)  # Turn off LED
