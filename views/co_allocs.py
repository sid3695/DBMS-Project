from flask import render_template, url_for, request, redirect, Blueprint
import pickle
import datetime
from utils import *


papp = Blueprint('papp', __name__, template_folder='templates')

#co_all -----------------------------------------------------
@papp.route('/co_allocs')
def com():
 	return render_template('c_alloc_menu.html')

@papp.route('/sp_add', methods = ['GET', 'POST'])
def spa():
	if request.method == 'POST':
		#constraints
		x = str(request.form['co_alloc_id'])
		course_allocations = file_to_list('files/course_allocations.dat')

		found = 0
		for i in course_allocations:
			if i['co_alloc_id'] == x:
				found = 1
		if found == 1:
			return render_template('spa.html', flag = 6)

		x = str(request.form['branch'])
		if x not in ('COE','ME','ECE'):
			return render_template('spa.html', flag = 3)

		x = str(request.form['type'])
		if x not in ('UG', 'PG'):
			return render_template('spa.html', flag = 4)
		
		if x == 'UG':
			try:
				y = int(request.form['sem'])
			except:
				return render_template('spa.html', flag = 5)
			if(y>8):
				return render_template('spa.html', flag = 5)

		if x == 'PG':
			try:
				y = int(request.form['sem'])
			except:
				return render_template('spa.html', flag = 5)
			if(y>2):
				return render_template('spa.html', flag = 5)


		course_allocation = {} #each entry is a dict
		course_allocation['co_alloc_id'] = str(request.form['co_alloc_id'])
		course_allocation['type'] = str(request.form['type'])

		courses = file_to_list('files/courses.dat')

		course_allocation['courseids'] = (request.form['courseids']).split() #split when you need
		if len(course_allocation['courseids']) > 5:
			return render_template('spa.html', flag = 55)
		for i in course_allocation['courseids']:
			flag = 0
			for j in courses:
				if j['courseid'] == i:
					flag = 1
			if flag == 0:
				course_allocation['courseids'].remove(i)


		course_allocation['branch'] = str(request.form['branch'])
		course_allocation['sem'] = str(request.form['sem'])

		if course_allocation not in course_allocations:
			course_allocations.append(course_allocation)
		write_com(course_allocations,'files/course_allocations.dat')


		students = file_to_list('files/students.dat')
		relations = file_to_list('files/courses.dat')

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



		return render_template('spa.html', flag = 99)
	else:
 		return render_template('spa.html')

@papp.route('/sp_del', methods = ['GET', 'POST'])
def spd():
	if request.method == 'POST':
		#constraints
		x = str(request.form['co_alloc_id'])
		course_allocations = file_to_list('files/course_allocations.dat')
		relations = file_to_list('files/relations.dat')
		found = 0
		for stu in xrange(len(course_allocations)):
			if(course_allocations[stu]['co_alloc_id']) == x:
				del course_allocations[stu]
				found = 1
				for j in xrange(len(relations)):
					print len(relations)
					if relations[j]['co_alloc_id'] == x:
						del relations[j]
						print relations
						write_com(relations, 'files/relations.dat')
				write_com(course_allocations, 'files/course_allocations.dat')
				return render_template('spd.html', flag = 99)
		if found == 0:
			return render_template('spd.html', flag = 6)
	else:
		return render_template('spd.html')

@papp.route('/sp_upd', methods = ['GET', 'POST'])
def spu_menu():
	if request.method == 'POST':
		#constraints
		x = str(request.form['co_alloc_id'])
		course_allocations = file_to_list('files/course_allocations.dat')

		found = 0
		for stu in xrange(len(course_allocations)):
			if(course_allocations[stu]['co_alloc_id']) == x:
				found = 1
				return redirect(url_for('papp.spu_form', co_alloc_id = x))
		if found == 0:
			return render_template('sp_upd_menu.html', flag = 6)
	else:
		return render_template('sp_upd_menu.html')

