import pickle
from students import *
from sems import *
from teachers import *
from courses import *

def student():
	try:
		with open('files/students.dat','rb+') as f:
			students = pickle.load(f)
	except:
		print 'hi'
		students = []

	'''ch = int(raw_input())
	if ch == 1:
		student = {} #each st is a dict
		student['name'] = raw_input()
		students.append(student)
		write2f(students)	
	#if ch == 2:'''
	print students 	

def write2f(students):
	with open('files/students.dat','wb') as f:
		pickle.dump(students,f)