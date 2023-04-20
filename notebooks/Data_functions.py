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
	