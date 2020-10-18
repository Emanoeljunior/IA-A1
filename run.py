import matplotlib.pyplot as plt
from a_star_algorithm import shortest_path

# Getting the coordinates of each point from position.txt and then creating a dictionary with them
coordinates_file = open("positions.txt", "r")
coordinates = dict()
coordinates_lines = coordinates_file.readlines()
for index, line in enumerate(coordinates_lines):
    new_line = line.split(' ')
    new_line[1] = new_line[1][:len(new_line[1])-1]
    for i in range(2):
        new_line[i] = float(new_line[i])
    coordinates[index] = new_line
coordinates_file.close()


# Getting the adjacency list of each node from adjacency_list.txt
# Creating 2D list out of adjacency list of lenght 15, which is the number of nodes in the the graph
adjacency_file = open("adjacency_list.txt", "r")
adjacency_list = list()
adjacency_lines = adjacency_file.readlines()
for line in adjacency_lines:
    line = line.split(' ')
    line = line[:len(line)-1]
    for i in range(len(line)):
        line[i] = int(line[i])
    adjacency_list.append(line)
adjacency_file.close()

print("Destino - Florianópolis")
print("1 - São José ")
print("2 - Palhoça ")
print("3 - Biguaçu ")
print("4 - Gov. Celso Ramos ")
print("5 - Tijucas ")
print("6 - Canelinha ")
print("7 - São Jão Batista ")
print("8 - Major Gercino ")
print("9 - Antônio Carlos ")
print("10 - Angelina ")
print("11 - Rancho Queimado ")
print("12 - Águas Mornas ")
print("13 - São Pedro Alcântara ")
print("14 - Santo Amaro Imperatriz ")
city = int(input("Escolha o número da cidade de partida:"))
# Start and th end 
start_end = [
    (city, 0)
]

# Test function for your test purposes
def test(shortest_path_function):
    for start, goal in start_end:
        path = shortest_path_function( adjacency_list, start, goal)
        print("Partida:", start,
                "Destino:",      goal,
                "Seu caminho:", path)
    return path

# run algorithm
path = test(shortest_path)

# print path
ansx=[]
ansy=[]
for j in path:
    ansx.append(coordinates[j][0])
    ansy.append(coordinates[j][1])

# print other points   
x=[]
y=[]
for i in range(0,14):
    x.append(coordinates[i][0])
    y.append(coordinates[i][1])

plt.plot(y,x,"o")
plt.plot(ansy, ansx)
plt.xlabel("Longitude")
plt.ylabel("Latitude")
for i in range(14):
    plt.annotate(i,(y[i], x[i]),(y[i]+0.01, x[i]+0.01))
plt.show()
