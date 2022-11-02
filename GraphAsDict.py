# Another Representation of Graphes: Dictionnary of lists
G = {'a':[( 'd', 2)],
	'b':[( 'c', 5), ( 'd', 6)],
	'c':[( 'b', 6), ( 'e', 8)],
	'd':[( 'a', 2), ( 'b', 6), ( 'e', 1), ( 'g', 9), ( 'h', 6)],
	'e':[( 'c', 8), ( 'd', 1), ( 'h', 4)],
	'f':[( 'g', 3)],
	'g':[( 'd', 9), ( 'f', 3), ( 'h', 2)],
	'h':[( 'd', 6), ( 'e', 4), ( 'g', 2)],}




# Depth-First Search:
def DFS( G, v, Visited):
	nodes = [chr(n) for n in range(97, 97+len(G))]
	idxs = { nodes[n]:n for n in range(len(nodes)) }

	if (v >= len(G)) or (v in Visited): 
		return
	else:
		Visited.append( nodes[v])
		for node, dist in G[nodes[v]]:
			if ( dist > 0) and ( node not in Visited):
				print( f" {nodes[v]} -> {node} ")
				DFS( G, idxs[node], Visited)


# Breadth-First Search:
def BFS( G, v, Visited):
	nodes = [chr(n) for n in range(97, 97+len(G))]
	idxs = { nodes[n]:n for n in range(len(nodes)) }

	if (v >= len(G)) or (v in Visited): 
		return
	else:
		cur = [nodes[v]]
		while len(cur):
			c = cur.pop(0)
			Visited.append( c)
			for node, dist in G[c]:
				if ( dist > 0) and ( node not in Visited) and ( node not in cur):
					cur.append( node ) 
					print( f" {c} -> {node} ")


def number_connections( G ):
	nbr = 0
	for key in G:
		nbr += len( G[key])
	return nbr//2

def maxdegree( G ):
	nodes = [chr(n) for n in range(97, 97+len(G))]

	max_d = 0
	mnode = 'a'
	for node in nodes:
		if len( G[node]) > max_d:
			max_d = len( G[node])
			mnode = node
	return mnode, max_d


print( "######### Depth-First Search: ##########")
Vis = []
DFS( G, 3, Vis)
print( Vis)


print( "######### Breadth-First Search: ##########")
Vis = []
BFS( G, 3, Vis)
print( Vis)

print( "######### Number of Connections: ##########")
print( f"Number of Connetions in the Graph: {number_connections( G)}" )

print( "######### Maximum Number of Connections: ##########")
node, maxd =  maxdegree( G)
print( f"Node '{node}' has maximun degree of {maxd}" )
