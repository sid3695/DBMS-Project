import pickle
from students import *
from relations import *
from courses import *

def archives():
	try:
		with open('files/archived.dat', 'rb+') as f:
			archived = pickle.load(f)
	except:
		print 'Empty'
		archived = []