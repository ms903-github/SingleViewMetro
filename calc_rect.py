import numpy as np
import math


def projection(coord, rmat):
    coord = np.append(coord, 1)
    return np.dot(rmat, coord)


# rmat = np.array(rmat)
# p1, p2, p3, p4 = rect
# pp1 = projection(p1, rmat)
# pp2 = projection(p2, rmat)
# pp3 = projection(p3, rmat)
# pp4 = projection(p4, rmat)
# origin, endpoint, dist = coord["origin"], coord["endpoint"], coord["distance"]
# p_origin, p_endpoint = projection(origin, rmat), projection(endpoint, rmat)
# scale = dist / math.sqrt((p_origin[0]-p_endpoint[0])**2 + (
#     p_origin[1]-p_endpoint[1])**2 + (p_origin[2]-p_endpoint[2])**2)
# print(pp1*scale)
# print(pp2*scale)
# print(pp3*scale)
# print(pp4*scale)

# rect = np.load("plane4.npy", allow_pickle=True)
coord = np.load("origin.npy", allow_pickle=True).item()
p1 = np.load("point1.npy", allow_pickle=True).item()
p2 = np.load("point2.npy", allow_pickle=True).item()
rmat = np.load("rmat.npy", allow_pickle=True)
origin, endpoint, dist = coord["origin"], coord["endpoint"], coord["distance"]
# translation
tvec = np.append(coord["origin"], 1)
tvec = tvec[:, np.newaxis]
pmat = np.concatenate([rmat, tvec], 1)
proj = projection(endpoint, pmat.T)
print(dist)
print(proj)
scale = dist / proj[2]
print(proj * scale)

# for point
# origin, endpoint, dist = p1["origin"], p1["endpoint"], p1["distance"]
# proj1 = projection(endpoint, pmat.T)
# scale = dist / proj1[2]
# print(proj1 * scale)
# origin, endpoint, dist = p2["origin"], p2["endpoint"], p2["distance"]
# proj2 = projection(endpoint, pmat.T)
# scale = dist / proj2[2]
# print(proj2 * scale)

# for quad
sq1 = np.load("rect1.npy", allow_pickle=True).item()
p1, p2, p3, p4 = sq1["coords"]
d1, d2, d3, d4 = sq1["zval"][0]
d1, d2, d3, d4 = int(d1), int(d2), int(d3), int(d4)
pp1 = projection(p1, pmat.T)
scale = d1 / pp1[2]
pp1 = pp1 * scale
print(pp1[:3])
pp2 = projection(p2, pmat.T)
scale = d2 / pp2[2]
pp2 = pp2 * scale
print(pp2[:3])
pp3 = projection(p3, pmat.T)
scale = d3 / pp3[2]
pp3 = pp3 * scale
print(pp3[:3])
pp4 = projection(p4, pmat.T)
scale = d4 / pp4[2]
pp4 = pp4 * scale
print(pp4[:3])
