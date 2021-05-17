import cv2
import numpy as np

cap = cv2.VideoCapture(0)
# Frame Width
cap.set(3, 640)
# Frame Height
cap.set(4, 480)
# adjusting brightness
cap.set(10, 140)

while True:
    # cap.read return two values: a boolean that sees if the image reading was successful and the image itself.
    success, video = cap.read()
    # mirroring my image
    videoFlip = cv2.flip(video, 1)

    # converting our current image into the HSV color space
    hsv = cv2.cvtColor(videoFlip, cv2.COLOR_RGB2HSV)

    # These are the lower and upper HSV values of the color red that we are trying to detect from our shapes
    lowerRed = np.array([0, 100, 151])
    upperRed = np.array([179, 193, 206])

    # plugging in these lower and upper HSV values into a mask so we want to see only the shape itself
    mask = cv2.inRange(hsv, lowerRed, upperRed)

    # second property is a retrieval method and it retrieves the extreme outer contours.
    # third property is a takes in an approximation method that can  give you all of the information or compressed values. Simple means less values and a much cleaner lines.
    # once we have contours it will be saves in the contours variable.
    contours, hierachy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        perimeter = cv2.arcLength(cnt, True)
        # It approximates a contour shape to another shape
        approx = cv2.approxPolyDP(cnt, 0.02*perimeter, True)
        print(approx)
        # Defining a minimum threshold for our area so it does not catch any noise.
        if area > 500:
            cv2.drawContours(videoFlip, [approx], 0, (0, 255, 0), 2)
            x, y, w, h = cv2.boundingRect(approx)
            if len(approx) == 4:
                cv2.putText(videoFlip, "Rectangle", (x, y-20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            elif len(approx) == 3:
                cv2.putText(videoFlip, "Triangle", (x, y-20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            elif len(approx) == 5:
                cv2.putText(videoFlip, "Pentagon", (x, y-20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            elif len(approx) == 6:
                cv2.putText(videoFlip, "Hexagon", (x+45, y-20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            elif len(approx) == 8:
                cv2.putText(videoFlip, "Octagon", (x+45, y-20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            else:
                cv2.putText(videoFlip, "Circle", (x, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Shape Detection Demo", videoFlip)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
