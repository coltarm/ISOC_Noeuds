Fichier dans lequelle on peut expliquer ce qu'on a fait et comment ça fonctionne

## Random Graph
Dans cette partie on nous demande à partir de quelle valeur de P tous les graphes sont interconnecté.(Pour comprendre de quoi je parle plus précisément cf sujet ISOC envoyé par mail)

Réalisation code : 
On crée une fonction "randon-asso" qui prend en argument P la probabilité que le noeuds se connecte à chacun des autres  noeuds. 
Cette fonction commence commence par crée 10 000 noeuds dans un graph G. 
Dans cette fonction on cherche à relier deux noeuds quelquonque suivant la probabilité P. Pour cela je dois parcourir deux fois la liste des noeuds, mais si on fait ça simplement alors on affecte une fois 1 et 10 selon la probabilité P et après on rééfecturas la même action quand nous nous occuperons de la liaison de 10 avec les autres noeuds.
Pour cela on définit une liste Liste_nodes_no_visited qui définieras les noeuds que l'on doit possiblement affecter à 10 par exemple. 

On boucle deux fois la première est pour choisir le noeuds auquel on va regarder les association.
On enlève ce noeuds de la liste des noeuds à visiter parce que on ne souhaite pas associer un noeuds sur lui même.
On parcours les noeuds à visiter et on utilise la fonction choice de la bibliothéque python pour tirer 1 ou 0 selon la probe P, 1 représente la liaison au noeuds que l'on visite.

Et à la fin on retourne Le graphe.

On réalise ensuite la fonction all_node qui va se charger de créer 100 graphe de 10 000 noeuds on on incrémente la probabilité de P de 0.01 de liaison entre deux noeuds quelquonque dans le graphe.

### Continuation
Il faut vérifier que le programme existant fait bien ce qu'on lui demande, si il y un problème de cohérence c'est probablement la fonction choice de random.

Il faut déterminer la taille du plus gros connected component(Pas sûr ce que c'est, possiblement le plus gros enseble de noeuds interconnecté ).

## Simple Graph
Dans cette partie je me référe à un noeuds par joueur parce que c'est censé être un jeu, donc permet d'éviter les répétitions. le joueur ce référe généralement au noeuds qui décident à quelle noeuds doit-il se relier.

Pour le Simple Graph name on doit stocker plusieur information sur un noeuds Sa valeur N(v), le temps auquel il joue, j'ai donc crée une classe.

On commence par définir une fonction create_graph qui prend en argument n le nombre de noeuds que l'on souhaite créer.

Pour connaître à qui sera le prochain tour, on crée une fonction who_play() qui prend en argument les noeuds qui doivent jouer. 
On défini une liste Node_smalles_time qui stockera les joueur qui doivent jouer au prochain tour. On définie ensuite la variable du plus petit temps, le critère selon lequel on choisit le prochain qui joue.
On parcours la liste des noeuds et on récupère les prochain joueurs. que l'on retourne à la fin de la fonction

J'ai construit le squelette de la fonction game, la fonction qui effectueras les actions de jeux. 

###Continuation
Il faut faire compléter la fonction connection_choice, qui doit servir à décidé sur quelle noeuds doit se connecter le joueur
Il faut ensuite compléter la fonction et game.

### prédictions sur cette partie
Les noeuds se regrouperons probablement sur quelque noeuds majoritaire. puisque pour se maximiser je vais chercher le noeuds avec les noeuds avec le plus de connection et il y aura donc probablement une centrallisation sur quelque noeuds.
