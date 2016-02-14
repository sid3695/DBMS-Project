import pickle
from students import *
from sems import *
from teachers import *
from courses import *

def courses():
	try:
		with open('files/sems.dat', 'rb+') as f:
			sems = pickle.load(f)
	except:
		print 'Empty'
		sems = []