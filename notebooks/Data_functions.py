import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def getData(path):
	"""
	This function takes the path to an obj file, reads it and then returns two pandas data frames. the first is for verticies the second is for faces (refering to the verticies)
	
	path: str
			the path to the file you want to read as a string.
	"""
	# open and read chosen file, split the file by lines and store them in a list
	with open(path, 'r') as f:
		file = f.read()
		file = file.splitlines()
	# add all non commented lines to a new list (containing all verticies and faces)
	vfs = []
	for q in file:
		if not '#' in q:
			vfs.append(q)
	verts = []
	faces = []
	# remove unwanted wightspace
	for i in range(vfs.count('')):
		vfs.remove('')
	
	for i in range(len(vfs)):
		vfs[i] = vfs[i].split(' ')
		for j in range(vfs[i].count('')):
			vfs[i].remove('')
	# split the data into seperate lists
		if vfs[i][0] == 'v':
			verts.append(vfs[i][1:])

		elif vfs[i][0] == 'f':
			faces.append(vfs[i][1:])
	# convert lists into data frames
	verts = np.array(verts, dtype= float)
	faces = np.array(faces, dtype= float)
	
	df_f = pd.DataFrame(faces, columns= ['x','y','z'])
	df_v = pd.DataFrame(verts, columns= ['x','y','z'])
	# this line can be used to normalize the verticies data into a unit cube, it has been commented out to prevent interference in surface area calculations
	#df_v= (df_v-(df_v.max(0)+df_v.min(0))/2)/max(df_v.max(0)-df_v.min(0))
	
	return df_v, df_f
	
# geometric center function

def obj_center(df_vert):
    '''
    This function takes a dataframe containing the x, y, and z coordinates of several points and returns
    the coordinates of the geometric center of that object
    
    Parameters:
        df_vert: a three-dimensional dataframe of the object verticies (x,y,z)
            - must have numeric entries
        
    Returns:
        center_point: a list containing the x, y, and z coordinates of the geometric center
    '''
    av_x = np.sum(df_vert['x'])/len(df_vert['x'])
    av_y = np.sum(df_vert['y'])/len(df_vert['y'])
    av_z = np.sum(df_vert['z'])/len(df_vert['z'])
    
    center_point = [av_x,av_y,av_z]
    return center_point

# verticies vectors function

def vert_vectors(df_vert):
    '''
    This function takes a dataframe containing the x, y, and z coordinates of several points and returns
    the vectors from the center point to each of those points
    
    Parameters:
        df_vert: a three-dimensional dataframe of the object verticies (x,y,z)
            - must have numeric entries
            
    Returns:
        v: a dataframe with the same dimensions as df_vert with the x, y, and z components of the verticies 
        vectors
    
    '''
    v = df_vert - obj_center(df_vert)
    return v

# Normal Vectors

def normal_vectors(df_v,df_f):
    
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