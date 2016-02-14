import pickle
from students import *
from archives import *
from courses import *
from course_allocations import *
import datetime

relations = []

def check_Expiry():
	try:
		with open('files/relations.dat', 'rb+') as f:
			relations = pickle.load(f)
	except:
		print 'Empty'
		relations = []

	try:
		with open('files/archived.dat', 'rb+') as f:
			archived = pickle.load(f)
	except:
		print 'Empty'
		archived = []
		
	for i in xrange(len(relations)):
		if(relations[i]['dor'] + datetime.timedelta(months=6) < datetime.datetime.now()):
			archived.append(relations[i])
			del relations[i]	
			writer2arc(archived)
			writer2f(relations)		


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
		relation['co_alloc_id'] = raw_input('Course Alloc id : ')
		print datetime.datetime.now()
		relation['dor']=datetime.datetime.now()
		
		#apply constraints

		if relation not in relations:
			relations.append(relation)
		#
		writer2f(relations)
	print relations

def writer2f(relations):
	with open('files/relations.dat','wb') as f:
		pickle.dump(relations,f)	

def writer2arc(archives):
	with open('files/archived.dat','wb') as f:
		pickle.dump(archives,f)	