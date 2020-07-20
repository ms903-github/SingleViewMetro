import cv2
import numpy as np
from pylsd.lsd import lsd
import math
import itertools


# def calc_cross(line1, line2):
#     x1, x3, y1, y3 = line1
#     x2, x4, y2, y4 = line2
#     s1 = ((x4-x2)*(y1-y2) - (y4-y2)*(x1-x2)) * 0.5
#     s2 = ((x4-x2)*(y2-y3) - (y4-y2)*(x2-x3)) * 0.5
#     try:
#         cx = x1 + (x3-x1)*s1 / (s1+s2)
#         cy = y1 + (y3-y1)*s1 / (s1+s2)
#     except:
#         cx, cy = 0, 0
#     return(cx, cy)


# img = cv2.imread("house.jpg")
# x1, x2, y1, y2 = 1265, 1265, 443, 315
# img = cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 3)
# x1, x2, y1, y2 = 1373, 1372, 764, 608
# img = cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 3)

# cv2.imwrite("house_lines_test.png", img)

# print(calc_cross((1265, 1265, 443, 315), (1373, 1372, 764, 608)))

with open("test_output.wrl") as f:
    lines = f.readlines()
for line in lines:
    print(line)
