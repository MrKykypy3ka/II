from random import *
import math

class Perceptron:
    def __init__(self):
        self.T = 0.5
        self.patterns = [[0, 0],
                         [0, 1],
                         [1, 0],
                         [1, 1]]
        self.answers = [0, 0, 0, 1]
        self.steps = 0

    def countOut(self):
        self.out = 0
        for i in range(len(self.enters)):
            self.out += self.enters[i] * self.synapses[i]
        if self.out > self.T:
            self.out = 1
        else:
            self.out = 0

    def study(self):
        for i in range(len(self.enters)):
            self.synapses[i] = 0.2 * random() + 0.1

        gErr = None
        while gErr != 0:
            self.steps += 1
            gErr = 0.0
            for p in range(len(self.patterns)):
                for i in range(len(self.enters)):
                    self.enters[i] = self.patterns[p][i]
                self.countOut()
                error = self.answers[p] - self.out
                gErr += math.fabs(error)
                for i in range(len(self.synapses)):
                    self.synapses[i] += 0.1 * error * self.enters[i]
        return self.steps

    def test(self):
        self.enters = [0 for _ in range(len(self.patterns[0]))]
        self.synapses = [0 for _ in range(len(self.enters))]

        self.study()
        print(f'steps: {self.steps}')
        for p in range(len(self.patterns)):
            for i in range(len(self.enters)):
                self.enters[i] = self.patterns[p][i]
            self.countOut()
            print(f'out_{p + 1}: {self.out}')

def main():
    logic_and = Perceptron()
    logic_and.test()


if __name__ == "__main__":
    main()