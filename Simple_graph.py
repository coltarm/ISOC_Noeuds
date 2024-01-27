import networkx as nx
import random
class node:
	def __init__(self,v,value=0):
		self.v = v
		self.value = value
		self.time = random.randint(0,10000)

	def getTime():
		return self.time
	def getValue(): # on doit être capable de déterminer la valeur de chaque noeuds avec une valeur de +- 50% (c'est la vision des noeuds)
		value_gap = random.randint(50,150)
		estimate_time = self.time * value_gap/100
		return estimate_time
#Question comment on gère quands plusieurs noeuds font le choix en même temps, chacun ne doit pas être au courant du choix de l'autre
def connection_choice(G, node): # On fait une fonction qui décrit le choix de à quelle noeuds décide de se connecter le noeuds, on donne en argument le graph et le noeuds qui fait le choix.
	pass


def create_graph(n)#créer un graphe de n noeuds
	Node_liste = list(range(n))
	G = nx.Graph()
	G.add_nodes_from(Node_Liste)
	return G

def who_play(Node_list, round): # objectif de cette fonction est de déterminer qui doit jouer au prochain tour. On prend en argument la liste des noeuds et le tour dans lequel on est.
	smallest
	pass
