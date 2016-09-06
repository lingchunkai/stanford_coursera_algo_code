import heapq

NN,NE = map(int, raw_input().split())

adj_list = [[] for x in xrange(NN)]
heap = []
for ne in xrange(NE):
    n1, n2, cost = map(int, raw_input().split())
    n1 -= 1
    n2 -= 1
    adj_list[n1].append((cost, n2))
    adj_list[n2].append((cost, n1))

vis = [False] * NN
curnode = 0
tcost = 0
for k in xrange(NN-1):
    vis[curnode] = True
    for j in adj_list[curnode]:
        heapq.heappush(heap, j)
    while True:
        c,n = heapq.heappop(heap)
        if not vis[n]: break

    tcost += c
    curnode = n

print tcost

