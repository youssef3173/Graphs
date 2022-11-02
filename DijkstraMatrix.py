G = [[ 0, -1, -1,  2, -1, -1, -1, -1 ],
	[ -1,  0,  8,  6, -1, -1, -1, -1 ],
	[ -1,  8,  0, -1,  8, -1, -1, -1 ],
	[  2,  6, -1,  0,  1, -1,  9,  6 ],
	[ -1, -1,  8,  1,  0, -1, -1,  4 ],
	[ -1, -1, -1, -1, -1,  0,  3, -1 ],
	[ -1, -1, -1,  9, -1,  3,  0,  2 ],
	[ -1, -1, -1,  6,  4, -1,  2,  0 ]]



def Dijkstra( G, start):
	inf = float('inf')
	D = { node:inf for node in range(len(G))}
	T = { node:start for node in range(len(G))}

	for node in range(len(G)):
		if G[start][node] > 0:
			D[node] = G[start][node]


	Visited = [start]
	while len(Visited) < len(G) - 1:
		minD = inf
		for node1 in range(len(G)):
			if (D[node1] < minD) and (node1 not in Visited):
				minD = D[node1]
				snode = node1
		
		Visited.append( snode)
		for node2 in range(len(G[snode])):
			if (G[snode][node2] > 0) and (node2 not in Visited) and (D[snode] + G[snode][node2] < D[node2]):
				D[node2] = D[snode] + G[snode][node2]
				T[node2] = snode

	return D, T




def find_path( Tracks, start, end):
	nodes = [chr(n) for n in range(97, 97+len(G))]

	path = []
	tmp = end

	while tmp != start:
		path.append( nodes[tmp])
		tmp = Tracks[tmp]

	path.append( nodes[start])
	return path




ss = 1   # 'b' node
D, T = Dijkstra( G, ss)

nodes = [chr(n) for n in range(97, 97+len(G))]
print( "Distnaces: " )
for key in D:
	print( f" {nodes[key]} -> {D[key]} -> {nodes[T[key]]}")

ee = 5
path = find_path( T, ss, ee)
print( path )
