import heapq
from solvers.maze_solver import MazeSolver

"""
Solves a maze using Dijkstra's weighted graph search algorithm and returns a list of the x,y coordinates for each step in the path.

Input: 
	graph - matrix (same size as graph used to create the maze)
	legal edges - edges that do not have a maze wall between the nodes

Output:
	seen - a list of (x,y) coordinates for each step in the path from the entry to exit
"""

class NodeWeight:
	"""node class for dijkstra/A* search"""
	def __init__(self,x,y,weight=0):
		self.x = x
		self.y = y
		self.weight = weight

	def __eq__(self,other):
		return self.weight == other.weight

	def __lt__(self,other):
		return self.weight < other.weight

	def __str__(self):
		return "{},{}".format(self.x,self.y)

class WeightedSearch(MazeSolver):
	def __init__(self,graph,legal_edges=None,starting_point=(0,0),exits=None):
		super().__init__(graph,legal_edges,starting_point,exits)
		self.path = self.solve_maze()

	def get_weight(self,node):
		"""gets the minimum distance from that node to any of the exit points"""
		x1 = node[0]
		y1 = node[1]
		weights = [abs(x1-x2) + abs(y1-y2) for x2,y2 in self.exits]
		weight = min(weights)
		return weight

	def solve_maze(self):
		all_seen = []
		seen = []
		print(self.starting_point)
		start_node = NodeWeight(self.starting_point[0],self.starting_point[1],self.get_weight(self.starting_point))
		queue = [start_node]
		heapq.heapify(queue)
		while queue:
			current = heapq.heappop(queue)
			seen.append((current.x,current.y))
			if (current.x,current.y) in self.exits:
				return seen
			neighbors = self.get_neighbors((current.x,current.y))
			for n in neighbors:
				if n not in seen and not any(nd.x == n[0] and nd.y == n[1] for nd in queue):
					new_node = NodeWeight(n[0],n[1],self.get_weight(n))
					heapq.heappush(queue,new_node)
		return seen
