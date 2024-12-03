import cv2

def main():
    # Open the camera using OpenCV
    camera = cv2.VideoCapture(0)  # 0 is the index for the first camera

    if not camera.isOpened():
        print("Error: Could not access the camera.")
        return

    print("Press 'q' to quit the video display.")
    try:
        while True:
            # Capture a single frame
            ret, frame = camera.read()

            if not ret:
                print("Error: Failed to capture image.")
                break

            # Display the frame in a window
            cv2.imshow("Raspberry Pi Camera Feed", frame)

            # Break the loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        # Release the camera and close windows
        camera.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
