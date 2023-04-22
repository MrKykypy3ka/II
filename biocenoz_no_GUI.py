import random


class LifeForm:
    def __init__(self, x, y, energy, speed):
        self.x = x
        self.y = y
        self.energy = energy
        self.speed = speed

    def move(self):
        dx = random.randint(-self.speed, self.speed)
        dy = random.randint(-self.speed, self.speed)
        self.x += dx
        self.y += dy
        self.energy -= 1

    def eat(self, food):
        self.energy += food.energy
        food.energy = 0


class Food:
    def __init__(self, x, y, energy):
        self.x = x
        self.y = y
        self.energy = energy


class Environment:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.food = []

    def add_food(self, food):
        self.food.append(food)

    def update(self, life_form):
        for food in self.food:
            if abs(life_form.x - food.x) <= 5 and abs(life_form.y - food.y) <= 5:
                life_form.eat(food)
                self.food.remove(food)
        life_form.move()
        if life_form.x < 0:
            life_form.x = 0
        elif life_form.x >= self.width:
            life_form.x = self.width - 1
        if life_form.y < 0:
            life_form.y = 0
        elif life_form.y >= self.height:
            life_form.y = self.height - 1


environment = Environment(50, 50)
life_forms = []
life_forms.append(LifeForm(25, 25, 10, 3))
life_forms.append(LifeForm(30, 30, 10, 3))
life_forms.append(LifeForm(35, 35, 10, 3))
for i in range(20):
    x = random.randint(0, environment.width - 1)
    y = random.randint(0, environment.height - 1)
    energy = random.randint(1, 5)
    food = Food(x, y, energy)
    environment.add_food(food)

for i in range(100):
    for life_form in life_forms:
        environment.update(life_form)
        print("Simulation finished.")
        print("Iteration:", i + 1)
        print("Life form energy:", life_form.energy)
        print("Number of food items:", len(environment.food))
        print()