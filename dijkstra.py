#Auteur --> aiglematth

class Dijkstra():
	"""
	Une classe permettant de trouver le plus court chemin dans un graphe à la méthode de dijkstra
	"""
	def __init__(self, graph, log=False):
		"""
		:param graph: La matrice graphe à résoudre
		:param log:   Si vrai, un affichage sera fait pour suivre étape par étape la résolution
		"""
		self.graph = graph
		self.log   = log

	def max(self):
		"""
		:return: La valeur maximale qu'on peut obtenir en parcourant les maxs des lignes + 1 (en gros on définit un infini artificiel)
		"""
		maxx = []
		for x in range(len((self.graph))):
			maxx.append(0)
			for item in self.graph[x]:
				if item > maxx[x]:
					maxx[x] = item
		return sum(maxx) + 1

	def solve(self, a, b):
		"""
		:param a: Le Sommet de départ
		:param b: Le Sommet d'arrivé
		"""
		self.infini  = self.max()
		self.resolve = []
		self._solve(a, b)

	def _solve(self, a, b, this=[0], use=[]):
		"""
		:param a:    Sommet de départ
		:param b:    Sommet d'arrivé
		:param this: [cout_actuel, chemins, chemins, ..., chemins]
		:param use:  Une liste des points sommets déjà parcourues
		"""
		if a == b:
			this.append(b)
			self.resolve.append(tuple(this))
			if self.log : print(f"YES {a} == {b} , this={this} , use={use}")
			return True

		for y in range(len(self.graph[a])):
			if y != a and self.graph[a][y] != 0 and y not in use:
				this[0] += self.graph[a][y]
				this.append(a)
				use.append(a)
				if self.log : print(f"AVANT {a} --> {y} : {b} , this={this} , use={use}")
				self._solve(y, b, this=this, use=use)

				this[0] -= self.graph[a][y]
				this = this[0:this.index(a, 1)]
				use.pop()
				if self.log : print(f"APRES {a} --> {y} : {b} , this={this} , use={use}")

		

if __name__ == "__main__":
	graph = [
		 [0, 1, 2, 0, 0],
		 [0, 0, 0, 2, 7],
		 [0, 0, 0, 2, 0],
		 [0, 0, 0, 0, 3],
		 [0, 0, 0, 0, 0]
		]
	d = Dijkstra(graph)
	d.solve(0,3)
	for x in d.resolve:
		print(x)