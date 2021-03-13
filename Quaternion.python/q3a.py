# In notes below, 'overload' is a computer science term

# We examine two overloaded quaternions, both use
# a format of [scalar, x, y, z] and not [x,y,z,scalar]

# First overload is a quaternion that is a rotator.
# [scalar, X, Y, Z] becomes
# [scalar = cos of rotating angle in radians,
#   X = rotating angle about x axis = 0 radians,
#   Y = rotating angle about y axis = 0 radians,
#   Z = rotating angle about z axis = sin of scalar radians]

# 2nd overloaded is a quaternion as a pure quaternion;
# [scalar, X, Y, Z] becomes [0, X, Y, Z].
# Where X Y Z represents a point's coordinates in 3D space.

# Procedure: quaternion rotator multiplied with pure quaternion and result
# is a 2nd pure quaternion: P' = ((rP)r-1)
# r is rotator, r-1 is conjugate of rotator and P is pure quaternion.

# To display this rotation,
# we fill out wire frames of both pure quaternions.
# Both wire frames have a 3D origin, as a vertex (0,0,0)
# Highlighted are original and rotated points

# To prove that wire frames are correct, you need to rotate
# image along its axes.

# Note this pure quaternion, as a point, could be a significant point in
# any geometric shape.  It must keep its shape, post rotation.  Ex:
# it could be center of a sphere.

import math
import numpy as np
import matplotlib.pyplot as plt
from plotPrism import plot_prism  #plotprism.py

def normalize(v, tolerance=0.00001):
    mag2 = sum(n * n for n in v)
    if abs(mag2 - 1.0) > tolerance:
        mag = math.sqrt(mag2)
        v = tuple(n / mag for n in v)
    return np.array(v)

# pq is pure quaternion
# r is rotator quaternion
def quaternion_mult(r,pq):
    return [pq[0]*r[0]-pq[1]*r[1]-pq[2]*r[2]-pq[3]*r[3],
            pq[0]*r[1]+pq[1]*r[0]+pq[2]*r[3]-pq[3]*r[2],
            pq[0]*r[2]-pq[1]*r[3]+pq[2]*r[0]+pq[3]*r[1],
            pq[0]*r[3]+pq[1]*r[2]-pq[2]*r[1]+pq[3]*r[0]]

# pq is pure quaternion
# rq is rotator quaternion
def point_rotation_by_quaternion(pq,rq):
    r = normalize(rq)
    r_conj = [r[0],-1*r[1],-1*r[2],-1*r[3]]
    return quaternion_mult(quaternion_mult(r,pq),r_conj)

degrees = math.pi/180;
rot = 180*degrees;
# for rotating about an axis.
w = math.cos(rot/2.);
ax = math.sin(rot/2.);
# quaternion format is [scalar, x, y ,z]
pq = [0, 1, 2, 3]  # pure quaternion.  Scalar is zero.
rq = [w, 0, 0, ax]  # play with ax on different axis: x,y,z  Change values of w and ax.

pq2 = point_rotation_by_quaternion(pq,rq)
print(pq2)

# Fill in a start prism wire frame, using point and a 3D origin as vertices
# Highlight point as vertex

p1 = np.array([0.,0.,0.])
p2 = np.array([pq[1],0.,0.])
p3 = np.array([0.,pq[2],0.])
p4 = np.array([0.,0.,pq[3]])

prism1 = [
    (p1[0],p1[1],p1[2]), (p2[0],p2[1],p2[2]), (p3[0],p3[1],p3[2]), (p4[0],p4[1],p4[2])
]

# Fill in a rotated prism wire frame, using point and a 3D origin as vertices
# Highlight point as vertex

p1A = np.array([0.,0.,0.])
p2A = np.array([pq2[1],0.,0.])
p3A = np.array([0.,pq2[2],0.])
p4A = np.array([0.,0.,pq2[3]])

prism2 = [
    (p1A[0],p1A[1],p1A[2]), (p2A[0],p2A[1],p2A[2]), (p3A[0],p3A[1],p3A[2]), (p4A[0],p4A[1],p4A[2])
]

# to prove that plot is correct, you need to rotate image along its axes.

plot_prism(prism1,prism2)



