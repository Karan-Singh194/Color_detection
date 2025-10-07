import numpy as np
import cv2


def get_limits(color):
    if color == [0, 0, 0]: #black
        return np.array([0, 0, 0]), np.array([180, 255, 50])

    if color == [255, 255, 255]: #white
        return np.array([0, 0, 200]), np.array([180, 30, 255])

    if color == [0, 0, 255]: #red
        # handle outside, since red needs two ranges
        return [(np.array([0, 120, 70]), np.array([10, 255, 255])),
                (np.array([170, 120, 70]), np.array([180, 255, 255]))]

    # For colors like blue, green, yellow
    c = np.uint8([[color]])
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    lowerLimit = (hsvC[0][0][0] - 15, 100, 100)
    upperLimit = (hsvC[0][0][0] + 15, 255, 255)

    return np.array(lowerLimit), np.array(upperLimit)
