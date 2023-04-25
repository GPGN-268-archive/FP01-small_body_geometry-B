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
    
# verticies vectors function

def vert_vectors(path_to_file):
    '''
    docstring
    
    This function computes the three dimensional vector components for the vectors connecting the
    the geometric center to each of the verticies.
    
    Parameters: 
        vert_df: a dataframe containing the x, y, and z coordinates of all verticies
        
    Returns:
        v: a dataframe containing the x, y, and z vector components for each of the verticies
    '''
    getData(path_to_file)
    
    v = df_v - obj_center(path_to_file)
    return v

# Normal Vectors

def normal_vectors(path_to_file):
    
    '''
    docstring:
    This function takes data from the faces and verticies of a given object and returns the normal vectors 
    for each face.
    
    Parameters: 
        df_v: dataframe containing the verticies coordinates of the object
        
        df_f: dataframe containing the face references for the object
        
    Returns:
        df_N: dataframe containing the normal vectors for each face
        
        face_center: dataframe containing the coordinates of the center points of each face
    '''
    
    getData(path_to_file)
    
    verts = []
    verts_x = []
    verts_y = []
    verts_x = []
    points= ['x','y','z']

    for point in points:
        verts = []
        for vert_num in df_f[point]:
            # print(vert_num)
            vert_x = df_v['x'][vert_num-1]
            vert_y = df_v['y'][vert_num-1]
            vert_z = df_v['z'][vert_num-1]

            vert_coords = [vert_x , vert_y , vert_z]
            # print(vert_coords)

            verts.append(vert_coords)
        if point == 'x':
            verts_x = verts
        elif point == 'y':
            verts_y = verts
        elif point == 'z':
            verts_z = verts
        #print(point)

    # the coordinates of the first vertex of the face
    df_X = pd.DataFrame(verts_x, columns = ['x', 'y','z'])

    # the coordinates of the second vertex of the face
    df_Y = pd.DataFrame(verts_y, columns = ['x', 'y','z'])

    # the coordinates of the third vertex of the face
    df_Z = pd.DataFrame(verts_z, columns = ['x', 'y','z'])
    
    # find the center of each face
    face_center = (df_X + df_Y + df_Z)/3

    # the vector connecting the first and second points   
    V_12 = df_Y - df_X
    
    # the vector connecting the first and third points
    V_13 = df_Z - df_X

    # computing the normal vectors
    norms = np.cross(V_12,V_13)
    df_N = pd.DataFrame(norms, columns = ['u', 'v','w'])

    return df_N, face_center

def vert_vectors2(path_to_file):
    
    getData(path_to_file)
    
    verts = []
    verts_x = []
    verts_y = []
    verts_x = []
    points= ['x','y','z']

    for point in points:
        verts = []
        for vert_num in df_f[point]:
            # print(vert_num)
            vert_x = df_v['x'][vert_num-1]
            vert_y = df_v['y'][vert_num-1]
            vert_z = df_v['z'][vert_num-1]

            vert_coords = [vert_x , vert_y , vert_z]
            # print(vert_coords)

            verts.append(vert_coords)
        if point == 'x':
            verts_x = verts
        elif point == 'y':
            verts_y = verts
        elif point == 'z':
            verts_z = verts
        #print(point)

    # the coordinates of the first vertex of the face
    df_X = pd.DataFrame(verts_x, columns = ['x', 'y','z'])
    #print(df_X)
    #print('======')

    # the coordinates of the second vertex of the face
    df_Y = pd.DataFrame(verts_y, columns = ['x', 'y','z'])
    #print(df_Y)
    #print('======')

    # the coordinates of the third vertex of the face
    df_Z = pd.DataFrame(verts_z, columns = ['x', 'y','z'])
    #print(df_Z)
    
    v = df_X - obj_center(path_to_file)
    return v