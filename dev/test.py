import numpy as np
import plotly.graph_objects as go

import mesh_raycast

x=[]
y=[]
z=[]
i=[]
j=[]
k=[]
#x1=[]
#y1=[]
#z1=[]
liner=[]
with open('/Users/fnoic/PycharmProjects/python-mesh-raycast/data/tri_sphere_simple.obj') as of:
#with open('/home/fnoic/PycharmProjects/python-mesh-raycast/data/tri_sphere_simple.obj') as of:
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
            b=0
    a = 0

triangles = np.array(liner, dtype='f4')
#triangles = triangles.copy(order='C')
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
x1, y1, z1 = triangles.T
num_nodes_single = int(len(liner))
f_ind = np.array([i for i in range(num_nodes_single)])
i1=(np.arange(0, num_nodes_single, 3)).tolist()
j1=(np.arange(1, num_nodes_single, 3)).tolist()
k1=(np.arange(2, num_nodes_single, 3)).tolist()


fig = go.Figure(data=[
    go.Mesh3d(
        x=x1,
        y=y1,
        z=z1,
        # colorbar_title='z',
        # colorscale=[[0, 'gold'],
        #            [0.5, 'mediumturquoise'],
        #            [1, 'magenta']],
        # intensity = np.linspace(0, 1, 12, endpoint=True),
        # intensitymode='cell',
        i=i1,
        j=j1,
        k=k1,
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
