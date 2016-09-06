# assuming the points are distinct
# since each vertices can have only 24C2 = const number of nodes that are 2-apart 
# we convert this to an unweighted graph
# and use floodfill 

N,B = map(int, raw_input().split())

bits=[]
bitsum_list = []
adj_list = [set() for n in xrange(N)]
bitsum_set = dict()
for n in xrange(N):
	bitmap = map(lambda x: True if x=='1' else False, raw_input().split())
	bitsum = sum([2**n * (1 if bitmap[n] == True else 0) for n in xrange(B)])
	
	if bitsum in bitsum_set: continue
	bits.append(bitmap)
	bitsum_set[bitsum] = len(bitsum_list)
	bitsum_list.append(bitsum)

# convert to unweighted graph
print 'done 1'
print len(bits)
print len(bitsum_set)
print len(bitsum_list)
# print bits[0]
q=0
N=len(bitsum_list)
for n in xrange(N):
	for m1 in xrange(B):
		next1 = bitsum_list[n] + (-1 if bits[n][m1]==True else 1) * (2 ** m1)
		
		# add
		if next1 in bitsum_set:
			j = bitsum_set[next1]
			adj_list[j].add(n)
			adj_list[n].add(j)
		
		for m2 in xrange(m1+1, B): 
			next2 = next1 + (-1 if bits[n][m2]==True else 1) * (2 ** m2)
			if next2 in bitsum_set:
				j = bitsum_set[next2]
				adj_list[j].add(n)
				adj_list[n].add(j)
		
print sum([len(adj_list[n]) for n in xrange(n)])
print max([len(adj_list[n]) for n in xrange(n)])

# floodfill
visited = [False] * N
nclusters=0
for n in xrange(N):
	if visited[n]: continue
	nclusters+=1
	q = [n]
	visited[n] = True
	while len(q) > 0:
		r = q.pop()
		for a in adj_list[r]:
			if visited[a]: continue
			q.append(a)
			visited[a] = True


print nclusters




