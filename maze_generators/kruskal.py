import random

"""
Generates a random maze from the given width and height using Kruskal's algorithm for minimum spanning trees

Output:
	maze - the edges of the spanning tree
	legal_edges - a dictionary of nodes as keys and a list of legal edges to traverse as values
"""


class KruskalMaze:
	def __init__(self,width,height):
		self.width = width
		self.height = height
		self.nodes,self.edges = self.create_graph()
		self.maze = self.generate_maze()
		self.legal_edges = self.get_legal_traversal_edges()

	def get_random_edge_weights(self):
		"""assigns random weights to each edge of the graph"""
		edge_weights = [(random.randint(1,4),x,y) for (x,y) in self.edges]
		return edge_weights

	def get_legal_traversal_edges(self):
		"""gets legal edges for each node based on the spanning tree. illegal edges are walls"""
		legal_edges = {}
		for s in sorted(self.maze):
			if s[0] not in legal_edges:
				legal_edges[s[0]] = [s[1]]
			else:
				legal_edges[s[0]].append(s[1])
			if s[1] not in legal_edges:
				legal_edges[s[1]] = [s[0]]
			else:
				legal_edges[s[1]].append(s[0])
		return legal_edges

	def create_graph(self):
		"""for now can't move diagonally"""
		x = self.width
		y = self.height
		nodes = set()
		edges = set()
		for i in range(x):
			for j in range(y):
				nodes.add((i,j))
				if i > 0:
					e1 = (i-1,j)
					edges.add(((i,j),e1))
				if i < x-1:	
					e2 = (i+1,j)
					edges.add(((i,j),e2))
				if j > 0:			
					e3 = (i,j-1)
					edges.add(((i,j),e3))
				if j < y-1:				
					e4 = (i,j+1)
					edges.add(((i,j),e4))
		return nodes,edges

	def generate_maze(self):
		"""implements kruskal's algorithm to generate minimum spanning tree"""
		edge_weights = self.get_random_edge_weights()
		clusters = {n:n for n in self.nodes}
		ranks  = {n:0 for n in self.nodes}
		solution = set()

		def find(u):
			if clusters[u] != u:
				clusters[u] = find(clusters[u])
			return clusters[u]

		def union(x,y):
			x,y = find(x), find(y)
			if ranks[x] > ranks[y]:
				clusters[y] = x
			else:
				clusters[x] = y
			if ranks[x] == ranks[y]:
				ranks[y] += 1

		for w,x,y in sorted(edge_weights):
			if x != y:
				if find(x) != find(y):
					#add edge to solution
					solution.add((x,y))
					union(x,y)
		return solution
