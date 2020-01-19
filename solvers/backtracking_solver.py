import random
from solvers.maze_solver import MazeSolver

"""
Solves a maze using a backtracking search algorithm and returns a list of the x,y coordinates for each step in the path.

Input: 
	graph - matrix (same size as graph used to create the maze)
	legal edges - edges that do not have a maze wall between the nodes

Output:
	path - a list of (x,y) coordinates for each step in the path from the entry to exit
"""

class BacktrackingIterativeSearch(MazeSolver):
	def __init__(self,graph,legal_edges=None,starting_point=(0,0),exits=None):
		super().__init__(graph,legal_edges,starting_point,exits)
		self.path = self.backtrack()

	def backtrack(self):
		current = self.starting_point
		path = []
		seen = []
		while current not in self.exits:
			neighbors = [n for n in self.get_neighbors(current) if n not in path]
			if len(neighbors) > 0:
				seen.append(current)
				path.append(current)
				random_neighbor = neighbors[random.randint(0,len(neighbors)-1)]
				current = random_neighbor
			elif len(seen) > 0:
				path.append(current)
				current = seen.pop()
		path.append(current)
		return path