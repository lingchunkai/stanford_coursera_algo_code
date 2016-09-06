import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import heapq
import itertools

N = int(raw_input())

coords = []
for n in xrange(N):
    coords.append(np.array(tuple(map(float, raw_input().split()))))
coordsarr = np.array(coords)
print coordsarr.shape

# Compute all pairwise distances
distmap = np.zeros([N, N])
for n in xrange(N):
    for m in xrange(N):
        distmap[n, m] = np.linalg.norm(coords[n]-coords[m])

# Using Prims, compute MST for upper bound of TSP problem
visited = [False] * N
visited[0] = True
edge_q = []
heapq.heapify(edge_q)
for n in xrange(1, N):
    heapq.heappush(edge_q, (distmap[0, n], n, 0))

tcost = 0
edges_mst = [[] for x in xrange(N)]
while len(edge_q) > 0:
    c, n, n2 = heapq.heappop(edge_q)
    if visited[n]:
        continue
    visited[n] = True
    tcost += c
    edges_mst[n].append(n2)
    edges_mst[n2].append(n)
    for m in xrange(N):
        if m == n:
            continue
        heapq.heappush(edge_q, (distmap[m, n], m, n))

c_upperbound = 2 * tcost
print c_upperbound

# Get upper bound using traversal in dfs order
best_min_tcost = float('inf')
for start in xrange(N):
    visited = [False] * N
    to_visit_stack = [start]
    visited_order = []
    while len(to_visit_stack) > 0:
        v = to_visit_stack.pop()
        if visited[v]:
            continue
        visited[v] = True
        visited_order.append(v)
        for a in edges_mst[v]:
            if visited[a]:
                continue
            to_visit_stack.append(a)
    visited_order.append(visited_order[0])
    tcost = sum([distmap[visited_order[x], visited_order[x+1]] for x in xrange(N)])
    best_min_tcost = min(tcost, best_min_tcost)
print 'upper bound: ', best_min_tcost
c_upperbound = best_min_tcost


# Naive brute force
# L = list(itertools.permutations(list(xrange(N))))
# print L
# mincost = float('inf')
# mew = []
# for l in L:
#     cost = 0
#     for x in xrange(N-1):
#         cost += distmap[l[x], l[x+1]]
#     cost += distmap[l[-1], l[0]]
#     # mincost = min(mincost, cost)
#     mew.append(cost)

# print 'min brute: ', min(mew)


# Brute force implementation of TSP using DP
end = [dict() for end in xrange(N)]  # [endbit][bitmask]
end[0][1] = 0

for n_iter in xrange(1, N):
    store = [dict() for endpoint in xrange(N)]
    for endpoint in xrange(N):
        for bitmask, v in end[endpoint].iteritems():
            for newend in xrange(N):
                if (2**newend) & (bitmask) > 0:
                    continue
                nextbitmask = bitmask + (2**newend)
                newcost = v + distmap[newend, endpoint]
                if newcost > c_upperbound:
                    continue
                if nextbitmask not in store[newend]:
                    store[newend][nextbitmask] = newcost
                else:
                    store[newend][nextbitmask] = min(store[newend][nextbitmask], newcost)
    end = store
    print [len(x) for x in store]

print end
best = float('inf')
for endpoint in xrange(N):
    for bitmask, v in end[endpoint].iteritems():  # technically no need to loop, only one possible bitmask
        newcost = store[endpoint][bitmask] + distmap[0, endpoint]
        best = min(best, newcost)

print best
print int(best)

# Plot tsp
# plt.scatter(coordsarr[:, 0], coordsarr[:, 1])
# plt.show()
