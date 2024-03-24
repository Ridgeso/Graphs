all_edges = [(u, v) for u in range(n) for v in range(u + 1, n)]
	# while all_edges:
	# 	u, v = random.choice(all_edges)
	# 	all_edges.remove((u, v))

	# 	if len(G[u]) < k and len(G[v]) < k:
	# 		G.add_edge(u, v)
	# 	else:
	# 		all_edges.append((u, v))