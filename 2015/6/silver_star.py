class Light:
    def __init__(self):
        self.state = False

    def toggle(self):
        self.state = not self.state

    def turn_on(self):
        self.state = True

    def turn_off(self):
        self.state = False

    def __str__(self) -> str:
        return "1" if self.state else "0"
    
    def __repr__(self) -> str:
        return "1" if self.state else "0"

lights = [[Light() for i in range(1000)] for j in range(1000)]

with open("2015/day6/input.txt") as f:
    for line in f:
        line = line.strip()
        end = line.split(" ")
        start = end[2].split(",")
        finish = end[4].split(",")
        x_start = int(start[0])
        x_finish = int(finish[0])
        y_start = int(start[1])
        y_finish = int(finish[1])
        if line.startswith("turn on"):
            for i in range(x_start, x_finish + 1):
                for j in range(y_start, y_finish + 1):
                    lights[i][j].turn_on()
        elif line.startswith("turn off"):
            for i in range(x_start, x_finish + 1):
                for j in range(y_start, y_finish + 1):
                    lights[i][j].turn_off()
        elif line.startswith("toggle"):
            for i in range(x_start, x_finish + 1):
                for j in range(y_start, y_finish + 1):
                    lights[i][j].toggle()

count = 0
for i in range(1000):
    for j in range(1000):
        if lights[i][j].state:
            count += 1
print(count)
            

    