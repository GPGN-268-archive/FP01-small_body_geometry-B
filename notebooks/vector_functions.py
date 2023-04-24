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