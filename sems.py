import pickle
from students import *
from relations import *
from courses import *

def sems():
	try:
		with open('files/sems.dat', 'rb+') as f:
			sems = pickle.load(f)
	except:
		print 'Empty'
		sems = []