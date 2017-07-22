#!/usr/bin/python
"""
Implementation of a bloom filter

"""


def insert(**kwargs):
	"""
	Insert function takes the following params:
	- kwargs['bf'] a Bloom filter initialized to 0 The Bloom filter
				MUST be a list to be updated.
	- kwargs['f'] a list of hash functions that operates over values
				you want to be inserted.

	- kwargs['values'] a list of values that has to be inserted in the
					Bloom Filter.

	"""
	for f in kwargs['f']:
		l = [f(x) for x in kwargs['values']]
		for i in l:
			kwargs['bf'][i] = 1


def search(**kwargs):
	"""
	search function takes the following params:
	- kwargs['bf'] a Bloom filter 
				
	- kwargs['f'] a list of hash functions that operates over values
				you want to be inserted.

	- kwargs['value'] the value  you want to search in the Bloom Filter.
					
	Returns true or false

	"""
	bf = kwargs['bf']
	v  =  kwargs['value']
	hashFuncs = kwargs['f']

	z = [ 1 if  bf[f(v)] == 1 else 0  for f in hashFuncs ]

	if 0 in  z:
		return False
	else:
		return True



if __name__=='__main__':
	m = 32
	bf = [0] * m
	
	"""
	Simple hash functions for demonstration purpose only.
	"""
	hashfuncs = (lambda x:(((x**2) + (x**3)) % m),
	             lambda x:((((x**2) + (x**3))*2) % m),
		     lambda x:((((x**2) + (x**3))*3) % m))

	insert(f=hashfuncs, bf=bf,values=[2013,2010, 2007, 2004, 2001, 1998])
	print(bf)
	if search(f=hashfuncs, bf=bf,value=2013) is True:
		print("value is present")

