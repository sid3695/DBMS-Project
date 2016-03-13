from flask import render_template, url_for, request, redirect, Blueprint
import pickle
import datetime
from utils import *


sapp = Blueprint('sapp', __name__, template_folder='templates')


#students --------------------------------------------------
@sapp.route('/students')
def sm():
	print 'lll'
 	return render_template('students_menu.html')


@sapp.route('/s_add', methods = ['GET', 'POST'])
def sa():
	if request.method == 'POST':
		#constraints
		print str(request.form['sex'])!='M'
		x = str(request.form['sex'])
		print x
		if x!="M":
			if x!= 'F':
				return render_template('sa.html', flag = 1)
		x = str(request.form['phone'])
		if len(x) != 10:
			return render_template('sa.html', flag = 2)

		x = str(request.form['branch'])
		if x not in ('COE','ME','ECE'):
			return render_template('sa.html', flag = 3)

		x = str(request.form['type'])
		if x not in ('UG', 'PG'):
			return render_template('sa.html', flag = 4)
		
		if x == 'UG':
			try:
				y = int(request.form['sem'])
			except:
				return render_template('sa.html', flag = 5)
			if(y>8):
				return render_template('sa.html', flag = 5)

		if x == 'PG':
			try:
				y = int(request.form['sem'])
			except:
				return render_template('sa.html', flag = 5)
			if(y>2):
				return render_template('sa.html', flag = 5)

		x = str(request.form['rollno'])
		students = file_to_list('files/students.dat')
		print students
		found = 0
		for i in students:
			if i['rollno'] == x and i['type'] == str(request.form['type']):
				found = 1
		if found == 1:
			return render_template('sa.html', flag = 6)

		student = {} #each st is a dict
		student['name'] = str(request.form['name'])
		student['rollno'] = str(request.form['rollno'])
		student['dob'] = str(request.form['dob'])
		student['sex'] = str(request.form['sex'])
		student['address'] = str(request.form['address'])
		student['branch'] = str(request.form['branch'])
		student['type'] = str(request.form['type'])
		student['sem'] = str(request.form['sem'])
		student['phone'] = str(request.form['phone'])
		student['regdate'] = datetime.date.today()
		existing = file_to_list('files/course_allocations.dat')
		relations = file_to_list('files/relations.dat') 
		
		for i in existing:
			try:
				if i['type'] == student['type'] and i['branch']== student['branch'] and i['sem']== student['sem']:
					relation = {}
					relation['co_alloc_id'] = i['co_alloc_id']
					relation['rollno'] = student['rollno']
					relation['dor'] = datetime.datetime.now()
					if relation not in relations:
						relations.append(relation)
						print relations
						write_com(relations, 'files/relations.dat')
			except:
				pass

		if student not in students:
			students.append(student)
		write_com(students,'files/students.dat')
		return render_template('sa.html', flag = 99)
	else:
 		return render_template('sa.html')

@sapp.route('/s_del', methods = ['GET', 'POST'])
def sd():
	if request.method == 'POST':
		#constraints
		x = str(request.form['rollno'])
		students = file_to_list('files/students.dat')
		relations = file_to_list('files/relations.dat') 
		
		found = 0
		for stu in xrange(len(students)):
			if(students[stu]['rollno']) == x:
				del students[stu]
				found = 1
				for j in xrange(len(relations)):
					if relations[j]['rollno'] == x:
						del relations[j]
						print relations
						write_com(relations, 'files/relations.dat')
				write_com(students, 'files/students.dat')
				return render_template('sd.html', flag = 99)
		if found == 0:
			return render_template('sd.html', flag = 6)
	else:
		return render_template('sd.html')


@sapp.route('/s_upd', methods = ['GET', 'POST'])
def su_menu():
	if request.method == 'POST':
		#constraints
		x = str(request.form['rollno'])
		students = file_to_list('files/students.dat')

		found = 0
		for stu in xrange(len(students)):
			if(students[stu]['rollno']) == x:
				found = 1
				return redirect(url_for('sapp.su_form', rollno = x))
		if found == 0:
			return render_template('s_upd_menu.html', flag = 6)
	else:
		return render_template('s_upd_menu.html')

@sapp.route('/su_form/<rollno>', methods = ['GET', 'POST'])
def su_form(rollno):
	if request.method == 'POST':
		#constraints
		print str(request.form['sex'])!='M'
		x = str(request.form['sex'])
		print x
		if x!="M":
			if x!= 'F':
				return render_template('s_upd_menu.html', flag = 1)
		x = str(request.form['phone'])
		if len(x) != 10:
			return render_template('s_upd_menu.html', flag = 2)

		x = str(request.form['branch'])
		if x not in ('COE','ME','ECE'):
			return render_template('s_upd_menu.html', flag = 3)

		x = str(request.form['type'])
		if x not in ('UG', 'PG'):
			return render_template('s_upd_menu.html', flag = 4)
		
		if x == 'UG':
			try:
				y = int(request.form['sem'])
			except:
				return render_template('s_upd_menu.html', flag = 5)
			if(y>8):
				return render_template('s_upd_menu.html', flag = 5)

		if x == 'PG':
			try:
				y = int(request.form['sem'])
			except:
				return render_template('s_upd_menu.html', flag = 5)
			if(y>2):
				return render_template('s_upd_menu.html', flag = 5)

		

		student = {} #each st is a dict
		student['name'] = str(request.form['name'])
		student['rollno'] = str(request.form['rollno'])
		student['dob'] = str(request.form['dob'])
		student['sex'] = str(request.form['sex'])
		student['address'] = str(request.form['address'])
		student['branch'] = str(request.form['branch'])
		student['type'] = str(request.form['type'])
		student['sem'] = str(request.form['sem'])
		student['phone'] = str(request.form['phone'])
		student['regdate'] = datetime.date.today()
		existing = file_to_list('files/course_allocations.dat')
		relations = file_to_list('files/relations.dat')
		flag_change = 0
		if(rollno != student['rollno']):#changed
			flag_change = 1
		
		students = file_to_list('files/students.dat')

		for stu in xrange(len(students)):
			if(students[stu]['rollno']) == rollno:
				students[stu] = student
		
		#if flag_change:
		#	for stu in xrange(len(students)):
		#		if(students[stu]['rollno']) == rollno:
		#			del students[stu]
		temp_dt = datetime.datetime.now()
		if flag_change: #remove previous relations
			temp = []
			for i in xrange(len(relations)):
				if relations[i]['rollno'] != rollno:
					temp.append(relations[i])
				if relations[i]['rollno'] == rollno:
					temp_dt = relations[i]['dor']
			relations = temp

		try:
			for i in existing:
				if i['type'] == student['type'] and i['branch']== student['branch'] and i['sem']== student['sem']:
					relation = {}
					relation['co_alloc_id'] = i['co_alloc_id']
					relation['rollno'] = student['rollno']
					relation['dor'] = temp_dt
					if relation not in relations:
						relations.append(relation)
						print relations
						write_com(relations, 'files/relations.dat')
		except:
			pass
		
		write_com(students,'files/students.dat')
		return render_template('s_upd_menu.html', flag = 99)

	else:
		students = file_to_list('files/students.dat')
		found = 0
		for stu in xrange(len(students)):
			if(students[stu]['rollno']) == rollno:
				found = 1
				student = students[stu]
				return render_template('sm.html', y = student)
		#return render_template('sm.html', y = rollno)

@sapp.route('/s_all', methods = ['GET', 'POST'])
def su_all():
	students = file_to_list('files/students.dat')
	return render_template('su_all.html', x = students)
#-----------------------------------------------------------
