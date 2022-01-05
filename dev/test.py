import numpy as np
import plotly.graph_objects as go

import mesh_raycast

x=[]
y=[]
z=[]
i=[]
j=[]
k=[]
with open('/home/fnoic/PycharmProjects/python-mesh-raycast/data/tri_sphere_simple.obj') as of:
    for line in of:
        if line.startswith('v'):
            x.append(float(line.split()[1]))
            y.append(float(line.split()[2]))
            z.append(float(line.split()[3]))
        elif line.startswith('f'):
            i.append(int(line.split()[1])-1)
            j.append(int(line.split()[2])-1)
            k.append(int(line.split()[3])-1)
    a = 0

triangles = np.array([x, y, z], dtype='f4').T
triangles = triangles.copy(order='C')

triangles1 = np.array(
    [
        [0.0, 0.0, 0.0],
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0],
        [1.0, 1.0, 10.0],
        [3.0, 7.0, 10.0],
        [0.0, 3.0, 10.0]
    ],
    dtype='f4')
#
# x, y, z = triangles.T

fig = go.Figure(data=[
    go.Mesh3d(
        x=x,
        y=y,
        z=z,
        # colorbar_title='z',
        # colorscale=[[0, 'gold'],
        #            [0.5, 'mediumturquoise'],
        #            [1, 'magenta']],
        # intensity = np.linspace(0, 1, 12, endpoint=True),
        # intensitymode='cell',
        i=i, #[0, 3, 0, 2],
        j=j, #[1, 4, 1, 4],
        k=k, #[2, 5, 5, 1],
        name='y',
        showscale=True
    )
])
fig.show()

index = np.array([
    [0, 1, 2],
], dtype='i4')

print(mesh_raycast.raycast((0.0, 0.0, 2.0), mesh_raycast.normalize((0.1, 0.2, -1.0)), triangles))
