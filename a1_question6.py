class Node():
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.route = []
        self.cost = 0

def coordinate_to_str(x, y):
    # flip x and y here to suit the question 
    return '(' + str(y) + ', ' + str(x) + ')'

def is_destination(node, destination):
    return (not node is None) and node.x == destination[0] and node.y == destination[1]

def is_obstacle(node, maze):
    return maze[node.x][node.y] == 1

def is_out_of_maze(node, maze):
    return node.x < 0 or node.x >= len(maze) or node.y < 0 or node.y >= len(maze)

def has_been_visited(node, visited):
    return visited[node.x][node.y] == 1

def visit(source_node, direction, maze, visited):
    if direction == 'Up':
        new_x = source_node.x - 1
        new_y = source_node.y
    elif direction == 'Down':
        new_x = source_node.x + 1
        new_y = source_node.y
    elif direction == 'Left':
        new_x = source_node.x
        new_y = source_node.y - 1
    elif direction == 'Right':
        new_x = source_node.x 
        new_y = source_node.y + 1
    
    new_node = Node(new_x, new_y)
    copied_route = list(source_node.route)
    copied_route.append(coordinate_to_str(new_x, new_y));
    new_node.route = copied_route
    new_node.cost = len(new_node.route)
    
    if (not is_out_of_maze(new_node, maze)) and (not is_obstacle(new_node, maze)) and (not has_been_visited(new_node, visited)):
        visited[new_node.x][new_node.y] = 1
        return new_node  


def run(current_node, destination, maze, direction, open_queue, visited, number_node_explored):
    result = visit(current_node, direction, maze, visited)
    if is_destination(result, destination):
        print("Route = " + str(result.route))
        print("Cost = " + str(result.cost))
        print("Number of Nodes Explored = " + str(number_node_explored))
        print("--------------------------------------------------------");
    elif not(result is None):
        open_queue.append(result)


def breadth_first_search(source, destination, maze):
    print("BFS from " + coordinate_to_str(source[0], source[1]) + " to " + coordinate_to_str(destination[0], destination[1]))
    visited = [[0 for i in range(25)] for j in range(25)]
    starting_node = Node(source[0], source[1])
    starting_node.route.append(coordinate_to_str(source[0], source[1]))
    open_queue = [starting_node]
    number_node_explored = 0;

    while open_queue:
        number_node_explored += 1
        current_node = open_queue.pop(0)
        run(current_node, destination, maze, 'Up', open_queue, visited, number_node_explored)
        run(current_node, destination, maze, 'Down', open_queue, visited, number_node_explored)
        run(current_node, destination, maze, 'Left', open_queue, visited, number_node_explored)
        run(current_node, destination, maze, 'Right', open_queue, visited, number_node_explored)

class DFSResult():
    def __init__(self, found, node):
        self.found = found
        self.node = node
        
