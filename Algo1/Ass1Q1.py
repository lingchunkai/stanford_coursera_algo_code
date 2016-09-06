import copy

N_INTS = 100000
# N_INTS = 10
N_LEVELS = 18
num_list = []
for n in xrange(N_INTS):
	num_list.append(int(raw_input()))

def mergesort(nums):
	if len(nums) == 1: return (copy.deepcopy(nums), 0)
	midpoint = len(nums)/2
	left = nums[0:midpoint]
	right = nums[midpoint:]
	ll, leftinv = mergesort(left)
	rr, rightinv = mergesort(right)

	# merge
	merged = []
	li = 0
	ri = 0
	crossinv = 0
	while len(ll)-li > 0 or len(rr)-ri > 0:
		if len(ll)-li == 0: 
			merged.append(rr[ri])
			ri=ri+1
		elif len(rr)-ri == 0:
			merged.append(ll[li])
			li=li+1
		else: 
			if ll[li] < rr[ri]:
				merged.append(ll[li])
				li+=1
			else:
				merged.append(rr[ri])
				ri+=1
				crossinv += len(ll)-li
				
	return merged, leftinv+rightinv+crossinv

merged,inv= mergesort(num_list)

prev=-100
for k in merged:
	if k < prev: 
		print "gg", k

	prev = k

print inv