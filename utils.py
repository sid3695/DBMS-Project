import pickle
import datetime

def write_com(param1, fname):
	with open(fname,'wb') as f:
		pickle.dump(param1,f)

def file_to_list(param1):
	temp = []
	try:
		with open(param1,'rb+') as f:
			temp = pickle.load(f)
	except:
		print 'IOError-Exception'
		temp = []
	return temp