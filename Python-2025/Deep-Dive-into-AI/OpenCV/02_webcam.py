import cv2
from typing import Optional

class WebcamError(Exception):
    """Custom exception for webcam Errors"""
    pass

def init_camera(camera_index: int = 0) -> Optional[cv2.VideoCapture]:
    """Initialize webcam"""
    cap = cv2.VideoCapture(camera_index)
    if not cap.isOpened():
        raise WebcamError(f"Cannot access webcam at index {camera_index}")

    # Set resolution
    cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
    return cap

def main() -> None:
    cap = None
    try:
        cap = init_camera()
        
        while True:
            ret, frame = cap.read()

            if not ret:
                raise WebcamError("Failed to grab frame")

            cv2.imshow("Webcam", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    except WebcamError as e:
        print(f"Webcam Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")
    finally:
        if cap is not None:
            cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()