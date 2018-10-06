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

PER_DAY_FINE = 50

@mapp.route('/fine', methods = ['GET', 'POST'])
def fine():
	if request.method == 'POST':
		inputStrDate = str(request.form['date'])
		splittedDate = map(int, inputStrDate.split('-'))
		inputDate = date(splittedDate[2], splittedDate[1], splittedDate[0])
		print inputDate

		allStudents = file_to_list('files/students.dat')
		defaulterStudents = {}

		for student in allStudents:
			regDate = student['regdate']
			numOfDays = (regDate-inputDate).days
			if numOfDays > 0:
				fine = numOfDays * PER_DAY_FINE
				defaulterStudents[student['rollno']] = fine
		print defaulterStudents

		return render_template('fine_tab.html', data = defaulterStudents)
	else:
		return render_template('fine.html')
