def print_board(elements):
    for i in range(9):
        if i % 3 == 0:
            print()
        if elements[i] == -1:
            print("_", end=" ")
        else:
            print(elements[i], end=" ")
    print()

def solvable(start):
    inv = 0
    for i in range(9):
        if start[i] == -1:
            blank_row = i // 3
            continue
        for j in range(i + 1, 9):
            if start[j] == -1:
                continue
            if start[i] > start[j]:
                inv += 1
    return (inv + blank_row) % 2 == 1  # Adjusted solvability condition

def manhattan_distance(start, goal):
    distance = 0
    for i in range(9):
        if start[i] == -1:
            continue
        goal_pos = goal.index(start[i])
        distance += abs(i // 3 - goal_pos // 3) + abs(i % 3 - goal_pos % 3)
    return distance

def moveleft(start, position):
    start[position], start[position - 1] = start[position - 1], start[position]

def moveright(start, position):
    start[position], start[position + 1] = start[position + 1], start[position]

def moveup(start, position):
    start[position], start[position - 3] = start[position - 3], start[position]

def movedown(start, position):
    start[position], start[position + 3] = start[position + 3], start[position]

def movetile(start, goal):
    emptyat = start.index(-1)
    row = emptyat // 3
    col = emptyat % 3
    t1, t2, t3, t4 = start[:], start[:], start[:], start[:]
    f1 = f2 = f3 = f4 = float('inf')

    if col - 1 >= 0:
        moveleft(t1, emptyat)
        f1 = manhattan_distance(t1, goal)
    if col + 1 < 3:
        moveright(t2, emptyat)
        f2 = manhattan_distance(t2, goal)
    if row + 1 < 3:
        movedown(t3, emptyat)
        f3 = manhattan_distance(t3, goal)
    if row - 1 >= 0:
        moveup(t4, emptyat)
        f4 = manhattan_distance(t4, goal)

    min_heuristic = min(f1, f2, f3, f4)

    if f1 == min_heuristic:
        moveleft(start, emptyat)
    elif f2 == min_heuristic:
        moveright(start, emptyat)
    elif f3 == min_heuristic:
        movedown(start, emptyat)
    elif f4 == min_heuristic:
        moveup(start, emptyat)

def solveEight(start, goal):
    global g
    if start == goal:
        print("Solved in {} moves".format(g))
        print_board(start)
        return
    g += 1
    movetile(start, goal)
    print_board(start)
    solveEight(start, goal)

def main():
    global g
    g = 0  # Reset global move counter
    start = []
    goal = []

    print("Enter the start state row-wise (3 numbers per line, -1 for blank):")
    for _ in range(3):
        start.extend(list(map(int, input().split())))

    print("Enter the goal state row-wise (3 numbers per line, -1 for blank):")
    for _ in range(3):
        goal.extend(list(map(int, input().split())))

    print("\nInitial Board:")
    print_board(start)

    if solvable(start):
        print("\nSolving...")
        solveEight(start, goal)
    else:
        print("\nNot possible to solve")

if __name__ == '__main__':
    main()

# Start State - 
# 2 8 3 
# 1 6 4 
# 7 -1 5

# Goal State
# 1 2 3 
# 8 -1 4 
# 7 6 5 