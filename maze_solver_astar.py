import heapq
# Heuristic Function
def heuristic(node, goal):
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

# A* Search Algorithm
def astar(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    open_list = []
    heapq.heappush(open_list, (0, start))
    came_from = {}
    g_cost = {start: 0}
 
  # Possible moves: Right, Down, Left, Up
    directions = [(0,1), (1,0), (0,-1), (-1,0)]
    while open_list:
        _, current = heapq.heappop(open_list)

        # Goal reached
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        for dx, dy in directions:
            neighbor = (current[0] + dx, current[1] + dy)

            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols:
                if maze[neighbor[0]][neighbor[1]] == 1:
                    continue

                new_g = g_cost[current] + 1

                if neighbor not in g_cost or new_g < g_cost[neighbor]:
                    g_cost[neighbor] = new_g
                    f_cost = new_g + heuristic(neighbor, goal)
                    heapq.heappush(open_list, (f_cost, neighbor))
                    came_from[neighbor] = current
    return None
# Main Function
def main():
    maze = [
        [0, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 0, 0, 0],
        [0, 1, 1, 0]
    ]

    start = (0, 0)
    goal = (3, 3)

    path = astar(maze, start, goal)

    if path:
        print("Shortest Path Found:")
        print(path)
      
        for r, c in path:
            maze[r][c] = "*"
        print("\nMaze with Path:")
        for row in maze:
            print(row)
    else:
        print("No path found.")
# Program Entry Point
if _name_ == "_main_":
    main()
