# Define a (non-ortiented) Graph as a Matrix:
# indeces: (0,a) (1,b) (2,c) (3,d) (4,e) (5,f) (6,g) (7,h) 
G = [[ 0, -1, -1, 2, -1, -1, -1, -1 ],
	[ -1, 0, 5, 6, -1, -1, -1, -1 ],
	[ -1, 5, 0, -1, 8, -1, -1, -1 ],
	[ 2, 6, -1, 0, 1, -1, 9, 6 ],
	[ -1, -1, 8, 1, 0, -1, -1, 4 ],
	[ -1, -1, -1, -1, -1, 0, 3, -1 ],
	[ -1, -1, -1, 9, -1, 3, 0, 2 ],
	[ -1, -1, -1, 6, 4, -1, 2, 0 ]]

# Depth-First Search:
def DFS( G, v, Visited):
	nodes = { n:chr(n+97) for n in range(len(G)) }
	if (v >= len(G)) or (v in Visited): 
		return
	else:
		Visited.append( v)
		for u in range( len(G[v])):
			if (G[v][u] > 0) and (u not in Visited):
				print(  nodes[v], " -> ", nodes[u])
				DFS( G, u, Visited)


# Breadth-First Search:
def BFS( G, v, Visited):
	nodes = { n:chr(n+97) for n in range(len(G)) }
	if (v >= len(G)) or (v in Visited): 
		return
	else:
		cur = [v]
		while len(cur):
			c = cur.pop(0)
			Visited.append( c)
			for u in range( len(G[c])):
				if (G[c][u] > 0) and (u not in Visited) and (u not in cur):
					cur.append( u ) 
					print( f" {nodes[c]} -> {nodes[u]} ")


def number_connections( G ):
	nbr = 0
	for m in range( len(G)):
		for n in range( m, len(G[m])):
			if G[m][n] > 0:
				nbr += 1
	return nbr

def maxdegree( G ):
	max_d = 0
	node = 0
	for m in range( len(G)):
		cur_d = 0
		for n in range( len(G[m])):
			if G[m][n] > 0:
				cur_d += 1
		if cur_d > max_d:
			max_d = cur_d
			node = m
	return node, max_d


Vis = []
DFS( G, 3, Vis)
print( Vis)


Vis = []
BFS( G, 3, Vis)
print( Vis)

print( f"Number of Connetions in the Graph: {number_connections( G)}" )

node, maxd =  maxdegree( G)
print( f"Node {node} has maximun degree of {maxd}" )




