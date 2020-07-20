import cv2
import numpy as np
from pylsd.lsd import lsd
import math
import itertools


def calc_cross(line1, line2):
    x1, x3, y1, y3 = line1
    x2, x4, y2, y4 = line2
    s1 = ((x4-x2)*(y1-y2) - (y4-y2)*(x1-x2)) * 0.5
    s2 = ((x4-x2)*(y2-y3) - (y4-y2)*(x2-x3)) * 0.5
    try:
        cx = x1 + (x3-x1)*s1 / (s1+s2)
        cy = y1 + (y3-y1)*s1 / (s1+s2)
    except:
        cx, cy = 0, 0
    return(cx, cy)


def main():
    img = cv2.imread("house.jpg")
    h, w, _ = img.shape
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    threshold = 100
    ret, gray = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)
    linesL = lsd(gray)
    longline = []
    for line in linesL:
        x1, y1, x2, y2 = map(int, line[:4])
        # img = cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 3)
        if math.sqrt((x2-x1)**2 + (y2-y1)**2) > 120:
            # 赤線を引く
            img = cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 3)
            longline.append((x1, x2, y1, y2))

    cv2.imwrite("house_lines_pylsd.png", img)
    # 傾きが正
    positive1 = []
    positive2 = []
    # 傾きが負
    negative1 = []
    negative2 = []
    # ほぼ縦線
    discarded = []
    for line in longline:
        x1, x2, y1, y2 = line
        if abs(x1 - x2) < 5:
            discarded.append(line)
            continue
        if x2 < x1:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        angle = (y2 - y1) / (x2 - x1)
        if angle > 0 and x2 < w//2:
            positive1.append(line)
        elif angle > 0 and x2 > w//2:
            positive2.append(line)
        elif angle < 0 and x2 < w//2:
            negative1.append(line)
        elif angle < 0 and x2 > w//2:
            negative2.append(line)

    lvpoint = [w//2, h//2]
    lvlines = [0, 0]
    rvpoint = [-11000000, 0]
    rvlines = [0, 0]
    for line1, line2 in itertools.product(positive1, negative1):
        cx, cy = calc_cross(line1, line2)
        if cx < lvpoint[0]:
            lvpoint = cx, cy
            lvlines = line1, line2
    for line1, line2 in itertools.product(positive2, negative2):
        cx, cy = calc_cross(line1, line2)
        if cx > rvpoint[0]:
            rvpoint = cx, cy
            rvlines = line1, line2
    print("left-side vanishing point:{}".format(lvpoint))

    print("right-side vanishing point:{}".format(rvpoint))

    np.save("lvpoint.npy", np.array(lvpoint))
    np.save("rvpoint.npy", np.array(rvpoint))

    dvpoint = [0, 1000000]
    dvlines = []
    for line1, line2 in itertools.product(discarded, discarded):
        cx, cy = calc_cross(line1, line2)
        if cy < abs(dvpoint[1]) and 0 < cx < w:
            dvpoint = cx, cy
            dvlines = line1, line2
    print("vertical vanishing point:{}".format(dvpoint))
    print(dvlines)

    np.save("dvpoint.npy", np.array(dvpoint))


if __name__ == "__main__":
    main()

# img = cv2.imread("house.jpg")
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# threshold = 100
# ret, gray = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)
# lines = cv2.HoughLinesP(gray, rho=1, theta=np.pi/360,
#                         threshold=400, minLineLength=500, maxLineGap=5)
# print(lines)
# for line in lines:
#     x1, y1, x2, y2 = line[0]

#     # 赤線を引く
#     red_line_img = cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 3)
#     cv2.imwrite("house_lines_opencv.png", red_line_img)
