import pickle
from students import *
from sems import *
from teachers import *
from courses import *

def courses():
	try:
		with open('files/teachers.dat', 'rb+') as f:
			teachers = pickle.load(f)
	except:
		print 'Empty'
		teachers = []