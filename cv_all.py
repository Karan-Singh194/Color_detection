import cv2
from PIL import Image
from util_all import get_limits

# Red → [0, 0, 255]
# Green → [0, 255, 0]
# Blue → [255, 0, 0]
# Yellow → [0, 255, 255]
# White → [255, 255, 255]
# Black → [0, 0, 0]
# color = [0, 0, 255]


def color_pick():
    x = int(input("Enter 1 = Red, 2 = Green, 3 = Blue, 4 = Yellow : "))
    tu = [[0, 0, 255], [0, 255, 0], [255, 0, 0], [0, 255, 255]]
    color = tu[x-1]
    return color


def color_detection():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()

        hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        if color == [0,0,255]:
            red_ranges = get_limits(color)  # This returns two pairs
            mask1 = cv2.inRange(hsvImage, red_ranges[0][0], red_ranges[0][1])
            mask2 = cv2.inRange(hsvImage, red_ranges[1][0], red_ranges[1][1])
            mask = mask1 | mask2   # Combine both
        else:
            lowerLimit, upperLimit = get_limits(color)
            mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

        mask_ = Image.fromarray(mask)
        bbox = mask_.getbbox()

        if bbox is not None:
            x1, y1, x2, y2 = bbox

            frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

        cv2.imshow('video Window', frame)

        if cv2.waitKey(1)  & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows

color = color_pick()
color_detection()