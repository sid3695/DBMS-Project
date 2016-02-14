import pickle
from students import *
from sems import *
from teachers import *
from courses import *

def courses():
	try:
		with open('files/courses.dat', 'rb+') as f:
			courses = pickle.load(f)
	except:
		print 'Empty'
		courses = []