import cv2
import numpy as np

def find_ellipse_equation(image_path):
    # Read the image
    img = cv2.imread(image_path, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Use Canny edge detection to find edges in the image
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)

    # Find contours in the edged image
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Filter out small contours
    contours = [c for c in contours if len(c) > 5]

    if contours:
        # Fit ellipse to the largest contour
        largest_contour = max(contours, key=cv2.contourArea)
        ellipse_params = cv2.fitEllipse(largest_contour)

        # Draw ellipse on the original image
        cv2.ellipse(img, ellipse_params, (0, 255, 0), 2)

        # Show the image with the detected ellipse
        cv2.imshow("Detected Ellipse", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print(f"Parameters for the ellipse: {ellipse_params}")
        return ellipse_params
    else:
        print("No ellipse detected in the image.")
        return None 

# Example usage
image_path = "ellipse.png"
ellipse_params = find_ellipse_equation(image_path)
if ellipse_params:
    center, axes, angle = ellipse_params
    a = max(axes) / 2.0
    b = min(axes) / 2.0
    x0, y0 = center

    print("Ellipse equation parameters:")
    print(f"Center: ({x0}, {y0})")
    print(f"Semi-Major Axis (a): {a}")
    print(f"Semi-Minor Axis (b): {b}")
    print(f"Angle of Rotation: {angle}")
    print(f"Ellipse Equation: ((x - {x0})^2 / {a}^2) + ((y - {y0})^2 / {b}^2) = 1")
