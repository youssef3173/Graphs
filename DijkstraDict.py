G = {'a':[( 'd', 2)],
	'b':[( 'c', 5), ( 'd', 6)],
	'c':[( 'b', 6), ( 'e', 8)],
	'd':[( 'a', 2), ( 'b', 6), ( 'e', 1), ( 'g', 9), ( 'h', 6)],
	'e':[( 'c', 8), ( 'd', 1), ( 'h', 4)],
	'f':[( 'g', 3)],
	'g':[( 'd', 9), ( 'f', 3), ( 'h', 2)],
	'h':[( 'd', 6), ( 'e', 4), ( 'g', 2)],}



def Dijkstra( G, start):
	nodes = [chr(n) for n in range(97, 97+len(G))]
	
	inf = float('inf')
	D = { node:inf for node in nodes}
	T = { node:start for node in nodes}

	D[start] = 0
	for node, dist in G[start]:
		D[ node ] = dist


	Visited = [ start]
	while len(Visited) < len(G) - 1:
		minD = inf
		for node1 in nodes:
			if (D[node1] < minD) and (node1 not in Visited):
				minD = D[node1]
				snode = node1
		
		Visited.append( snode)
		for node2, dist in G[snode]:
			if (node2 not in Visited) and (D[snode] + dist < D[node2]):
				D[node2] = D[snode] + dist
				T[node2] = snode

	return D, T




def find_path( Tracks, start, end):
	path = []
	tmp = end

	while tmp != start:
		path.append( tmp)
		tmp = Tracks[tmp]

	path.append( start)
	return path



nodes = nodes = [chr(n) for n in range(97, 97+len(G))]

ss = 'b'   # 'b' node
D, T = Dijkstra( G, ss)

print( "Distnaces: " )
for key in D:
	print( f" {key} -> {D[key]} -> {T[key]}")

ee = 'f'
path = find_path( T, ss, ee)
print( path )
