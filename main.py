import pickle
from students import *
from archives import *
from relations import *
from course_allocations import *
from courses import *


#student
#sem 
#courses
#teachers


#sem -> courses [courseid], sem-no, 
#courses -> id, name, credits,


def main():
	while 1 :
		print 'hi'

		ch = raw_input('choice 1 for st, 2 for cou, 3 for re, 4 for co_a \n')
		if ch == '1':
			Students()
		elif ch == '2':
			Courses()
		elif ch == '3':
			Relations()
		elif ch == '4':
			Course_Allocations()


main()