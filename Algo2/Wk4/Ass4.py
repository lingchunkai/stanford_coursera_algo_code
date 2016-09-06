# Johnsons' algorithm, we do not take advantage of the small minimum cost for each edge

import copy
import heapq


N,E = map(int, raw_input().split())
edge_list = []
adj_list = [[] for x in xrange(N+1)]

for e in xrange(E):
	v1, v2, c = map(int, raw_input().split())
	edge_list.append((v1,v2,c))
	adj_list[v1].append((c,v2))

# Create G', dual graph and run bellman ford on it
for v in xrange(1,N+1):
	adj_list[0].append((0,v))

bmf = [float('inf')] * (N+1)
bmf[0] = 0

for t in xrange(N+2):
	print t
	bmf_next = copy.deepcopy(bmf)
	for n in xrange(N+1):
		for c,v in adj_list[n]:
			bmf_next[v] = min(bmf_next[v], bmf[n] + c)

	# check for changed
	change = False
	for n in xrange(N+1):
		if not bmf_next[n] == bmf[n]: change = True
	bmf = bmf_next

if change: print 'negative cycle detected'

######################################################################################################

print 'constructing modified graph'

adj_list2 = [[] for x in xrange(N+1)]
for v1 in xrange(1, N+1):
	for c,v2 in adj_list[v1]:
		adj_list2[v1].append((c+bmf[v1]-bmf[v2], v2))

print 'running dijkstras'
shortest_shortest = float('inf')
for source in xrange(1,N+1):
	visited = [False] * (N+1)
	shortest_path = [0] * (N+1)
	pq = []
	heapq.heappush(pq, (0, source))

	while (len(pq) > 0):
		costs, v = heapq.heappop(pq)
		if visited[v]: continue
		visited[v] = True
		shortest_path[v] = costs
		for c,v2 in adj_list2[v]:
			if visited[v2]: continue
			heapq.heappush(pq, (c + costs, v2))

	# adjust to negative costs
	for g in xrange(1, N+1):
		shortest_path[g] += bmf[source]-bmf[g]

	shortest_shortest = min(shortest_shortest, min(shortest_path))

if change: print 'negative cycle detected'
print shortest_shortest

#g3:-19
#g2:-226
#g3:-331