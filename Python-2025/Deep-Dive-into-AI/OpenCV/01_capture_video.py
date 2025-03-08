import os
import cv2
import numpy as np
from typing import Optional

def get_video_path() -> str:
    curr_dir = os.path.abspath("OpenCV")
    vid_path = os.path.join(curr_dir, "assets/video/video1.mp4")
    return vid_path

try:
    # Get video path
    vid_path = get_video_path()

    # Check if video is available
    if not os.path.exists(vid_path):
        raise FileNotFoundError(f"Unable to find video path: {vid_path}")

    cap = cv2.VideoCapture(vid_path)

    # Check if video opened successfully
    if not cap.isOpened():
        raise IOError("Error opening video stream")
    
    while True:
        ret, frame = cap.read()
        cv2.imshow("Video", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Handle exceptions
except FileNotFoundError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
finally:
    # Clean up resources
    if 'cap' in locals():
        cap.release()
    cv2.destroyAllWindows()