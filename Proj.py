import networkx as nx
import time
import random
G = nx.Graph()
Liste_nodes = range(10000)
G.add_nodes_from(Liste_nodes)

def random_asso(p): # on crée une fonction pour associé chaque noeuds selon la probe P
	G = nx.Graph()
	Liste_nodes = list(range(10000))
	Liste_nodes_no_visited = Liste_nodes[0:] #on stocke la liste des noeuds à visiter
	G.add_nodes_from(Liste_nodes)
	print(G.number_of_nodes())
	for node in Liste_nodes:
		Liste_nodes_no_visited.remove(node) # on enlève le noeuds qu'on est en train de traiter
		for node_asso in Liste_nodes_no_visited: #on parcours la liste des noeuds à visiter
			choix = random.choices([0,1],weights= [1-p,p] ) # on tire avec une probabilité de p l'événement je me connecte au noeud node que je visite
			if choix ==[1]:
				G.add_edge(node, node_asso)
	print(f'nbre arrete = {G.number_of_edges()} nb noeuds = {G.number_of_nodes()}')
	return G

def all_node(n):#on trace n graphe avec une probabilité variant de 1/n à 1
	start_prob = 1/n
	Liste_graph=[random_asso(start_prob * k) for k in range(1,n+1)]
	print(f"il y a {len(Liste_graph)} graphe")	
tp = time.time()
all_node(15)
print(f"ça à pris {time.time()- tp}")
