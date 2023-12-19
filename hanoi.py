class Hanoi:
    def __init__(self, n):
        self.n = n
        self.towers = [[], [], []]
        self.towers[0] = range(n, 0, -1)

    def move(self, src, dst):
        if len(self.towers[src]) == 0:
            return
        if len(self.towers[dst]) == 0 or self.towers[src][-1] < self.towers[dst][-1]:
            self.towers[dst].append(self.towers[src].pop())

    def solve(self):
        if self.n % 2 == 0:
            self.move(0, 1)
        else:
            self.move(0, 2)
        while len(self.towers[2]) < self.n:
            self.move(0, 1)
            self.move(0, 2)
            self.move(1, 2)

    def __str__(self):
        return str(self.towers)
    