import numpy as np
from calc_vpoints import calc_cross
import cv2
import math

lvpoint, rvpoint, dvpoint = np.load("lvpoint.npy"), np.load(
    "rvpoint.npy"), np.load("dvpoint.npy")
x2, y2 = dvpoint
x1, y1 = lvpoint
x0, y0 = rvpoint
img = cv2.imread("house.jpg")
h, w, _ = img.shape
# center of camera
cx, cy = w//2, h//2
# focal length
f = math.sqrt(abs((x0-cx)*(x1-cx)+(y0-cy)*(y1-cy)))
# rotation matrix
r = np.array([[x0-cx, y0-cy, f], [x1-cx, y1-cy, f], [x2-cx, y2-cy, f]]).T
print(r)
np.save("rmat.npy", r)
