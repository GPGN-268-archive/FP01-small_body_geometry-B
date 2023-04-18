import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def getData(path):
	with open(path, 'r') as f:
		file = f.read()
		file = file.splitlines()
	vfs = []
	for q in file:
		if not '#' in q:
			vfs.append(q)
	verts = []
	faces = []
	
	for i in range(vfs.count('')):
		vfs.remove('')
	
	for i in range(len(vfs)):
		vfs[i] = vfs[i].split(' ')
		for j in range(vfs[i].count('')):
			vfs[i].remove('')
		if vfs[i][0] == 'v':
			verts.append(vfs[i][1:])

		elif vfs[i][0] == 'f':
			faces.append(vfs[i][1:])
	
	verts = np.array(verts, dtype= float)
	faces = np.array(faces, dtype= float)
	
	df_f = pd.DataFrame(faces, columns= ['x','y','z'])
	df_v = pd.DataFrame(verts, columns= ['x','y','z'])
	#df_v= (df_v-(df_v.max(0)+df_v.min(0))/2)/max(df_v.max(0)-df_v.min(0))
	
	return df_v, df_f
	