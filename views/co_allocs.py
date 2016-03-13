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
			try:
				if i['co_alloc_id'] == x:
					found = 1
			except:
				pass
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
		lis = []
		for i in (request.form['courseids']).split():
			lis.append(i)
		print lis

		if len(lis) > 5:
			return render_template('spa.html', flag = 55)
		lis2 = []
		for i in lis:
			print i
			flag = 0
			for j in courses:
				print j['courseid']
				print i
				if j['courseid'] == i:
					flag = 1
			if flag == 1:
				lis2.append(i)
		print lis2
		course_allocation['courseids'] = lis2
		course_allocation['branch'] = str(request.form['branch'])
		course_allocation['sem'] = str(request.form['sem'])

		if course_allocation not in course_allocations:
			course_allocations.append(course_allocation)
		write_com(course_allocations,'files/course_allocations.dat')


		students = file_to_list('files/students.dat')
		relations = file_to_list('files/relations.dat')

		for i in students:
			#print i['type'], i['branch'], i['sem']
			if i['type'] == course_allocation['type'] and i['branch']== course_allocation['branch'] and i['sem']== course_allocation['sem']:
				relation = {}
				relation['co_alloc_id'] = course_allocation['co_alloc_id']
				relation['rollno'] = i['rollno']
				relation['dor'] = datetime.datetime.now()
				flag = 0
				for r in relations:
					if r['co_alloc_id'] == relation['co_alloc_id'] and r['rollno'] == relation['rollno']:
						flag = 1
				if flag == 0: #wrong, cause of dor, check only for first two ###############!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
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
		cor = relations
		found = 0
		for stu in xrange(len(course_allocations)):
			try:
				if(course_allocations[stu]['co_alloc_id']) == x:
					del course_allocations[stu]
					found = 1
			except:
				pass
		print relations
		temp = []
		for j in relations:
			if j['co_alloc_id'] != x:
				temp.append(j)

		

		relations = temp
		write_com(relations, 'files/relations.dat')
		write_com(course_allocations, 'files/course_allocations.dat')
		if found == 1:
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
			try:
				if(course_allocations[stu]['co_alloc_id']) == x:
					found = 1
					return redirect(url_for('papp.spu_form', co_alloc_id = x))
			except:
				pass
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
			print 'i',i
			#if i['co_alloc_id'] == x and co_alloc_id != x:
				#found = 1
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
		phi = (request.form['courseids']).split()
		course_allocation['branch'] = str(request.form['branch'])
		course_allocation['sem'] = str(request.form['sem'])

		courses = file_to_list('files/courses.dat')
		temp = []
		#print course_allocation['courseids'] #= (request.form['courseids']).split() #split when you need
		for i in phi:
			flag = 0
			for j in courses:
				if str(j['courseid']) == str(i):
					flag = 1
			if flag == 1:
				temp.append(str(i))
		print temp
		course_allocation['courseids'] = temp

		students = file_to_list('files/students.dat')
		relations = file_to_list('files/relations.dat')

		flag_change = 0
		if(co_alloc_id != course_allocation['co_alloc_id']):#changed
			flag_change = 1
		
		course_allocations = file_to_list('files/course_allocations.dat')

		for stu in xrange(len(course_allocations)):
			try:
				if(course_allocations[stu]['co_alloc_id']) == co_alloc_id:
					course_allocations[stu] = course_allocation
			except:
				pass
		
		#if flag_change:
		#	for stu in xrange(len(students)):
		#		if(students[stu]['rollno']) == rollno:
		#			del students[stu]

		if flag_change: #remove previous relations
			for i in xrange(len(relations)):
				try:
					if relations[i]['co_alloc_id'] == co_alloc_id:
						del relations[i]
				except:
					pass

		for i in students:
			if i['type'] == course_allocation['type'] and i['branch']== course_allocation['branch'] and i['sem']== course_allocation['sem']:
				relation = {}
				relation['co_alloc_id'] = course_allocation['co_alloc_id']
				relation['rollno'] = i['rollno']
				relation['dor'] = datetime.datetime.now()
				flag = 0
				for r in relations:
					if r['co_alloc_id'] == relation['co_alloc_id'] and r['rollno'] == relation['rollno']:
						flag = 1
				if flag == 0: #wrong, cause of dor, check only for first two ###############!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
					relations.append(relation)
					print relations
					write_com(relations, 'files/relations.dat')

		
		write_com(course_allocations,'files/course_allocations.dat')
		return render_template('sp_upd_menu.html', flag = 99)

	else:
		course_allocations = file_to_list('files/course_allocations.dat')
		found = 0
		for stu in xrange(len(course_allocations)):
			try:
				if(course_allocations[stu]['co_alloc_id']) == co_alloc_id:
					found = 1
					course_allocation = course_allocations[stu]
					phi = ''
					for i in course_allocation['courseids']:
						print i
						phi = phi + str(i) + ' '
					print phi
					course_allocation['courseids'] = phi
					return render_template('spm.html', y = course_allocation)
			except:
				pass
		print found
		#return render_template('sm.html', y = rollno)

@papp.route('/sp_all')
def sp_all():
	course_allocations = file_to_list('files/course_allocations.dat')
	return render_template('sp_all.html', x = course_allocations)

#----------------------------------------------------------------------