from flask import Flask, render_template, request, redirect, url_for
import pickle
import datetime
app = Flask(__name__)


def write_com(param1, fname):
	with open(fname,'wb') as f:
		pickle.dump(param1,f)

@app.route('/')
def index():
    return render_template('index.html')
#students --------------------------------------------------
@app.route('/students')
def sm():
 	return render_template('students_menu.html')


@app.route('/s_add', methods = ['GET', 'POST'])
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
		try:
			with open('files/students.dat','rb+') as f:
				students = pickle.load(f)
		except:
			print 'hi'
			students = []
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

		try:
			with open('files/course_allocations.dat', 'rb+') as f:
				existing = pickle.load(f)
		except:
			existing = []

		try:
			with open('files/relations.dat', 'rb+') as f:
				relations  = pickle.load(f)
		except:
			relations = []

		for i in existing:
			if i['type'] == student['type'] and i['branch']== student['branch'] and i['sem']== student['sem']:
				relation = {}
				relation['co_alloc_id'] = i['co_alloc_id']
				relation['rollno'] = student['rollno']
				relation['dor'] = datetime.datetime.now()
				if relation not in relations:
					relations.append(relation)
					print relations
					write_com(relations, 'files/relations.dat')

		if student not in students:
			students.append(student)
		write_com(students,'files/students.dat')
		return render_template('sa.html', flag = 99)
	else:
 		return render_template('sa.html')

@app.route('/s_del', methods = ['GET', 'POST'])
def sd():
	if request.method == 'POST':
		#constraints
		x = str(request.form['rollno'])
		try:
			with open('files/students.dat','rb+') as f:
				students = pickle.load(f)
		except:
			print 'hi'
			students = []

		try:
			with open('files/relations.dat', 'rb+') as f:
				relations  = pickle.load(f)
		except:
			relations = []
		print relations
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


@app.route('/s_upd', methods = ['GET', 'POST'])
def su_menu():
	if request.method == 'POST':
		#constraints
		x = str(request.form['rollno'])
		try:
			with open('files/students.dat','rb+') as f:
				students = pickle.load(f)
		except:
			print 'hi'
			students = []

		found = 0
		for stu in xrange(len(students)):
			if(students[stu]['rollno']) == x:
				found = 1
				return redirect(url_for('su_form', rollno = x))
		if found == 0:
			return render_template('s_upd_menu.html', flag = 6)
	else:
		return render_template('s_upd_menu.html')

@app.route('/su_form/<rollno>', methods = ['GET', 'POST'])
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

		try:
			with open('files/course_allocations.dat', 'rb+') as f:
				existing = pickle.load(f)
		except:
			existing = []

		try:
			with open('files/relations.dat', 'rb+') as f:
				relations  = pickle.load(f)
		except:
			relations = []
		flag_change = 0
		if(rollno != student['rollno']):#changed
			flag_change = 1
		
		try:
			with open('files/students.dat','rb+') as f:
				students = pickle.load(f)
		except:
			print 'hi'
			students = []

		for stu in xrange(len(students)):
			if(students[stu]['rollno']) == rollno:
				students[stu] = student
		
		#if flag_change:
		#	for stu in xrange(len(students)):
		#		if(students[stu]['rollno']) == rollno:
		#			del students[stu]

		if flag_change: #remove previous relations
			for i in xrange(len(relations)):
				if relations[i]['rollno'] == rollno:
					del relations[i]

		for i in existing:
			if i['type'] == student['type'] and i['branch']== student['branch'] and i['sem']== student['sem']:
				relation = {}
				relation['co_alloc_id'] = i['co_alloc_id']
				relation['rollno'] = student['rollno']
				relation['dor'] = datetime.datetime.now()
				if relation not in relations:
					relations.append(relation)
					print relations
					write_com(relations, 'files/relations.dat')

		
		write_com(students,'files/students.dat')
		return render_template('s_upd_menu.html', flag = 99)

	else:
		try:
			with open('files/students.dat','rb+') as f:
				students = pickle.load(f)
		except:
			print 'hi'
			students = []
		found = 0
		for stu in xrange(len(students)):
			if(students[stu]['rollno']) == rollno:
				found = 1
				student = students[stu]
				return render_template('sm.html', y = student)
		#return render_template('sm.html', y = rollno)

@app.route('/s_all', methods = ['GET', 'POST'])
def su_all():
	try:
		with open('files/students.dat','rb+') as f:
			students = pickle.load(f)
	except:
		print 'hi'
		students = []
	return render_template('su_all.html', x = students)
#-----------------------------------------------------------
#courses----------------------------------------------------
@app.route('/courses')
def cm():
 	return render_template('courses_menu.html')

@app.route('/c_add', methods = ['GET', 'POST'])
def ca():
	if request.method == 'POST':
		#constraints
		x = str(request.form['courseid'])
		try:
			with open('files/courses.dat','rb+') as f:
				courses = pickle.load(f)
		except:
			print 'hi'
			courses = []

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

