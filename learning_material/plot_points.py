points_2D = [(1,2), (2,4), (0,8), (5,4)]

import matplotlib.pyplot as plt
xs = [i[0] for i in points_2D]
ys = [i[1] for i in points_2D]

plt.plot(xs, ys, '^')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
#plt.savefig('points2d.png')



import matplotlib.pyplot as plt
points_3D = [[1, 2, 4], [2, 4, 3], [0, 0, 1], [5, 4, 0]]
xs = [i[0] for i in points_3D]
ys = [i[1] for i in points_3D]
zs = [i[2] for i in points_3D]


fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(xs, ys, zs, marker='o')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

plt.show()