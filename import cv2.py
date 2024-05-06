import cv2
import numpy as np

def detect_box(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        contour = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(contour)
        return [(x, y), (x + w, y), (x + w, y + h), (x, y + h)]

def main():
    image_paths = ["image1.png", "image2.png", "image1.jpeg", "image2.jpeg"]

    for image_path in image_paths:
        image = cv2.imread(image_path)
        box = detect_box(image)
        if box:
            print("Image:", image_path)
            print("Box Coordinates:", box)
        else:
            print("No box detected in", image_path)

if __name__ == "__main__":
    main()
