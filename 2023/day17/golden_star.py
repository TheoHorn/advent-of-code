from heapq import heappop, heappush


def find_path(data):
    max_y = len(data)
    max_x = len(data[0])

    start = (0, 0)
    end = (max_y - 1, max_x - 1)

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    visited = {} 

    priority_q = [(0, start, -1, 0)]

    while priority_q:
        loss, pos, current_direction, number_steps = heappop(priority_q)
        if pos == end:
            return loss

        good_directions = []
        for direction in range(4):
            if direction != current_direction and (direction + 2) % 4 != current_direction:
                good_directions.append(direction)
    
        
        for direction in good_directions:
            next_loss = loss
            for consecutive_step in range(1, 11):
                next_position_list = []

                for coord, direction_vector in zip(pos, directions[direction]):
                    next_position_list.append(coord + direction_vector * consecutive_step)
                next_position = tuple(next_position_list)

                if 0 <= next_position[0] < max_y and 0 <= next_position[1] < max_x:
                    next_loss += int(data[next_position[0]][next_position[1]])
                    
                    if next_loss < visited.get((next_position, direction), float('inf')):
                        visited[(next_position, direction)] = next_loss
                        
                        if consecutive_step >= 4:
                            heappush(priority_q, (next_loss, next_position, direction, consecutive_step))
            
    

with open("2023/day17/input.txt") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    print(find_path(lines))
