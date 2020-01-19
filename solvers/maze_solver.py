"""
Base class for other maze solvers.
"""

class MazeSolver:
	def __init__(self,graph,legal_edges=None,starting_point=(0,0),exits=None):
		"""
		graph = matrix
		legal_edges = dictionary of each node with the legal edges from the maze/spanning tree generation 

		starting_point = randomly generated entry point on one side
		exits = randomly generated exits on each of the other 3 sides
		"""
		self.graph = graph
		self.legal_edges = legal_edges
		self.starting_point = starting_point
		self.exits = exits	

	def get_neighbors(self,node):
		neighbors = self.legal_edges[node]
		return neighbors