def dfs_run(current_node, destination, maze, visited):
    global dfs_num_node_explored
    if is_destination(current_node, destination):
        dfs_num_node_explored += 1
        result = DFSResult(True, current_node)
        return result
    
    if has_been_visited(current_node, visited):
        result = DFSResult(False, None, number_node_explored)
        return result
    else:
        visited[current_node.x][current_node.y] = 1
        dfs_num_node_explored += 1
        # down 
        down_x = current_node.x + 1
        down_y = current_node.y
        copied_route = list(current_node.route)
        copied_route.append(coordinate_to_str(down_x, down_y));
        down_node = Node(down_x, down_y)
        down_node.route = copied_route
        down_node.cost = len(down_node.route)
      
        if (not is_out_of_maze(down_node, maze)) and (not is_obstacle(down_node, maze)) and (not has_been_visited(down_node, visited)):
            down_result = dfs_run(down_node, destination, maze, visited)
            if down_result.found is True:
                return down_result
        
        # Right 
        right_x = current_node.x
        right_y = current_node.y + 1
        copied_route = list(current_node.route)
        copied_route.append(coordinate_to_str(right_x, right_y))
        right_node = Node(right_x, right_y)
        right_node.route = copied_route
        right_node.cost = len(right_node.route)
      
        if (not is_out_of_maze(right_node, maze)) and (not is_obstacle(right_node, maze)) and (not has_been_visited(right_node, visited)):
            right_result = dfs_run(right_node, destination, maze, visited)
            if right_result.found is True:
                return right_result
        
        # Up 
        up_x = current_node.x - 1
        up_y = current_node.y
        copied_route = list(current_node.route)
        copied_route.append(coordinate_to_str(up_x, up_y))
        up_node = Node(up_x, up_y)
        up_node.route = copied_route
        up_node.cost = len(up_node.route)
      
        if (not is_out_of_maze(up_node, maze)) and (not is_obstacle(up_node, maze)) and (not has_been_visited(up_node, visited)):
            up_result = dfs_run(up_node, destination, maze, visited)
            if up_result.found is True:
                return up_result
            
        # Left 
        left_x = current_node.x 
        left_y = current_node.y - 1
        copied_route = list(current_node.route)
        copied_route.append(coordinate_to_str(left_x, left_y))
        left_node = Node(left_x, left_y)
        left_node.route = copied_route
        left_node.cost = len(left_node.route)
      
        if (not is_out_of_maze(left_node, maze)) and (not is_obstacle(left_node, maze)) and (not has_been_visited(left_node, visited)):
            left_result = dfs_run(left_node, destination, maze, visited)
            if left_result.found is True:
                return left_result
            
    result = DFSResult(False, None)
    return result
    

def depth_first_search(source, destination, maze):
    global dfs_num_node_explored
    dfs_num_node_explored = 0
    print("DFS from " + coordinate_to_str(source[0], source[1]) + " to " + coordinate_to_str(destination[0], destination[1]))
    visited = [[0 for i in range(25)] for j in range(25)]
    
    starting_node = Node(source[0], source[1])
    starting_node.route.append(coordinate_to_str(source[0], source[1]))  
    
    number_node_explored = 0
    final_result = dfs_run(starting_node, destination, maze, visited)
    if final_result.found is True:
        print("Route = " + str(final_result.node.route))
        print("Cost = " + str(final_result.node.cost))
        print("Number of Nodes Explored = " + str(dfs_num_node_explored))
        print("--------------------------------------------------------");
    else:
        print("DFS failed to find a path")

class AStarNode():
    def __init__(self, parent, x, y):
        self.parent = parent
        self.x = x
        self.y = y
        self.g = 0
        self.h = 0
        self.f = 0
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __ne__(self, other):
        return self.x != other.x or self.y != other.y
    def __cmp__(self, other):
        return self.x > other.x and self.y > other.y
    def manhattan_distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)
    def update(self, lower_g, ending_node):
        self.g = lower_g + 1
        self.h = self.manhattan_distance(ending_node)
        self.f = self.g + self.h
        
def build_neighbors(best_node, maze):
    up_node = AStarNode(best_node, best_node.x-1, best_node.y)
    down_node = AStarNode(best_node, best_node.x+1, best_node.y)
    left_node = AStarNode(best_node, best_node.x, best_node.y-1)
    right_node = AStarNode(best_node, best_node.x, best_node.y+1)
    neighbors = []
    if (not is_out_of_maze(up_node, maze)) and (not is_obstacle(up_node, maze)):
        neighbors.append(up_node)
            
    if (not is_out_of_maze(down_node, maze)) and (not is_obstacle(down_node, maze)):
        neighbors.append(down_node)
            
    if (not is_out_of_maze(left_node, maze)) and (not is_obstacle(left_node, maze)):
        neighbors.append(left_node)
            
    if (not is_out_of_maze(right_node, maze)) and (not is_obstacle(right_node, maze)):
        neighbors.append(right_node)
        
    return neighbors;

