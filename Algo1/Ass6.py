import sys

N_POINTS = 10**6

# read points
points = []
for n in xrange(N_POINTS):
    points.append(int(raw_input()))
points = list(sorted(points))
print len(points)

# use sliding window method
MIN_INTEREST = -10000
MAX_INTEREST = 10000

results = set()

max_start = len(points)-1
for x in xrange(len(points)):
    # print x
    for m in xrange(max_start, -1, -1):
        if points[m] + points[x] <= MAX_INTEREST:
            break
    max_start = m

    for m in xrange(max_start, -1, -1):
        if points[m] + points[x] < MIN_INTEREST:
            break

        if not m == x and not points[m] == points[x]:
            results.add(points[m] + points[x])

print len(results)
