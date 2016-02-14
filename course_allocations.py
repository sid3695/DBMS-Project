import pickle
from students import *
from archives import *
from courses import *
from relations import *

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
		course_allocation['type'] = raw_input('UG/PG : ')
		course_allocation['courseids'] = [int(x) for x in raw_input('Enter Course Id(s) separated by space: ').split()]
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
			writeca2f(course_allocations)
	print course_allocations

def writeca2f(course_allocations):
	with open('files/course_allocations.dat','wb') as f:
		pickle.dump(course_allocations,f)	