@app.route('/c_del', methods = ['GET', 'POST'])
def cd():
	if request.method == 'POST':
		#constraints
		x = str(request.form['courseid'])
		try:
			with open('files/courses.dat','rb+') as f:
				courses = pickle.load(f)
		except:
			print 'hi'
			courses = []

		try:
			with open('files/course_allocations.dat', 'rb+') as f:
				course_allocations = pickle.load(f)
		except:
			course_allocations = []

		found = 0
		for i in xrange(len(courses)):
			if(courses[i]['courseid']) == x:
				del courses[i]
				found = 1
				for j in xrange(len(course_allocations)): #list
					if x in course_allocations[j]['courseids']:
						course_allocations[j]['courseids'].remove(x) #needs testing
						write_com(course_allocations, 'files/course_allocations.dat')
				write_com(courses, 'files/courses.dat')
				return render_template('cd.html', flag = 99)
		if found == 0:
			return render_template('cd.html', flag = 6)
	else:
		return render_template('cd.html')

@app.route('/c_upd', methods = ['GET', 'POST'])
def cu_menu():
	if request.method == 'POST':
		#constraints
		x = str(request.form['courseid'])
		try:
			with open('files/courses.dat','rb+') as f:
				courses = pickle.load(f)
		except:
			print 'hi'
			courses = []

		found = 0
		for stu in xrange(len(courses)):
			if(courses[stu]['courseid']) == x:
				found = 1
				return redirect(url_for('cu_form', courseid = x))
		if found == 0:
			return render_template('c_upd_menu.html', flag = 6)
	else:
		return render_template('c_upd_menu.html')

@app.route('/cu_form/<courseid>', methods = ['GET', 'POST'])
def cu_form(courseid):
	if request.method == 'POST':
		#constraints
		course = {} #each st is a dict
		course['name'] = str(request.form['name'])
		course['courseid'] = str(request.form['courseid'])
		course['credits'] = str(request.form['credits'])
		
		try:
			with open('files/course_allocations.dat', 'rb+') as f:
				existing = pickle.load(f)
		except:
			existing = []

		flag_change = 0
		if(courseid!= course['courseid']):#changed
			flag_change = 1
		
		try:
			with open('files/courses.dat','rb+') as f:
				courses = pickle.load(f)
		except:
			print 'hi'
			courses = []

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
		try:
			with open('files/courses.dat','rb+') as f:
				courses = pickle.load(f)
		except:
			print 'hi'
			courses = []
		found = 0
		for stu in xrange(len(courses)):
			if(courses[stu]['courseid']) == courseid:
				found = 1
				course = courses[stu]
				return render_template('cm.html', y = course)
		#return render_template('sm.html', y = rollno)


@app.route('/c_all', methods = ['GET', 'POST'])
def c_all():
	try:
		with open('files/courses.dat','rb+') as f:
			courses = pickle.load(f)
	except:
		print 'hi'
		courses = []
	return render_template('c_all.html', x = courses)
#------------------------------------------------------------
#co_all -----------------------------------------------------
@app.route('/co_allocs')
def com():
 	return render_template('c_alloc_menu.html')

@app.route('/sp_add', methods = ['GET', 'POST'])
def spa():
	if request.method == 'POST':
		#constraints
		x = str(request.form['co_alloc_id'])
		try:
			with open('files/course_allocations.dat','rb+') as f:
				course_allocations = pickle.load(f)
		except:
			print 'hi'
			course_allocations = []

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

		try:
			with open('files/courses.dat','rb+') as f:
				courses = pickle.load(f)
		except:
			print 'hi'
			courses = []

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



		return render_template('spa.html', flag = 99)
	else:
 		return render_template('spa.html')

@app.route('/sp_del', methods = ['GET', 'POST'])
def spd():
	if request.method == 'POST':
		#constraints
		x = str(request.form['co_alloc_id'])
		try:
			with open('files/course_allocations.dat','rb+') as f:
				course_allocations = pickle.load(f)
		except:
			print 'hi'
			course_allocations = []

		try:
			with open('files/relations.dat', 'rb+') as f:
				relations  = pickle.load(f)
		except:
			relations = []
		print relations
		found = 0
		for stu in xrange(len(course_allocations)):
			if(course_allocations[stu]['co_alloc_id']) == x:
				del course_allocations[stu]
				found = 1
				for j in xrange(len(relations)):
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

@app.route('/sp_upd', methods = ['GET', 'POST'])
def spu_menu():
	if request.method == 'POST':
		#constraints
		x = str(request.form['co_alloc_id'])
		try:
			with open('files/course_allocations.dat','rb+') as f:
				course_allocations = pickle.load(f)
		except:
			print 'hi'
			course_allocations = []

		found = 0
		for stu in xrange(len(course_allocations)):
			if(course_allocations[stu]['co_alloc_id']) == x:
				found = 1
				return redirect(url_for('spu_form', co_alloc_id = x))
		if found == 0:
			return render_template('sp_upd_menu.html', flag = 6)
	else:
		return render_template('sp_upd_menu.html')

