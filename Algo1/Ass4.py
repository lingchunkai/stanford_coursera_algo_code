import sys

N_VERTICES = 875714
# N_VERTICES = 9

# Tarjan's algorithm for SCCS
adj_list = [[] for x in xrange(N_VERTICES)]
for line in sys.stdin:
    tail, head = map(int, line.split())
    tail -= 1
    head -= 1

    adj_list[tail].append(head)

print 'input read'

# DFS
stack = [] # for dfs itself ( vertex_id, (0/1 for new, old) , [list of things to visit]  )
visited = [False] * N_VERTICES
# visited[0] = True
dfs_low = [10**10] * N_VERTICES
dfs_num = [-1] * N_VERTICES

dfs_cnt = 0
cc_collection = []

nret = 0
stack_cc = []
for start_vertex in xrange(N_VERTICES):
	# if visited[start_vertex]: continue
	if dfs_num[start_vertex] >= 0: continue
	stack.append((start_vertex, 0))
	# visited[start_vertex] = True
	ret = None
	
	while not len(stack) == 0:
		# print dfs_cnt, len(cc_collection)
		cmd = stack.pop()
		v = cmd[0]
		typ = cmd[1]
		if typ == 0:
			# print v
			dfs_num[v] = dfs_cnt
			dfs_cnt += 1
			# flag all next nodes as to visit
			stack.append((v, 1, 0))
			ret = None
			visited[v] = True
			stack_cc.append(v)
			dfs_low[v]=dfs_num[v]
		elif typ == 1:
			if not ret is None:
				dfs_low[v] = min(dfs_low[v], ret)
				ret = None
			if len(adj_list[v]) <= cmd[2]: 
				nret+=1
				# recursive step over, do return part here
				ret = dfs_low[v]
				if dfs_low[v] == dfs_num[v]: 
					# connected component here!
					cc = []
					while len(stack_cc) > 0:
						vv = stack_cc.pop()
						cc.append(vv)
						visited[vv]=False

						if vv == v: break
					cc_collection.append(cc)
				#visited[v] = False

			else:
				stack.append((v, 1, cmd[2]+1)) # reappend the next thing to visit

				# if not visited[adj_list[v][cmd[2]]]: 
				if dfs_num[adj_list[v][cmd[2]]] < 0: 
					stack.append((adj_list[v][cmd[2]], 0))
					ret = None
				else:
					# visited before
					ret = None
					if visited[adj_list[v][cmd[2]]]: 
						dfs_low[v] = min(dfs_low[v], dfs_num[adj_list[v][cmd[2]]])

#print visited
#print stack_cc
# print cc_collection
# print sum(map(len,cc_collection))
X = list(sorted(map(len, cc_collection), reverse=True))
print X[0:5]

# [129, 120, 94, 86, 86]
# [447515, 969, 459, 211, 205]
