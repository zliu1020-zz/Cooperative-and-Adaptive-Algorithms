import csv
import random 

def get_cost(current_solution):
    cost = 0
    for i in range(20):
        for j in range(i+1, 20):
            cost += int(distance_matrix[i][j]) * int(flow_matrix[current_solution[i] - 1][current_solution[j] - 1])
    return cost

def update_tabu_structure():
    global tabu_structure
    for i in range(20):
        for j in range(20):
            if tabu_structure[i][j] > 0:
                tabu_structure[i][j] -= 1

def generate_neighbors(initial_solution):
    neighbors = list()
    best_cost = get_cost(initial_solution)
    
    for i in range(20):
        for j in range(i+1, 20):
            current_solution = initial_solution[:]
            current_solution[i], current_solution[j] = current_solution[j], current_solution[i]
            current_cost = get_cost(current_solution)
            neighbors.append({
                "i": i,
                "j": j,
                "cost": current_cost
            })
    
    neighbors.sort(key=lambda x:x["cost"])
    return neighbors

def get_best_neighbor(neighbors, current_solution, current_cost, best_cost):
    global tabu_structure
    for neighbor in neighbors:
        idx_i = neighbor["i"]
        idx_j = neighbor["j"]
        cost = neighbor["cost"]
        # if the best solution is not a tabu or it's a tabu but improving:
        # also skip solutions that have been used for a certain number of times to force diversification
        if (cost < best_cost) or (tabu_structure[idx_i][idx_j] == 0 and ((diversification_switch is False) or (tabu_structure[idx_j][idx_i] < diversification_bound))):
            # increment corresponding entry in recency based memeory
            tabu_structure[idx_i][idx_j] = tabu_size
            # increment corresponding entry in frequency based memeory for diversification purpose
            tabu_structure[idx_j][idx_i] += 1
            # copy the initial solution and swap as the neighbor suggests
            best_solution = current_solution[:]
            best_solution[idx_i], best_solution[idx_j] = current_solution[idx_j], current_solution[idx_i]
            return {
                "solution": best_solution,
                "idx_i": neighbor["i"],
                "idx_j": neighbor["j"],
                "cost": neighbor["cost"]
            }
        

def tabu_search():
    current_solution = initial_solution
    current_cost = get_cost(initial_solution)
    best_solution = initial_solution
    best_cost = current_cost
    iterations = 0 
    global tabu_size
    
    while iterations < 1000 and best_cost > 1285: 
#  ----- Uncomment the following lines to enable dynamic tabu list size --------        
#        if iterations > 0 and iterations % 100 == 0:
#            tabu_size = random.randint(1, 30)  
#            print("At iteration", iterations, ", tabu_size is changed to" , tabu_size)
        
        neighbors = generate_neighbors(current_solution)
        best_neighbor = get_best_neighbor(neighbors, current_solution, current_cost, best_cost)
        
        current_solution = best_neighbor["solution"][:]
        current_cost = best_neighbor["cost"]
        if current_cost < best_cost:
            best_cost = current_cost
            best_solution = current_solution
        
        iterations += 1
        # decrement existing tabu entries
        update_tabu_structure()

    print({
        "best_solution": best_solution,
        "best_cost": best_cost,
        "iteration": iterations
    })
    
diversification_switch = True 
diversification_bound = 5
tabu_size = 10 
distance_matrix = list()
flow_matrix = list()
tabu_structure = [[0 for x in range(20)] for y in range(20)]
initial_solution =[16, 7, 5, 2, 15, 6, 19, 8, 4, 20, 1, 11, 18, 10, 9, 13, 14, 12, 3, 17]
#  ----- Uncomment the following lines to enable random initial solutions --------     
#initial_solution = [(x+1) for x in range(20)]
#random.shuffle(initial_solution)

print({
    "initial_solution": initial_solution
})


with open('Distance.csv', newline='') as distance_csv:
    distance_matrix = list(csv.reader(distance_csv))
with open('Flow.csv', newline='') as flow_csv:
    flow_matrix = list(csv.reader(flow_csv))
    
tabu_search()

