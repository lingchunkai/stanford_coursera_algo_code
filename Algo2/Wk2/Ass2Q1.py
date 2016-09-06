K = 4
N = int(raw_input())

# edge = [[0 for x in xrange(N)] for y in xrange(N)]
edge_list = []
for n in xrange(N*(N-1)/2):
	n1,n2,d = map(int, raw_input().split())
	n1-=1
	n2-=1
	edge_list.append((d,n1,n2))

edge_list = sorted(edge_list)

# since this graph has edges of order V^2=E, there is technically no advantage in us implementing tree-based union find. 
# asymptoticlaly this is equal to just brute force merging, since we will merge at most N times, and each merge costs O(N)
# but we have already spent O(N^2 log (N)) time sorting

node_owner = [n for n in xrange(N)]
nodes_inside = [[n] for n in xrange(N)]

e = 0
m = 0
spacing = 1000000
# while m < N-K:	
while m < N-1:
	# check 
	d,n1,n2 = edge_list[e]
	if node_owner[n1] == node_owner[n2]: 
		pass
	else:
		if len(nodes_inside[node_owner[n2]]) > len(nodes_inside[node_owner[n1]]):
			n1,n2=n2,n1
		for x in nodes_inside[node_owner[n2]]:
			nodes_inside[node_owner[n1]].append(x)
			node_owner[x] = node_owner[n1]
		if m >= N-K:
			spacing = min([spacing, d])
		m+=1
	e+=1

	
print spacing