from flask import render_template, url_for, request, redirect, Blueprint
import pickle
import datetime
from utils import *


rapp = Blueprint('rapp', __name__, template_folder='templates')

#relations--------------------------------------------------------------
@rapp.route('/relations')
def rel():
 	return render_template('relations.html')

@rapp.route('/r_exp')
def rel_exp():
	relations = file_to_list('files/relations.dat')
	archived = file_to_list('files/archived.dat')
		
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

@rapp.route('/r_add', methods = ['GET', 'POST'])
def r_add():
	if request.method == 'POST':
		#constraints
		x = str(request.form['co_alloc_id'])
		course_allocations = file_to_list('files/course_allocations.dat')

		found = 0
		for i in course_allocations:
			if i['co_alloc_id'] == x:
				found = 1
		if found == 0:
			return render_template('ra.html', flag = 6)

		x = str(request.form['rollno'])
		students = file_to_list('files/students.dat')

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

		relations = file_to_list('files/relations.dat')

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

@rapp.route('/r_del', methods = ['GET', 'POST'])
def rd():
	if request.method == 'POST':
		#constraints
		relations = file_to_list('files/relations.dat')

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

@rapp.route('/r_all')
def rel_all():
	relations = file_to_list('files/relations.dat')
	return render_template('r_all.html', x = relations)