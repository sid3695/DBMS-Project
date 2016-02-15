import pickle
from relations import *
from students import *
from archives import *
from courses import *
import datetime
from utils import write_com


course_allocations = []

def union_list(a,b):
	return list(set(a) | set(b))


def Course_Allocations():
	try:
		with open('files/course_allocations.dat', 'rb+') as f:
			course_allocations = pickle.load(f)
	except:
		print 'Empty'
		course_allocations = []

	ch = int(raw_input('1 for add\n2 for del\n3 for upd\n'))
	if ch == 1:
		course_allocation = {} #each entry is a dict
		course_allocation['co_alloc_id'] = raw_input('Enter a unique id for this course allocation: ')
		course_allocation['type'] = raw_input('UG/PG : ')
		course_allocation['courseids'] = [x for x in raw_input('Enter Course Id(s) separated by space: ').split()]
		course_allocation['branch'] = raw_input('branch')
		course_allocation['sem'] = raw_input('sem')
		#apply constraints

		flag = 1
		for i in xrange(len(course_allocations)):
			if course_allocations[i]['type'] == course_allocation['type'] and course_allocations[i]['branch']== course_allocation['branch'] and course_allocations[i]['sem']== course_allocation['sem']:
				flag = 0 #course added to a nonexisting allocation
				course_allocations[i]['courseids'] = union_list(course_allocations[i]['courseids'] , course_allocation['courseids'])
				writeca2f(course_allocations)
				break


		if flag == 1: #course added to a nonexisting allocation
			course_allocations.append(course_allocation)
			#now check if some student is there having the same branch, year and sem
			try:
				with open('files/students.dat') as f:
					students = pickle.load(f)
			except:
				students = []

			try:
				with open('files/relations.dat', 'rb+') as f:
					relations  = pickle.load(f)
			except:
				relations = []

			for i in students:
				#print i['type'], i['branch'], i['sem']
				if i['type'] == course_allocation['type'] and i['branch']== course_allocation['branch'] and i['sem']== course_allocation['sem']:
					relation = {}
					relation['co_alloc_id'] = course_allocation['co_alloc_id']
					relation['rollno'] = i['rollno']
					relation['dor'] = datetime.datetime.now()
					if relation not in relations:
						relations.append(relation)
						print relations
						write_com(relations, 'files/relations.dat')

			writeca2f(course_allocations)
	print course_allocations

def writeca2f(course_allocations):
	with open('files/course_allocations.dat','wb') as f:
		pickle.dump(course_allocations,f)	