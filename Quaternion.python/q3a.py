# In notes below, 'overload' is a computer science term

# Procedure: We examine two overloaded quaternions, both use
# a format of [scalar, x, y, z] and not [x,y,z,scalar]

# First overload is a quaternion that is a rotator.
# [scalar, X, Y, Z] becomes
# [scalar = cos of rotating angle in radians,
#   X = rotating angle about x axis = 0 radians,
#   Y = rotating angle about y axis = sin of scalar radians,
#   Z = rotating angle about z axis = 0 radians]

# 2nd overloaded is a quaternion as a pure quaternion;
# [scalar, X, Y, Z] becomes [0, X, Y, Z].
# Where X Y Z represents a point's coordinates in 3D space.

# Procedure: quaternion rotator 'wedge product' with pure quaternion and result
# is a 2nd pure quaternion.

# To display this rotation,
# we fill out wire frames of both pure quaternions.
# Both wire frames have a 3D origin, as a vertex (0,0,0)
# Highlighted are original and rotated points

# To prove that wire frames are correct, you need to rotate
# image along its axes.

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

def quaternion_mult(q,r):
    return [r[0]*q[0]-r[1]*q[1]-r[2]*q[2]-r[3]*q[3],
            r[0]*q[1]+r[1]*q[0]-r[2]*q[3]+r[3]*q[2],
            r[0]*q[2]+r[1]*q[3]+r[2]*q[0]-r[3]*q[1],
            r[0]*q[3]-r[1]*q[2]+r[2]*q[1]+r[3]*q[0]]

def point_rotation_by_quaternion(point,qq):
    r = point
    q = normalize(qq)
    q_conj = [q[0],-1*q[1],-1*q[2],-1*q[3]]
    return quaternion_mult(quaternion_mult(q,r),q_conj)

degrees = math.pi/180;
rot = 180*degrees;
# for rotating about an axis.
w = math.cos(rot/2.);
ax = math.sin(rot/2.);
# quaternion format is [scalar, x, y ,z]
pts1 = [0, 1, 2, 3]  # pure quaternion.  Scalar is zero.
quat = [w, 0, ax, 0]  # play with ax as x,y,z  And change w

qq = point_rotation_by_quaternion(pts1,quat)
print(qq)

# Fill in a start prism wire frame, using point and a 3D origin as vertices
# Highlight point as vertex

p1 = np.array([0.,0.,0.])
p2 = np.array([pts1[1],0.,0.])
p3 = np.array([0.,pts1[2],0.])
p4 = np.array([0.,0.,pts1[3]])

prism1 = [
    (p1[0],p1[1],p1[2]), (p2[0],p2[1],p2[2]), (p3[0],p3[1],p3[2]), (p4[0],p4[1],p4[2])
]

# Fill in a rotated prism wire frame, using point and a 3D origin as vertices
# Highlight point as vertex

p1A = np.array([0.,0.,0.])
p2A = np.array([qq[1],0.,0.])
p3A = np.array([0.,qq[2],0.])
p4A = np.array([0.,0.,qq[3]])

prism2 = [
    (p1A[0],p1A[1],p1A[2]), (p2A[0],p2A[1],p2A[2]), (p3A[0],p3A[1],p3A[2]), (p4A[0],p4A[1],p4A[2])
]

# to prove that plot is correct, you need to rotate image along its axes.

plot_prism(prism1,prism2)



