import copy
SIZE, N_ITEMS = map(int, raw_input().split())

VALUE = []
COST = []
for n in xrange(N_ITEMS):
	v,c = map(int, raw_input().split())
	VALUE.append(v)
	COST.append(c)

STO = dict()
STO[0] = 0
for k in xrange(N_ITEMS):
	STO2=copy.deepcopy(STO)
	for siz,val in STO.iteritems():
		newsize = siz + COST[k]
		newval = val + VALUE[k]
		if newsize > SIZE: continue
		if newsize in STO2 and STO2[newsize] < newval:
			STO2[newsize] = newval
		elif not newsize in STO2:
			STO2[newsize] = newval
		else: # old solution was better
			pass

	STO=STO2

print max(STO.iteritems(), key=lambda x:x[1])
	
