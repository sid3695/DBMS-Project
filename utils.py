import pickle

def write_com(param1, fname):
	with open(fname,'wb') as f:
		pickle.dump(param1,f)