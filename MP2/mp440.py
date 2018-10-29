import random

''' ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ '''
'''
                For Search Algorithms
'''
''' ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ '''

'''
BFS add to queue
'''
def add_to_queue_BFS(node_id, parent_node_id, cost, initialize=False):
    # Your code here
     if initialize is True:
         global queue_BFS
         queue_BFS = []
     queue_BFS.append((node_id, parent_node_id))
     #print queue_BFS
     return

'''
BFS add to queue
'''
def is_queue_empty_BFS():
    # Your code here
    if len(queue_BFS) == 0:
        return True
    return False

'''
BFS pop from queue
'''
def pop_front_BFS():
    (node_id, parent_node_id) = (0, 0)
    # Your code here
    (node_id, parent_node_id) = queue_BFS.pop(0)
    return (node_id, parent_node_id)

'''
DFS add to queue
'''
def add_to_queue_DFS(node_id, parent_node_id, cost, initialize=False):
    # Your code here
    if initialize is True:
        global queue_DFS
        queue_DFS = []
    queue_DFS.insert(0, (node_id, parent_node_id))
    # print queue_DFS
    return

'''
DFS add to queue
'''
def is_queue_empty_DFS():
    # Your code here
    if len(queue_DFS) == 0:
        return True
    return False

'''
DFS pop from queue
'''
def pop_front_DFS():
    (node_id, parent_node_id) = (0, 0)
    # Your code here
    (node_id, parent_node_id) = queue_DFS.pop(0)
    return (node_id, parent_node_id)

'''
UC add to queue
'''
def add_to_queue_UC(node_id, parent_node_id, cost, initialize=False):
    # Your code here
    if initialize is True:
        global queue_UC
        global cost_UC
        cost_UC = 0
        queue_UC = []
    index = 0
    for tuple in queue_UC:
        if tuple[1] == parent_node_id:
            if tuple[2] >= cost + cost_UC:
                queue_UC.insert(index, (node_id, parent_node_id, cost + cost_UC))
                #print "Add:", queue_UC
                return
        if tuple[2] > cost + cost_UC:
            queue_UC.insert(index, (node_id, parent_node_id, cost + cost_UC))
            #print "Add:", queue_UC
            #print cost
            return
        index += 1
    queue_UC.append((node_id, parent_node_id, cost + cost_UC))
    #print "Add:", queue_UC
    return

'''
UC add to queue
'''
def is_queue_empty_UC():
    # Your code here
    if len(queue_UC) == 0:
        return True
    return False

'''
UC pop from queue
'''
def pop_front_UC():
    (node_id, parent_node_id) = (0, 0)
    # Your code here
    (a, b, cost) = queue_UC.pop(0)
    global cost_UC
    cost_UC = cost
    #print "Cost from Pop:", cost_UC
    (node_id, parent_node_id) = (a, b)
    #print "Pop:", (node_id, parent_node_id)
    return (node_id, parent_node_id)

'''
A* add to queue
'''
def add_to_queue_ASTAR(node_id, parent_node_id, cost, initialize=False):
    # Your code here
    if initialize:
    	global queue_ASTAR
    	queue_ASTAR = []
    upper = len(queue_ASTAR) - 1
    if len(queue_ASTAR) != 0:
	    lower = 0
	    while upper >= lower:
	    	pos = (upper + lower) // 2
	    	if queue_ASTAR[pos][2] >= cost:
	    		upper = pos - 1
	    	elif queue_ASTAR[pos][2] < cost:
	    		lower = pos + 1

    queue_ASTAR.insert(upper+1, (node_id, parent_node_id, cost))
    return
'''
A* add to queue
'''
def is_queue_empty_ASTAR():
	# Your code here
    if len(queue_ASTAR) == 0:
    	return True
    return False

'''
A* pop from queue
'''
def pop_front_ASTAR():
    (node_id, parent_node_id) = (0, 0)
    # Your code here
    (a, b, c) = queue_ASTAR.pop(0)
    (node_id, parent_node_id) = (a, b)
    return (node_id, parent_node_id)

''' ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ '''
'''
                For n-queens problem
'''
''' ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ '''


'''
Compute a random state 
'''
def get_random_state(n):
	state = []
	for a in range(n):
		state.append(random.randint(1, n))

	return state

'''
Compute pairs of queens in conflict 
'''
def compute_attacking_pairs(state):
    number_attacking_pairs = 0
    for x in range(0,len(state),1):
    	for y in range(x+1, len(state),1):
    		diff = y - x
    		if state[x] == state[y]:
    			number_attacking_pairs += 1
    		elif state[x] == (state[y] + diff):
    			number_attacking_pairs += 1
    		elif state[x] == (state[y] - diff):
    			number_attacking_pairs += 1

    return number_attacking_pairs

'''
The basic hill-climing algorithm for n queens
'''
def hill_desending_n_queens(state, comp_att_pairs):
	final_state = list(state)
	current = comp_att_pairs(state)

	#Test Each Row
	while current != 0:
		end = False
		original = list(final_state)
		test = list(original)

		for x in range(len(state)):
			for y in range(1, len(state)+1):
				test[x] = y
				testPairs = comp_att_pairs(test)

				if testPairs < current:
					final_state = list(test)
					current = testPairs
					end = True
					break
			if end:
				break

			test[x] = final_state[x]
		
		if end:
			continue
		return final_state
	return final_state

'''
Hill-climing algorithm for n queens with restart
'''
def n_queens(n, get_rand_st, comp_att_pairs, hill_descending):
    final_state = hill_descending(get_rand_st(n), comp_att_pairs)
    while comp_att_pairs(final_state) != 0:
    	final_state = hill_descending(get_rand_st(n), comp_att_pairs)

    return final_state
