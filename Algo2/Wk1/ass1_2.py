import heapq


class optimal:
    def __init__(self, weight, length):
        self.weight = weight
        self.length = length
    
    def __lt__(self, other):
        return self.weight * other.length > other.weight * self.length
    
    def __str__(self):
        return str(tuple([self.weight, self.length]))

NJOBS = int(raw_input())
heap = []
for k in xrange(NJOBS):
    jw, jl = tuple(map(int, raw_input().split()))
    heapq.heappush(heap, optimal(jw, jl))

time = 0
tcost = 0
while len(heap) > 0:
    job = heapq.heappop(heap)
    time = time + job.length
    cost = job.weight * time
    tcost += cost

print tcost
