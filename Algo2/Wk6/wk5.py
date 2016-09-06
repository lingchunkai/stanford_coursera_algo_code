# We try to solve this using Tarjan's SCC algo.
# This is re-implemented from Algo1 for more clarity

n_variables = int(raw_input())
n_vertices = 2 * n_variables

# we will label vertices 0 to n_variables as x_1 ... x_n
# and label vertices n_variables to 2 * n_variables - 1 as not x_1 ... not x_n
adj_list = [[] for x in xrange(n_vertices)]
for n in xrange(n_variables):
    a, b = map(int, raw_input().split())

    # a v b is equivalent to saying not a --> b AND not b --> a
    # We need to convert a and b into their 0-indexed version

    va = abs(a)-1
    vb = abs(b)-1

    # raw value of a and b
    ra = va if a > 0 else va + n_variables
    rb = vb if b > 0 else vb + n_variables

    # negated value of a and b
    _ra = (ra + n_variables) % n_vertices
    _rb = (rb + n_variables) % n_vertices

    # add in constraint nodes
    adj_list[_ra].append(rb)
    adj_list[_rb].append(ra)

# Perform DFS proper. Because there can be up to 2 mil possibilities we need
# to manage our own stack rather than rely on recursive functions directly.

OPERATION_FIRST_ENTRY = 0
OPERATION_ITERATING_OVER_NEIGHBOURS = 1

idd = [-1] * n_vertices
idd_low = [n_vertices+1] * n_vertices
in_cur_cc = [False] * n_vertices
num_ided = 0  # number of vertices which have been ided (visited)
connected_components = []

for start_node in xrange(n_vertices):
    if idd[start_node] > 0:
        continue
    stack = [(start_node, OPERATION_FIRST_ENTRY)]
    cur_cc = []
    ret = None  # return variable if any
    while len(stack) > 0:
        params = stack.pop()
        node = params[0]
        operation = params[1]
        if operation == OPERATION_FIRST_ENTRY:
            # First time we explore a vertex
            idd[node] = num_ided
            idd_low[node] = num_ided
            num_ided += 1
            cur_cc.append(node)
            in_cur_cc[node] = True
            # Enter iterating-over-neighbours stage
            stack.append((node, OPERATION_ITERATING_OVER_NEIGHBOURS, 0))
            ret = None
        elif operation == OPERATION_ITERATING_OVER_NEIGHBOURS:
            # handle update of node_low if return exists
            if not ret == None:
                idd_low[node] = min(idd_low[node], ret)
            ret = None

            position_in_iteration = params[2]
            if position_in_iteration >= len(adj_list[node]):
                if idd_low[node] == idd[node]:
                    # found a connected component
                    new_component = []
                    while True:
                        new_node_to_component = cur_cc.pop()
                        new_component.append(new_node_to_component)
                        in_cur_cc[new_node_to_component] = False
                        if new_node_to_component == node:
                            break
                    connected_components.append(new_component)

                # no more neighbours to explore, prepare for return
                ret = idd_low[node]
            else:
                # append itself after return
                stack.append((node, OPERATION_ITERATING_OVER_NEIGHBOURS, position_in_iteration+1))

                next_node = adj_list[node][position_in_iteration]
                if idd[next_node] < 0:
                    # add in next node if not explored
                    stack.append((next_node, OPERATION_FIRST_ENTRY, 0))
                elif in_cur_cc[next_node]:
                    # update back edge if required
                    idd_low[node] = idd_low[next_node]

print 'Sanity check: ', 'pass' if sum([len(x) for x in connected_components]) else 'fail'
print "# Connected components: ", len(connected_components)

# post processing to check for inconsistencies
violated = False
for cc in connected_components:
    visited = set()
    for v in cc:
        if (v + n_variables) % n_vertices in visited:
            violated = True
            break
        visited.add(v)
    if violated:
        break

print "2SAT true" if not violated else "2SAT violated"