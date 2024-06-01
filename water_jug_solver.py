class WaterJugSolver:
    def __init__(self):
        self.three_gallon = 0
        self.five_gallon = 0
        self.steps = []

    def fill_three_gallon(self):
        self.three_gallon = 3
        self.log_step()

    def fill_five_gallon(self):
        self.five_gallon = 5
        self.log_step()

    def empty_three_gallon(self):
        self.three_gallon = 0
        self.log_step()

    def empty_five_gallon(self):
        self.five_gallon = 0
        self.log_step()

    def pour_three_to_five(self):
        total = self.three_gallon + self.five_gallon
        if total <= 5:
            self.five_gallon = total
            self.three_gallon = 0
        else:
            self.three_gallon = total - 5
            self.five_gallon = 5
        self.log_step()

    def pour_five_to_three(self):
        total = self.five_gallon + self.three_gallon
        if total <= 3:
            self.three_gallon = total
            self.five_gallon = 0
        else:
            self.five_gallon = total - 3
            self.three_gallon = 3
        self.log_step()

    def log_step(self):
        self.steps.append((self.three_gallon, self.five_gallon))

    def solve(self):
        self.fill_three_gallon()
        self.pour_three_to_five()
        self.fill_three_gallon()
        self.pour_three_to_five()
        self.empty_five_gallon()
        self.pour_three_to_five()
        self.fill_three_gallon()
        self.pour_three_to_five()
        
        for i, step in enumerate(self.steps):
            print(f"Step {i+1}: 3-gallon = {step[0]}, 5-gallon = {step[1]}")
        
        if 4 in [self.three_gallon, self.five_gallon]:
            print("Successfully measured 4 gallons!")
        else:
            print("Failed to measure 4 gallons.")

if __name__ == "__main__":
    solver = WaterJugSolver()
    solver.solve()
