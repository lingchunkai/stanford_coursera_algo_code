import copy
N_INTEGERS = 10000

X = []
for x in xrange(N_INTEGERS):
	X.append(int(raw_input()))

#X=X[0:5]

def pivotfirst(X):
	pass

def pivotlast(X):
	#print X
	X[0],X[-1] = X[-1],X[0]
	#print X

def pivotmedian(X):
	center_spot = (len(X)-1)/2
	Z = sorted([(X[0], 0), (X[center_spot], center_spot), (X[-1], -1)])
	target_loc = Z[1][1]
	X[0],X[target_loc] = X[target_loc], X[0]
 
def QuickSort(X, setpivot):
	if len(X) == 1 or len(X) == 0: 
		return X,0

	setpivot(X)	
	i=1
	j=1
	while(j<len(X)):
		if X[j] < X[0]:
			X[i], X[j] = X[j], X[i]
			i+=1
		j+=1

	X[i-1],X[0] = X[0], X[i-1]

	left, cmp_left = QuickSort(X[0:i-1], setpivot)
	right, cmp_right = QuickSort(X[i:], setpivot)
	return left + [X[i-1]] + right, cmp_left+cmp_right+len(X)-1

print X
Y1,z1=QuickSort(copy.deepcopy(X), pivotfirst)
Y2,z2=QuickSort(copy.deepcopy(X), pivotlast)
Y3,z3=QuickSort(copy.deepcopy(X), pivotmedian)
print Y1
print Y2
print Y3
print z1, z2, z3

