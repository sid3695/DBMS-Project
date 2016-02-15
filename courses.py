import pickle
from students import *
from archives import *
from relations import *
from course_allocations import *
from utils import write_com

courses = []

def Courses():
	try:
		with open('files/courses.dat', 'rb+') as f:
			courses = pickle.load(f)
	except:
		print 'Empty'
		courses = []

	ch = int(raw_input('1 for add\n2 for del\n3 for upd\n'))
	if ch == 1:
		course = {} #each course is a dict
		course['name'] = raw_input('Enter name : ')
		course['courseid'] = raw_input('Course id : ')
		#course['sem'] = raw_input('sem : ')
		#course['type'] = raw_input('UG/PG : ')
		#course['branch'] = raw_input('Branch : ')
		course['credits'] = raw_input('Credits : ')
		#apply contra
		if course not in courses:
			courses.append(course)
		writec2f(courses)	

	elif ch == 2:
		cid = raw_input("course id to be deleted")
		for i in xrange(len(courses)):
			if(courses[i]['courseid']) == cid:
				del courses[i]
				#del allocations
				writec2f(courses)

	elif ch == 3:
		cid = raw_input("course id to be updated")
		for i in xrange(len(courses)):
			if(courses[i]['courseid']) == cid:
				courses[i]['name'] = raw_input('Enter name')
				#upd allocations
				writec2f(courses)
	print courses 


def writec2f(courses):
	with open('files/courses.dat','wb') as f:
		pickle.dump(courses,f)	
