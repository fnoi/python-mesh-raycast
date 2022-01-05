import numpy as np
import plotly.graph_objects as go

import mesh_raycast

x=[]
y=[]
z=[]
i=[]
j=[]
k=[]
x1=[]
y1=[]
z1=[]
liner=[]
with open('/home/fnoic/PycharmProjects/python-mesh-raycast/data/tri_sphere_simple.obj') as of:
    for line in of:
        if line.startswith('v'):
            x.append(float(line.split()[1]))
            y.append(float(line.split()[2]))
            z.append(float(line.split()[3]))
        elif line.startswith('f'):
            i_temp = int(line.split()[1])-1
            i.append(i_temp)
            liner.append([x[i_temp], y[i_temp], z[i_temp]])
            j_temp = int(line.split()[2])-1
            j.append(j_temp)
            liner.append([x[j_temp], y[j_temp], z[j_temp]])
            k_temp = int(line.split()[3])-1
            k.append(k_temp)
            liner.append([x[k_temp], y[k_temp], z[k_temp]])
    a = 0

triangles = np.array(liner, dtype='f4')
triangles = triangles.copy(order='C')
# triangles = np.array([x, y, z], dtype='f4').T
# triangles = triangles.copy(order='C')

# triangles1 = np.array(
#     [
#         [0.0, 0.0, 0.0],
#         [1.0, 0.0, 0.0],
#         [0.0, 1.0, 0.0],
#         [1.0, 1.0, 10.0],
#         [3.0, 7.0, 10.0],
#         [0.0, 3.0, 10.0]
#     ],
#     dtype='f4')
#
x, y, z = triangles.T

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

# index = np.array([
#     [0, 1, 2],
# ], dtype='i4')

result = mesh_raycast.raycast(source=(0.4, 0.8, 5.0), direction=(0.0, 0.0, -1.0), mesh=triangles)
a=0
