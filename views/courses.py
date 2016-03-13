from flask import render_template, url_for, request, redirect, Blueprint
import pickle
import datetime
from utils import *


capp = Blueprint('capp', __name__, template_folder='templates')


#courses----------------------------------------------------
@capp.route('/courses')
def cm():
 	return render_template('courses_menu.html')

@capp.route('/c_add', methods = ['GET', 'POST'])
def ca():
	if request.method == 'POST':
		#constraints
		x = str(request.form['courseid'])
		courses = file_to_list('files/courses.dat')

		found = 0
		for i in courses:
			if i['courseid'] == x:
				found = 1
		if found == 1:
			return render_template('ca.html', flag = 6)

		try:
			x = int(request.form['credits'])
			if(x<1 or x>4):
				return render_template('ca.html', flag = 1)
		except:
			return render_template('ca.html', flag = 1)

		course = {} #each st is a dict
		course['name'] = request.form['name']
		course['courseid'] = request.form['courseid']
		course['credits'] = request.form['credits']

		if course not in courses:
			courses.append(course)
		write_com(courses,'files/courses.dat')
		return render_template('ca.html', flag = 99)
	else:
 		return render_template('ca.html')

@capp.route('/c_del', methods = ['GET', 'POST'])
def cd():
	if request.method == 'POST':
		#constraints
		x = str(request.form['courseid'])
		courses = file_to_list('files/courses.dat')
		course_allocations = file_to_list('files/course_allocations.dat')

		found = 0
		for i in xrange(len(courses)):
			if(courses[i]['courseid']) == x:
				del courses[i]
				found = 1
		for j in xrange(len(course_allocations)): #list
			#print j
			#print course_allocations[j]['courseids']
			try:
				if x in course_allocations[j]['courseids']:
					course_allocations[j]['courseids'].remove(x) #needs testing
			except:
				pass
		write_com(course_allocations, 'files/course_allocations.dat')
		write_com(courses, 'files/courses.dat')
		if found == 1:
			return render_template('cd.html', flag = 99)
		if found == 0:
			return render_template('cd.html', flag = 6)
	else:
		return render_template('cd.html')

@capp.route('/c_upd', methods = ['GET', 'POST'])
def cu_menu():
	if request.method == 'POST':
		#constraints
		x = str(request.form['courseid'])
		courses = file_to_list('files/courses.dat')

		found = 0
		for stu in xrange(len(courses)):
			if(courses[stu]['courseid']) == x:
				found = 1
				return redirect(url_for('capp.cu_form', courseid = x))
		if found == 0:
			return render_template('c_upd_menu.html', flag = 6)
	else:
		return render_template('c_upd_menu.html')

@capp.route('/cu_form/<courseid>', methods = ['GET', 'POST'])
def cu_form(courseid):
	if request.method == 'POST':
		#constraints
		course = {} #each st is a dict
		course['name'] = str(request.form['name'])
		course['courseid'] = str(request.form['courseid'])
		course['credits'] = str(request.form['credits'])
		
		existing = file_to_list('files/course_allocations.dat')

		flag_change = 0
		if(courseid!= course['courseid']):#changed
			flag_change = 1
		
		courses = file_to_list('files/courses.dat')

		for stu in xrange(len(courses)):
			if(courses[stu]['courseid']) == courseid:
				courses[stu] = course
		
		#if flag_change:
		#	for stu in xrange(len(students)):
		#		if(students[stu]['rollno']) == rollno:
		#			del students[stu]
		print existing
		if flag_change: #remove previous relations
			for i in xrange(len(existing)):
				if courseid in existing[i]['courseids']:
					existing[i]['courseids'].remove(courseid)
					existing.append(course) #testing
					write_com(existing, 'files/course_allocations.dat')
		print existing
		
		write_com(courses,'files/courses.dat')
		return render_template('c_upd_menu.html', flag = 99)

	else:
		courses = file_to_list('files/courses.dat')
		found = 0
		for stu in xrange(len(courses)):
			if(courses[stu]['courseid']) == courseid:
				found = 1
				course = courses[stu]
				return render_template('cm.html', y = course)
		#return render_template('sm.html', y = rollno)


@capp.route('/c_all', methods = ['GET', 'POST'])
def c_all():
	courses = file_to_list('files/courses.dat')
	return render_template('c_all.html', x = courses)
#------------------------------------------------------------