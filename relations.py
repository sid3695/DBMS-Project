import pickle
from students import *
from sems import *
from courses import *

def relations():
	try:
		with open('files/relations.dat', 'rb+') as f:
			relations = pickle.load(f)
	except:
		print 'Empty'
		relations = []