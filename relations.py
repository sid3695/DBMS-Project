import pickle
from students import *
from archives import *
from courses import *
from course_allocations import *

relations = []

def Relations():
	try:
		with open('files/relations.dat', 'rb+') as f:
			relations = pickle.load(f)
	except:
		print 'Empty'
		relations = []

	ch = int(raw_input('1 for add\n2 for del\n3 for upd\n'))
	if ch == 1:
		relation = {} #each entry is a dict
		relation['rollno'] = raw_input('rollno : ')
		relation['courseid'] = raw_input('Course id : ')
		
		#apply constraints

		if relation not in relations:
			relations.append(relation)
		#
		writer2f(relations)
	print relations

def writer2f(relations):
	with open('files/relations.dat','wb') as f:
		pickle.dump(relations,f)	