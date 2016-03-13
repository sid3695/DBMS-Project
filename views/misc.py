from flask import render_template, url_for, request, redirect, Blueprint
import pickle
import datetime
from datetime import date
from utils import *

import os, sys

mapp = Blueprint('mapp', __name__, template_folder='templates')

@mapp.route('/misc')
def misc():
 	return render_template('misc.html')

@mapp.route('/del_all')
def del_all():
	try:
		os.remove('files/relations.dat')
	except:
		pass
	try:
		os.remove('files/students.dat')
	except:
		pass
	try:
		os.remove('files/course_allocations.dat')
	except:
		pass
	try:
		os.remove('files/courses.dat')
	except:
		pass

 	return render_template('index.html')

@mapp.route('/fine', methods = ['GET', 'POST'])
def fine():
	if request.method == 'POST':
		x = str(request.form['date'])
		y = x.replace('-',' ').split()
		d0 = date(int(y[2]), int(y[1]), int(y[0]))
		print d0
		students = file_to_list('files/students.dat')
		data = {}
		for i in students:
			d1 = i['regdate']
			if ((d1-d0).days*50 > 0):
				data[ i['rollno'] ] = (d1-d0).days*50
		print data
		return render_template('fine_tab.html', data = data)
	else:
		return render_template('fine.html')