from collections import deque

class Roundabout:
    def __init__(self, size):
        self.size = size
        self.quarters = [
            deque() for _ in range(4)
        ]
        
    def can_enter(self, direction):
        quarter_index = self._direction_to_quarter_index(direction)
        return len(self.quarters[quarter_index]) < self.size // 4
    
    def enter(self, enter_dir, exit_dir):
        quarter_index = self._direction_to_quarter_index(enter_dir)
        # Store the exit direction in quarters
        self.quarters[quarter_index].append(self._direction_to_quarter_index(exit_dir))  
    
    def update(self):
        for quarter_index, quarter in enumerate(roundabout.quarters):
            if quarter:
                first = quarter.popleft()
                if first != quarter_index:
                    # Move first to next quarter
                    roundabout.quarters[quarter_index - 1].append(first)


    def display(self, time):
        print('t =', time, 'N:', list(self.quarters[0]), 'E:', list(self.quarters[1]), 'S:', list(self.quarters[2]), 'W:', list(self.quarters[3]))

    def _direction_to_quarter_index(self, direction):
        if direction == 'N':
            return 0
        elif direction == 'E':
            return 1
        elif direction == 'S':
            return 2
        elif direction == 'W':
            return 3

size = int(input())
n = int(input())

roundabout = Roundabout(size)

cars = deque()
for i in range(n):
    entry_time, entry_dir, exit_dir = input().split()
    cars.append((int(entry_time), entry_dir, exit_dir))

time = 0

while cars or any(roundabout.quarters):
    roundabout.update()
    car_index = 0
    # loop through waiting cars based on arrival time
    while car_index < len(cars) and time >= cars[car_index][0]:
        if roundabout.can_enter(cars[car_index][1]):
            roundabout.enter(cars[car_index][1], cars[car_index][2])
            del cars[car_index]
        else:
            car_index += 1
    roundabout.display(time)
    time += 1
