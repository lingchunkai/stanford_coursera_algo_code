import heapq

N = 200
adj_list = [[] for x in xrange(N)]
for n in xrange(N):
    Z = raw_input().split()
    for z in xrange(1,len(Z)):
        next_node, cost = map(int, Z[z].split(','))
        next_node -= 1
        adj_list[n].append((next_node, cost))

start_node = 0
pq = [(0, 0)]
heapq.heapify(pq)
visited = [False] * N
cost_reach = [float('inf')] * N
while len(pq) > 0:
    c, v = heapq.heappop(pq)
    if visited[v]:
        continue

    visited[v] = True
    cost_reach[v] = c

    for a, edge_cost in adj_list[v]:
        if visited[a]:
            continue
        heapq.heappush(pq, (c + edge_cost, a))

queries = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
print [cost_reach[x-1] for x in queries]
