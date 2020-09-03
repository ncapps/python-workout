
class Animal():
    def __init__(self, color, number_of_legs):
        self.species = self.__class__.__name__
        self.color = color
        self.number_of_legs = number_of_legs

    def __repr__(self):
        return f'{self.color} {self.species}, {self.number_of_legs} legs'


class Wolf(Animal):
    def __init__(self, color):
        super().__init__(color, 4)


class Sheep(Animal):
    def __init__(self, color):
        super().__init__(color, 4)


class Snake(Animal):
    def __init__(self, color):
        super().__init__(color, 0)


class Parrot(Animal):
    def __init__(self, color):
        super().__init__(color, 2)


class Cage():
    def __init__(self, cage_id):
        self.cage_id = cage_id
        self.animals = []

    def add_animals(self, *animals):
        for one_animal in animals:
            self.animals.append(one_animal)

    def __repr__(self):
        output = f'Cage {self.cage_id}\n'
        output += '\n'.join('\t' + str(animal)
                            for animal in self.animals)

        return output


class Zoo():
    def __init__(self):
        self.cages = []

    def add_cages(self, *cages):
        for one_cage in cages:
            self.cages.append(one_cage)

    def animals_by_color(self, color):
        return "\n".join(str(animal)
                         for cage in self.cages
                         for animal in cage.animals
                         if animal.color == color)

    def animals_by_legs(self, number_of_legs):
        return "\n".join(str(animal)
                         for cage in self.cages
                         for animal in cage.animals
                         if animal.number_of_legs == number_of_legs)

    def number_of_legs(self):
        return sum(animal.number_of_legs
                   for cage in self.cages
                   for animal in cage.animals)

    def __repr__(self):
        return '\n'.join(str(cage) for cage in self.cages)


wolf = Wolf('black')
sheep = Sheep('white')
snake = Snake('brown')
parrot = Parrot('green')

# print(wolf)
# print(sheep)
# print(snake)
# print(parrot)

c1 = Cage(1)
c1.add_animals(wolf, sheep)

c2 = Cage(2)
c2.add_animals(snake, parrot)

# print(c1)
# print(c2)

zoo = Zoo()
zoo.add_cages(c1, c2)
print(zoo)
print(zoo.animals_by_color("white"))
print(zoo.animals_by_legs(4))
print(zoo.number_of_legs())
