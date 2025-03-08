import os
import cv2
import numpy as np
from typing import Optional

def read_image(image_path: str) -> Optional[np.ndarray]:
    img = cv2.imread(image_path)
    return img

def display_image(title: str, image: np.ndarray) -> None:
    cv2.imshow(title, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main() -> None:

    # Get file path
    current_dir = os.path.abspath("OpenCV") # absolute path
    image_path = os.path.join(current_dir, "assets/image/img1.jpeg")

    try:
        # Read image
        img = read_image(image_path)
        print(img)
        if img is None:
            raise FileNotFoundError(f"Unable to load image: {image_path}")
        
        display_image("Output", img)

    except FileNotFoundError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()