import cv2
import os
from datetime import datetime

def capture_photo(save_directory="photos"):
    """
    Captures a single photo using the Raspberry Pi camera and saves it to a file.
    Args:
        save_directory (str): Directory where the photo will be saved.
    Returns:
        str: Path to the saved photo, or None if an error occurs.
    """
    # Ensure the save directory exists
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    # Generate a timestamped filename
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    photo_path = os.path.join(save_directory, f"photo_{timestamp}.jpg")

    # Open the camera
    camera = cv2.VideoCapture(0)  # 0 is the index for the first camera

    if not camera.isOpened():
        print("Error: Could not access the camera.")
        return None

    try:
        # Capture a single frame
        ret, frame = camera.read()

        if not ret:
            print("Error: Failed to capture image.")
            return None

        # Save the captured frame as an image file
        cv2.imwrite(photo_path, frame)
        print(f"Photo captured and saved to {photo_path}")
        return photo_path

    except Exception as e:
        print(f"Error during photo capture: {e}")
        return None

    finally:
        # Release the camera
        camera.release()
