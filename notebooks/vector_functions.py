from Data_functions import getData
import numpy as np
import plotly.graph_objects as go

def switchax(vectors):

    n_vectors = []
    for i in range(vectors.shape[1]):
        n_vectors.append([vectors[0][i], vectors[1][i], vectors[2][i]])
    return np.array(n_vectors)
	
	
def getNormal(path):
	points, faces = getData('../data/obj/Psyche Hanuš.obj')
	normals = []
	for face in faces:
		v1 = switchax(np.array([points['x'][faces['x']-1], points['y'][faces['x']-1], points['z'][faces['x']-1]]))
		v2 = switchax(np.array([points['x'][faces['y']-1], points['y'][faces['y']-1], points['z'][faces['y']-1]]))
		v3 = switchax(np.array([points['x'][faces['z']-1], points['y'][faces['z']-1], points['z'][faces['z']-1]]))

	normal = np.cross(v2 - v1, v3 - v1)
	normals.append(normal)
	
	return normals


def plotNormals(path):

	with open(path) as f:
		lines = f.readlines()

	vertices = []
	faces = []

	for line in lines:
		if line.startswith('v '):
			vertex = [float(i) for i in line.split()[1:]]
			vertices.append(vertex)
		elif line.startswith('f '):
			face = [int(i.split('/')[0]) - 1 for i in line.split()[1:]]
			faces.append(face)

	vertices = np.array(vertices)
	faces = np.array(faces)

	normals = []
	midpoints = []
	for face in faces:
		v1 = vertices[face[0]]
		v2 = vertices[face[1]]
		v3 = vertices[face[2]]
		normal = np.cross(v2 - v1, v3 - v1)
		midpoint = (v1 + v2 + v3) / 3
		normals.append(normal)
		midpoints.append(midpoint)

	normals = np.array(normals)
	midpoints = np.array(midpoints)

	fig = go.Figure(data=[go.Mesh3d(x=vertices[:, 0], y=vertices[:, 1], z=vertices[:, 2], i=faces[:, 0], j=faces[:, 1], k=faces[:, 2], facecolor=(200,200,200), flatshading=True, vertexcolor=(0,0,0))])

	fig.add_trace(go.Cone(x=midpoints[:, 0], y=midpoints[:, 1], z=midpoints[:, 2], u=normals[:, 0], v=normals[:, 1], w=normals[:, 2], sizeref=5))

	fig.show()