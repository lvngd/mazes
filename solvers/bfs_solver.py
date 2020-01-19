from collections import deque
from solvers.maze_solver import MazeSolver

"""
Solves a maze using the breadth-first search algorithm and returns a list of the x,y coordinates for each step in the path.

Input: 
	graph - matrix (same size as graph used to create the maze)
	legal edges - edges that do not have a maze wall between the nodes

Output:
	seen - a list of (x,y) coordinates for each step in the path from the entry to exit
"""


class BreadthFirstSearch(MazeSolver):
	def __init__(self,graph,legal_edges=None,starting_point=(0,0),exits=None):
		super().__init__(graph,legal_edges,starting_point,exits)
		self.path = self.solve_bfs()

	def solve_bfs(self):
		seen = []
		path = []
		queue = deque([self.starting_point])
		while queue:
			current = queue.pop()
			seen.append(current)
			#path.append((current,1))
			if current in self.exits:
				return seen
			neighbors = self.get_neighbors(current)
			for n in neighbors:
				if n not in seen and n not in queue:
					queue.appendleft(n)
		return seen