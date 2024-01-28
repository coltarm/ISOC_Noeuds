import networkx as nx
import random
class node: # On crée un objet noeuds qui contient les informations d'un noeuds ça valeur , le temps auquel il doit jouer.
	def __init__(self,v,value=0):
		self.v = v
		self.value = value
		self.time = random.randint(0,10000)
		self.Neighbors =[]

	def getTime(self):
		return self.time

	def addValue(self,value_to_add ):
		self.value += value_to_add

	def addNeighbor(self, node): #on stocke les voisins dans Neighbor puisqu'on doit update notre valeur en foction de la valeur de notre voisin.
		self.Neighbors.append(node)

	def getValue(self): # on doit être capable de déterminer la valeur de chaque noeuds avec une valeur de +- 50% (c'est la vision des noeuds)
		value_gap = random.randint(50,150)
		estimate_value = self.value * value_gap/100
		return estimate_value
	def getExactValue(self):
		return self.value

	def updateValue(self):
		value = 0
		for node in self.Neighbors:
			value+= node.getExactValue()
		self.value = value

#Question comment on gère quands plusieurs noeuds font le choix en même temps, chacun ne doit pas être au courant du choix de l'autre?
# Idée on va supposer que ils vont faire des choix similaire.
#Question combien de connection peut faire un noeuds?
# Dans un premier temps on va supposer que ils chacun doit faire un unique choix


def connection_choice(G, Nodes): # On fait une fonction qui décrit le choix que vont faire les noeuds à qui c'est leur tour de jouer
	Node_max =[] # on va stocker les noeuds parmi les quelquels je peux faire un choix.
	val_max=0
	for node in Nodes:
		if val_max<= node.getValue():
			Node_max.append(node)
			val_max = node.getValue()
	return random.choices(Node_max) #on retourne les noeuds avec la valeur maximal, qui va permettre de maximiser ma valeur.

def create_connection(G, List_node_to_connect): #on donne en argument le graph et la liste d'association à réaliser
	for asso in List_node_to_connect:
		node1 = asso[0]
		node2 = asso[1]
		node1.addNeighbor(node2)
		node2.addNeighbor(node1)
		G.add_edge(node1,node2)
		


def create_graph(n):#créer un graphe de n noeuds
	Node_liste = [node(k) for k in range(n)] 
	G = nx.Graph()
	G.add_nodes_from(Node_liste)
	return G

def who_play(Node_list): # objectif de cette fonction est de déterminer qui doit jouer au prochain tour. On prend en argument la liste des noeuds qui doivent jouer et le tour dans lequel on est.
	Node_smallest_time = [] 
	smallest_time = Node_list[0].getTime() 
	for node in Node_list: # on cherche les noeuds qui sont les prochains à jouer et donc se pour qui Tv est le plus petit
		if smallest_time>= node.getTime(): 
			smallest = node.getTime()
			Node_smallest_time.append(node)
	return Node_smallest_time

def game():
	G = create_graph(10000)
	List_node = list(G.nodes)
	List_nodes_to_play = List_node[:]
	Association =[]# on stocke les assoqu'on doit faire
	while List_nodes_to_play != []: # Pour chaque joueur on détermine quand il doit jouer et à ce moment, il peut faire son mouvement (choisir la connexion qu'il souhaite effectuer') et on l'enlève de la liste des joueur qui voivent jouer. 
		Association =[] # on assure que liste est vide.
		Playing_nodes = who_play(List_nodes_to_play)
		for node in Playing_nodes:
			connect_to = connection_choice(G,Playing_nodes)[0] # il faut compléter la fonction connection_choice pour créer la connection entre deux noeuds
			Association.append([node,connect_to])
			List_nodes_to_play.remove(node) #on enlève un noeuds quand il a joué
		create_connection(G,Association) # on crée les association choisis lors du tour.
		for node in List_node:
			node.updateValue()# on mets à jour les valeurs
	return G

print(f'nuber of edges : {game().number_of_edges()}')

		

