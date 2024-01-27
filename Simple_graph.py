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
def connection_choice(G, Nodes): # On fait une fonction qui décrit le choix que vont faire les noeuds à qui c'est leur tour de jouer
	pass


def create_graph(n)#créer un graphe de n noeuds
	Node_liste = [node(k) for k in range(n)] 
	G = nx.Graph()
	G.add_nodes_from(Node_Liste)
	return G

def who_play(Node_list): # objectif de cette fonction est de déterminer qui doit jouer au prochain tour. On prend en argument la liste des noeuds qui doivent jouer et le tour dans lequel on est.
	Node_smallest_time = [] 
	smallest_time = 10000000000000000000000000
	for node in Node_list:
		if smallest_time<= node.getTime():
			smallest = node.getTime()
			Node_smallest_time.append(node)
	return Node_smallest_time

def game():
	G = create_graph(10)
	List_node = list(G.nodes)
	List_nodes_to_play = List_node[:]
	while Liste_nodes_to_play != []:
		Playing_nodes = who_play(List_nodes_to_play)
		connection_choice(G,Playing_nodes) # il faut compléter la fonction connection_choice pour créer la connection entre deux noeuds

