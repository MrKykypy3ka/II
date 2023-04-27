import random
import math

INITIAL_PLANT_HEALTH = 100
INITIAL_HERBIVORE_HEALTH = 100
INITIAL_PREDATOR_HEALTH = 100

PLANT_GROWTH_RATE = 0.05
HERBIVORE_METABOLISM = 0.1
PREDATOR_METABOLISM = 0.2
PREDATOR_SPEED = 5


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx*dx + dy*dy)

    def move_towards(self, other, distance):
        if self.distance_to(other) < distance:
            self.x = other.x
            self.y = other.y
            return
        dx = other.x - self.x
        dy = other.y - self.y
        dist = math.sqrt(dx*dx + dy*dy)
        self.x += dx / dist * distance
        self.y += dy / dist * distance


class Plant:
    def __init__(self, position, health=INITIAL_PLANT_HEALTH):
        self.position = Position(*position)
        self.health = health

    def grow(self):
        self.health += PLANT_GROWTH_RATE

    def is_eaten(self):
        return self.health <= 0


class Herbivore:
    def __init__(self, position, health=INITIAL_HERBIVORE_HEALTH):
        self.position = Position(*position)
        self.health = health

    def move(self, plants):
        if not plants:
            return
        closest_plant = min(plants, key=lambda p: self.position.distance_to(p.position))
        self.position.move_towards(closest_plant.position, HERBIVORE_METABOLISM)
        self.health -= HERBIVORE_METABOLISM
        closest_plant.health -= HERBIVORE_METABOLISM
        if closest_plant.is_eaten():
            plants.remove(closest_plant)
            self.health += INITIAL_PLANT_HEALTH

    def is_dead(self):
        return self.health <= 0


class Predator:
    def __init__(self, position, health=INITIAL_PREDATOR_HEALTH):
        self.position = Position(*position)
        self.health = health

    def hunt(self, herbivores):
        closest_herbivore = None
        min_distance = float("inf")
        for herbivore in herbivores:
            distance = self.position.distance_to(herbivore.position)
            if distance < min_distance:
                closest_herbivore = herbivore
                min_distance = distance
        if closest_herbivore is not None:
            self.position.move_towards(closest_herbivore.position, PREDATOR_SPEED)
            self.health += closest_herbivore.health
            herbivores.remove(closest_herbivore)

    def is_dead(self):
        return self.health <= 0


import time


class Biosphere:
    def __init__(self, num_plants, num_herbivores, num_predators):
        self.plants = [Plant() for _ in range(num_plants)]
        self.herbivores = [Herbivore() for _ in range(num_herbivores)]
        self.predators = [Predator() for _ in range(num_predators)]
        self.tick_count = 0

    def run(self, num_ticks):
        for i in range(num_ticks):
            self.tick_count += 1
            self.update()
            self.display()
            time.sleep(0.1)

    def update(self):
        for plant in self.plants:
            plant.grow()

        for herbivore in self.herbivores:
            herbivore.eat(self.plants)
            herbivore.metabolize()

        for predator in self.predators:
            predator.hunt(self.herbivores)
            predator.metabolize()

    def display(self):
        print(f"Tick count: {self.tick_count}")
        print(f"Number of plants: {len(self.plants)}")
        print(f"Number of herbivores: {len(self.herbivores)}")
        print(f"Number of predators: {len(self.predators)}")
        print("=" * 30)



biosphere = Biosphere(num_plants=10, num_herbivores=5, num_predators=2)
biosphere.run(num_ticks=20)