def a_star_search(source, destination, maze):
    print("A* search from " + coordinate_to_str(source[0], source[1]) + " to " + coordinate_to_str(destination[0], destination[1]))
    
    starting_node = AStarNode(None, source[0], source[1])
    ending_node = AStarNode(None, destination[0], destination[1])
    open_queue = []
    open_queue.append(starting_node)
    closed_queue = []
    number_node_explored = 0
    
    while open_queue:
        # find the node with the smallest f
        best_node = open_queue[0]
        best_idx = 0
        idx = 0
        while idx < len(open_queue):
            current_node = open_queue[idx]
            if current_node.f < best_node.f:
                best_node = current_node
                best_idx = idx
            idx+=1
        
        if is_destination(best_node, destination):
            resultant_route = []
            pointer = best_node
            while pointer is not None:
                resultant_route.append(coordinate_to_str(pointer.x, pointer.y))
                pointer = pointer.parent
            resultant_route.reverse()
            print("Route = " + str(resultant_route))
            print("Cost = " + str(len(resultant_route)))
            print("Number of Nodes Explored = " + str(number_node_explored))
            print("--------------------------------------------------------");
            return
        else:  
            number_node_explored += 1
            open_queue.pop(best_idx)
            closed_queue.append(best_node)
            neighbors = build_neighbors(best_node, maze)
            
            for current_neighbor in neighbors:
                if current_neighbor in closed_queue and current_neighbor.g < best_node.g:
                    current_neighbor.update(current_neighbor.g, ending_node)
                    best_node = current_neighbor.parent 
                elif current_neighbor in open_queue and current_neighbor.g > best_node.g:
                    current_neighbor.update(best_node.g, ending_node)
                    current_neighbor.parent = best_node
                elif (current_neighbor not in closed_queue) and (current_neighbor not in open_queue):
                    current_neighbor.update(best_node.g, ending_node)
                    open_queue.append(current_neighbor)
    


sample_maze = [
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,1,1,0,0,0,0,0],
[0,0,0,0,0,0,1,1,0,0,1,1,1,0,0,0,0,0,1,1,0,0,0,0,0],
[1,1,1,0,0,0,1,1,0,0,1,1,1,0,0,0,0,0,1,1,0,0,0,0,0],
[1,1,1,0,0,0,1,1,0,0,1,1,1,0,0,0,0,0,1,1,1,1,0,0,0],
[0,0,1,0,0,0,1,1,0,0,1,1,1,0,0,0,0,0,1,1,1,1,1,1,0],
[0,0,1,1,1,0,1,1,0,0,1,1,1,0,0,0,0,0,1,0,0,0,0,0,0],
[0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,0,1,0,0,0],
[0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,0,1,0,0,0],
[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,1,0,1,0,0,1,0,0,1],
[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,1,0,0,0,0,1,1,1,1],
[0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,1,1,0,0,0,0,0,1,1,1],
[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,1,1,1,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,1,1,1,0,0,0,1,1,1,1,1,1,1,0,0,0,0],
[0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,1,1,1,0,0,1,1,1,0,0,0,1,1,1,1,1,1,1,0,0,0,0],
[0,0,0,1,1,1,0,0,1,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0],
[1,1,1,1,1,0,0,0,1,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0],
[1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0],
]
dfs_num_node_explored = 0
breadth_first_search([11,2], [19,23], sample_maze)
breadth_first_search([11,2], [21,2], sample_maze)
breadth_first_search([0,0], [24,24], sample_maze)
depth_first_search([11,2], [19,23], sample_maze)
depth_first_search([11,2], [21,2], sample_maze)
depth_first_search([0,0], [24,24], sample_maze)
a_star_search([11,2], [19,23], sample_maze)
a_star_search([11,2], [21,2], sample_maze)
a_star_search([0,0], [24,24], sample_maze)