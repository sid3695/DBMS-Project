import pickle
from archives import *
from relations import *
from courses import *

students = []
def Students():
	try:
		with open('files/students.dat','rb+') as f:
			students = pickle.load(f)
	except:
		print 'hi'
		students = []

	ch = int(raw_input('1 for add\n2 for del\n3 for upd\n'))
	if ch == 1:
		student = {} #each st is a dict
		student['name'] = raw_input('Enter name : ')
		student['rollno'] = raw_input('Roll No : ')
		student['dob'] = raw_input('DOB : ')
		student['sex'] = raw_input('Sex : ')
		student['address'] = raw_input('Address : ')
		student['branch'] = raw_input('Branch : ')


		students.append(student)
		writes2f(students)	

	elif ch == 2:
		rno = raw_input("roll no to be deleted")
		for stu in xrange(len(students)):
			if(students[stu]['rollno']) == rno:
				del students[stu]
				#del allocations
				writes2f(students)
	elif ch == 3:
		rno = raw_input("roll no to be updated")
		for stu in xrange(len(students)):
			if(students[stu]['rollno']) == rno:
				students[stu]['name'] = raw_input('Enter name')
				#upd allocations
				writes2f(students)
	print students 	

def writes2f(students):
	with open('files/students.dat','wb') as f:
		pickle.dump(students,f)