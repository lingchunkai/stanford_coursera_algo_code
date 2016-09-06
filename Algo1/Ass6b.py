import heapq  # defaults to min heap

N_NUMBERS = 10000

small_heap = []  # max heap
large_heap = []  # min heap
meds = []
nn = []
for n in xrange(N_NUMBERS):
    in_num = int(raw_input())
    nn.append(in_num)
    
    if len(small_heap) == 0 or small_heap[0] <= -in_num:
        heapq.heappush(small_heap, -in_num)
    else:
        heapq.heappush(large_heap, in_num)
    
    # transfer if necessary
    if len(small_heap) - len(large_heap) >= 2:
        w = -heapq.heappop(small_heap)
        heapq.heappush(large_heap, w)
    elif len(large_heap) - len(small_heap) >= 2:
        w = heapq.heappop(large_heap)
        heapq.heappush(small_heap, -w)

    if n >= 2:
        print -small_heap[0], large_heap[0]
    # get median
    if (n+1) % 2 == 0:
        meds.append(-small_heap[0])
    else:
        if len(small_heap) > len(large_heap):
            meds.append(-small_heap[0])
        else:
            meds.append(large_heap[0])



print sum(meds) % 10000