@papp.route('/spu_form/<co_alloc_id>', methods = ['GET', 'POST'])
def spu_form(co_alloc_id):
	if request.method == 'POST':
		x = str(request.form['co_alloc_id'])
		course_allocations = file_to_list('files/course_allocations.dat')

		found = 0
		for i in course_allocations:
			if i['co_alloc_id'] == x and co_alloc_id != x:
				found = 1
		if found == 1:
			return render_template('sp_upd_menu.html', flag = 6)
		
		x = str(request.form['branch'])
		if x not in ('COE','ME','ECE'):
			return render_template('sp_upd_menu.html', flag = 3)

		x = str(request.form['type'])
		if x not in ('UG', 'PG'):
			return render_template('sp_upd_menu.html', flag = 4)
		
		if x == 'UG':
			try:
				y = int(request.form['sem'])
			except:
				return render_template('sp_upd_menu.html', flag = 5)
			if(y>8):
				return render_template('sp_upd_menu.html', flag = 5)

		if x == 'PG':
			try:
				y = int(request.form['sem'])
			except:
				return render_template('sp_upd_menu.html', flag = 5)
			if(y>2):
				return render_template('sp_upd_menu.html', flag = 5)

		

		course_allocation = {} #each entry is a dict
		course_allocation['co_alloc_id'] = str(request.form['co_alloc_id'])
		course_allocation['type'] = str(request.form['type'])
		course_allocation['courseids'] = (request.form['courseids'])
		course_allocation['branch'] = str(request.form['branch'])
		course_allocation['sem'] = str(request.form['sem'])

		courses = file_to_list('files/courses.dat')
		temp = []
		print course_allocation['courseids'] #= (request.form['courseids']).split() #split when you need
		for i in course_allocation['courseids']:
			flag = 0
			for j in courses:
				if str(j['courseid']) == str(i):
					flag = 1
			if flag == 1:
				temp.append(str(i))
		print temp


		students = file_to_list('files/students.dat')
		relations = file_to_list('files/relations.dat')

		flag_change = 0
		if(co_alloc_id != course_allocation['co_alloc_id']):#changed
			flag_change = 1
		
		course_allocations = file_to_list('files/course_allocations.dat')

		for stu in xrange(len(course_allocations)):
			if(course_allocations[stu]['co_alloc_id']) == co_alloc_id:
				course_allocations[stu] = course_allocation
		
		#if flag_change:
		#	for stu in xrange(len(students)):
		#		if(students[stu]['rollno']) == rollno:
		#			del students[stu]

		if flag_change: #remove previous relations
			for i in xrange(len(relations)):
				if relations[i]['co_alloc_id'] == co_alloc_id:
					del relations[i]

		for i in students:
			if i['type'] == course_allocation['type'] and i['branch']== course_allocation['branch'] and i['sem']== course_allocation['sem']:
				relation = {}
				relation['co_alloc_id'] = course_allocation['co_alloc_id']
				relation['rollno'] = i['rollno']
				relation['dor'] = datetime.datetime.now()
				if relation not in relations:
					relations.append(relation)
					print relations
					write_com(relations, 'files/relations.dat')

		
		write_com(course_allocations,'files/course_allocations.dat')
		return render_template('sp_upd_menu.html', flag = 99)

	else:
		course_allocations = file_to_list('files/course_allocations.dat')
		found = 0
		for stu in xrange(len(course_allocations)):
			if(course_allocations[stu]['co_alloc_id']) == co_alloc_id:
				found = 1
				course_allocation = course_allocations[stu]
				return render_template('spm.html', y = course_allocation)
		print found
		#return render_template('sm.html', y = rollno)

@papp.route('/sp_all')
def sp_all():
	course_allocations = file_to_list('files/course_allocations.dat')
	return render_template('sp_all.html', x = course_allocations)

#----------------------------------------------------------------------