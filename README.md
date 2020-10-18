This code was based on a_star_algorithm from https://github.com/tjazerzen.

Código alterado para a resolução da questão da matéria de inteligência artificial da Unisociesc - 2020/2
Editado por: Emanoel Alves Junior
Busca A* para encontrar o menor caminho entre duas cidades de Santa Catarina, próximas a florianópolis.


# a_star_algorithm
Implementation of A* algorithm in python

- Helper functions.py: Few functions to determine heuristic distance values between to adjacent nodes.
- A_star_algorithm.py: The core of this repository, shortest path is calculated here and the list of path returned.
- positions.txt: a text file with the information of node possition in coordinate system. The map is made out of 15 nodes (I mark them 0-14) and each of those nodes has latitude and longitude coordinates written in its own line. 1 is the maximum value of this coordinate system
- Adjacency_list.txt: There's 15 lines in text file but this time each line holds the information of the node's adjacent nodes.
- run.py: run program.

# Reference
Tjaž Eržen
- LinkedIn: https://www.linkedin.com/in/tjaz-erzen-688aa1190/
- Github: https://github.com/tjazerzen

