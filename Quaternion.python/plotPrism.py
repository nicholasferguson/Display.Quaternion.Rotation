import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection

def new_subplot(self):
                nsubplots = len(self.__subplots) + 1

                for i, subplot in enumerate(self.__subplots):
                        subplot.change_geometry(nsubplots, 1, i + 1)

                subplot = self.figure.add_subplot(nsubplots, 1, nsubplots)
                subplot.grid(True)

                self.__subplots.append(subplot)
                self.__subplot = subplot

def plot_prism(prism_definition1, prism_definition2):
    prism_definition_array1 = [
        np.array(list(item))
        for item in prism_definition1
    ]
    prism_definition_array2 = [
        np.array(list(item))
        for item in prism_definition2
    ]
    pt1x = (prism_definition_array1[1][0])
    pt1y = (prism_definition_array1[2][1])
    pt1z = (prism_definition_array1[3][2])

    pt2x = (prism_definition_array2[1][0])
    pt2y = (prism_definition_array2[2][1])
    pt2z = (prism_definition_array2[3][2])
#================================
    points1 = []
    points1 += prism_definition_array1
    vectors1 = [
        prism_definition_array1[1] - prism_definition_array1[0],
        prism_definition_array1[2] - prism_definition_array1[0],
        prism_definition_array1[3] - prism_definition_array1[0]
    ]

    points1 += [prism_definition_array1[0] + vectors1[0] + vectors1[1]]
    points1 += [prism_definition_array1[0] + vectors1[0] + vectors1[2]]
    points1 += [prism_definition_array1[0] + vectors1[1] + vectors1[2]]
    points1 += [prism_definition_array1[0] + vectors1[0] + vectors1[1] + vectors1[2]]

    points1 = np.array(points1)

    edges1 = [
        [points1[0], points1[3], points1[5], points1[1]],
        [points1[1], points1[5], points1[7], points1[4]],
        [points1[4], points1[2], points1[6], points1[7]],
        [points1[2], points1[6], points1[3], points1[0]],
        [points1[0], points1[2], points1[4], points1[1]],
        [points1[3], points1[6], points1[7], points1[5]]
    ]

#================================
    points2 = []
    points2 += prism_definition_array2
    vectors2 = [
        prism_definition_array2[1] - prism_definition_array2[0],
        prism_definition_array2[2] - prism_definition_array2[0],
        prism_definition_array2[3] - prism_definition_array2[0]
    ]

    points2 += [prism_definition_array2[0] + vectors2[0] + vectors2[1]]
    points2 += [prism_definition_array2[0] + vectors2[0] + vectors2[2]]
    points2 += [prism_definition_array2[0] + vectors2[1] + vectors2[2]]
    points2 += [prism_definition_array2[0] + vectors2[0] + vectors2[1] + vectors2[2]]

    points2 = np.array(points2)

    edges2 = [
        [points2[0], points2[3], points2[5], points2[1]],
        [points2[1], points2[5], points2[7], points2[4]],
        [points2[4], points2[2], points2[6], points2[7]],
        [points2[2], points2[6], points2[3], points2[0]],
        [points2[0], points2[2], points2[4], points2[1]],
        [points1[3], points1[6], points1[7], points1[5]]
    ]
#===============================
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    faces1 = Poly3DCollection(edges1, linewidths=1, edgecolors='k')
    faces1.set_facecolor((0,1,1,0.1))

    ax.add_collection3d(faces1)
    ax.plot(pt1x, pt1y, pt1z, markerfacecolor='k', markeredgecolor='k', marker='o', markersize=10, alpha=0.6)
    ax.plot(pt2x, pt2y, pt2z, markerfacecolor='k', markeredgecolor='k', marker='o', markersize=10, alpha=0.6)

    faces2 = Poly3DCollection(edges2, linewidths=1, edgecolors='k')
    faces2.set_facecolor((0,0,1,0.1))

    ax.add_collection3d(faces2)

    # Plot the points themselves to force the scaling of the axes
  #  ax.scatter(points1[:,0], points1[:,1], points1[:,2], s=1)

 #   ax.set_aspect('auto')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Setting the axes properties
    ax.set_xlim3d([-4.0, 4.0])
    ax.set_ylim3d([-2.0, 2.0])
    ax.set_zlim3d([-4.0, 4.0])
  #  return ax

    plt.show()


