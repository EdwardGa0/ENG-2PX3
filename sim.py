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
    
    def exit(self):
        for quarter_index, quarter in enumerate(roundabout.quarters):
            if quarter[0] == quarter_index:
                quarter.popleft()
    
    def update(self):
        # Front car either exits, or moves to next quarter
        # Try to enter car(s)
        pass

    def display(self):
        # Print out the timestamp and self.quarters
        pass

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

cars = []
for i in range(n):
    entry_time, entry_dir, exit_dir = input().split()
    cars.append((int(entry_time), entry_dir, exit_dir))

cars.sort()

time = 0
car_index = 0

while car_index < n or any(roundabout.quarters):
    roundabout.exit()
    roundabout.update()
    roundabout.display()
    time += 1
