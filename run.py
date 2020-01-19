from solvers.bfs_solver import BreadthFirstSearch
from solvers.backtracking_solver import BacktrackingIterativeSearch
from solvers.dijkstra_solver import WeightedSearch
from visualizations.grid_maze_visualization import MazePlot
from maze_generators.kruskal import KruskalMaze


class MazeRunner:
	def __init__(self,width,height):
		"""input: matrix width and height"""
		self.width = width
		self.height = height
		self.maze = KruskalMaze(self.width,self.height)
		self.graph = [[0 for x in range(self.width)]for y in range(self.height)]
		self.visualization = self.generate_visualization(name="maze")
		#save initial maze layout as a png
		self.visualization.save_as_image()
		self.solve_maze_bfs()
		self.solve_maze_backtracking_iterative()
		self.solve_maze_weighted()

	def generate_visualization(self, name=None):
		if name:
			visualization = MazePlot(self.width,self.height,self.maze,maze_name=name)
		else:
			visualization = MazePlot(self.width,self.height,self.maze)
		return visualization

	def solve_maze_backtracking_iterative(self):
		print("backtracking iterative maze")
		self.visualization.clear_maze()
		self.visualization.maze_name = "backtrack_iterative"
		entry_exit_points = self.visualization.entry_exit_points
		self.maze_solver = BacktrackingIterativeSearch(self.graph,self.maze.legal_edges,starting_point=entry_exit_points[0],exits=entry_exit_points[1:])
		self.visualization.path = self.maze_solver.path
		self.visualization.animate()
		return

	def solve_maze_bfs(self):
		print("breadth first search maze")
		self.visualization.clear_maze()
		self.visualization.maze_name = "bfs"
		entry_exit_points = self.visualization.entry_exit_points
		self.maze_solver = BreadthFirstSearch(self.graph,self.maze.legal_edges,starting_point=entry_exit_points[0],exits=entry_exit_points[1:])
		path = self.maze_solver.path
		self.visualization.path = path
		self.visualization.animate()
		return

	def solve_maze_weighted(self):
		print("breadth first search with weights maze")
		self.visualization.clear_maze()
		self.visualization.maze_name = "weighted_search"
		entry_exit_points = self.visualization.entry_exit_points
		self.maze_solver = WeightedSearch(self.graph,self.maze.legal_edges,starting_point=entry_exit_points[0],exits=entry_exit_points[1:])
		self.visualization.path = self.maze_solver.path
		self.visualization.animate()
		return		




MazeRunner(20,20)