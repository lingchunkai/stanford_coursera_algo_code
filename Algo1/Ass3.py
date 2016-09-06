N_VERTICES = 200
adj_list = [[] for x in xrange(N_VERTICES)]

import random

def Kargers(N_VERTICES, adj_list):
	edges = set()
	#print adj_list
	for n1, neighbours in enumerate(adj_list):
		for n2 in neighbours:
			edges.add(tuple(sorted([n1, n2])))

	edges = list(edges)

	while True:
		L = random.randint(0, len(edges)-1)
		A,B = edges[L]

		edges2 = []
		nodes_left = set()
		for k in edges:
			x,y = k
			if x == B:
				x = A
			if y == B:
				y = A
			if x > y: x, y = y, x
			nodes_left.add(x)
			nodes_left.add(y)
			if x==y: continue
			edges2.append((x,y))
		edges=edges2

		if len(nodes_left) == 2: 
			break

	return len(edges)


for k in xrange(N_VERTICES):
	splits = map(int, raw_input().split())
	splits = [x-1 for x in splits]
	vertex_index = splits[0]
	adj_list[vertex_index] = splits[1:]


bestmin = 100
for n in xrange(10000):
	bestmin = min(bestmin, Kargers(N_VERTICES, adj_list))
	print bestmin