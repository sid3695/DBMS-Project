import pickle
from students import *
from archives import *
from courses import *

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
		relation = {} #each course is a dict
		relation['rollno'] = raw_input('rollno : ')
		relation['courseid'] = raw_input('Course id : ')
		
		#apply contra
		relations.append(relation)
		writer2f(relation)
	print relations

def writer2f(courses):
	with open('files/relations.dat','wb') as f:
		pickle.dump(relations,f)	