@app.route('/spu_form/<co_alloc_id>', methods = ['GET', 'POST'])
def spu_form(co_alloc_id):
	if request.method == 'POST':
		x = str(request.form['co_alloc_id'])
		try:
			with open('files/course_allocations.dat','rb+') as f:
				course_allocations = pickle.load(f)
		except:
			print 'hi'
			course_allocations = []

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

		try:
			with open('files/courses.dat','rb+') as f:
				courses = pickle.load(f)
		except:
			print 'hi'
			courses = []
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

		flag_change = 0
		if(co_alloc_id != course_allocation['co_alloc_id']):#changed
			flag_change = 1
		
		try:
			with open('files/course_allocations.dat','rb+') as f:
				course_allocations = pickle.load(f)
		except:
			print 'hi'
			course_allocations = []

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
		try:
			with open('files/course_allocations.dat','rb+') as f:
				course_allocations = pickle.load(f)
		except:
			print 'hi'
			course_allocations = []
		found = 0
		for stu in xrange(len(course_allocations)):
			if(course_allocations[stu]['co_alloc_id']) == co_alloc_id:
				found = 1
				course_allocation = course_allocations[stu]
				return render_template('spm.html', y = course_allocation)
		print found
		#return render_template('sm.html', y = rollno)

@app.route('/sp_all')
def sp_all():
	try:
		with open('files/course_allocations.dat','rb+') as f:
			course_allocations = pickle.load(f)
	except:
		print 'hi'
		course_allocations = []
	print course_allocations
	return render_template('sp_all.html', x = course_allocations)

#----------------------------------------------------------------------
#relations--------------------------------------------------------------
@app.route('/relations')
def rel():
 	return render_template('relations.html')

@app.route('/r_exp')
def rel_exp():
	try:
		with open('files/relations.dat', 'rb+') as f:
			relations = pickle.load(f)
	except:
		print 'Empty'
		relations = []

	try:
		with open('files/archived.dat', 'rb+') as f:
			archived = pickle.load(f)
	except:
		print 'Empty'
		archived = []
		
	for i in xrange(len(relations)):
		#relations[i]['dor'] + datetime.timedelta(days=180)
		if(relations[i]['dor'] + datetime.timedelta(days=180) < datetime.datetime.now()):
			archived.append(relations[i])
			del relations[i]	
			write_com(archived,'files/archived.dat')
			write_com(relations,'files/relations.dat')
 	try:
		with open('files/archived.dat','rb+') as f:
			archived = pickle.load(f)
	except:
		print 'hi'
		archived = []
	#print relations
	return render_template('archives.html', x = archived)

@app.route('/r_add', methods = ['GET', 'POST'])
def r_add():
	if request.method == 'POST':
		#constraints
		x = str(request.form['co_alloc_id'])
		try:
			with open('files/course_allocations.dat','rb+') as f:
				course_allocations = pickle.load(f)
		except:
			print 'hi'
			course_allocations = []

		found = 0
		for i in course_allocations:
			if i['co_alloc_id'] == x:
				found = 1
		if found == 0:
			return render_template('ra.html', flag = 6)

		x = str(request.form['rollno'])
		try:
			with open('files/students.dat','rb+') as f:
				students = pickle.load(f)
		except:
			print 'hi'
			students = []

		found = 0
		for i in students:
			if i['rollno'] == x:
				found = 1
		if found == 0:
			return render_template('ra.html', flag = 5)



		relation = {} #each st is a dict
		relation['co_alloc_id'] = request.form['co_alloc_id']
		relation['rollno'] = request.form['rollno']
		relation['dor'] = (datetime.datetime.now())

		try:
			with open('files/relations.dat','rb+') as f:
				relations = pickle.load(f)
		except:
			print 'hi'
			relations = []

		found = 0
		for i in relations:
			if i['rollno'] == str(request.form['rollno']):
				found = 1
		if found == 1:
			return render_template('ra.html', flag = 3)
		
		if relation not in relations:
			relations.append(relation)
		write_com(relations,'files/relations.dat')
		return render_template('ra.html', flag = 99)
	else:
 		return render_template('ra.html')

@app.route('/r_del', methods = ['GET', 'POST'])
def rd():
	if request.method == 'POST':
		#constraints
		try:
			with open('files/relations.dat', 'rb+') as f:
				relations  = pickle.load(f)
		except:
			relations = []
		print relations

		found = 0
		for stu in xrange(len(relations)):
			if(relations[stu]['rollno']) == str(request.form['rollno']):
				del relations[stu]
				found = 1
				print relations
				write_com(relations, 'files/relations.dat')
				#write_com(course_allocations, 'files/course_allocations.dat')
				return render_template('spd.html', flag = 99)
		if found == 0:
			return render_template('spd.html', flag = 6)
	else:
		return render_template('spd.html')

@app.route('/r_all')
def rel_all():
	try:
		with open('files/relations.dat','rb+') as f:
			relations = pickle.load(f)
	except:
		print 'hi'
		relations = []
	print relations
	return render_template('r_all.html', x = relations)

if __name__ == '__main__':
    app.run(debug=True)