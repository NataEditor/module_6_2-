class Animal:
    """Класс животных с атрибутами alive = True(живой) и fed = False(накормленный),
    name - индивидуальное название каждого животного. """

    alive = True # живой
    fed = False  #накормленный

    def __init__(self, name):
        self.name = name


class Plant:
    """Класс растений атрибут edible = False(съедобность),
     name - индивидуальное название каждого растения. """
    edible = False

    def __init__(self, name):
        self.name = name


class Mammal(Animal):
    def eat(self, food):
        if food.edible == True:
            self.fed = True
            return f'{self.name}, съел {food.name}'
        else:
            self.alive = False
            return f'{self.name} не стал есть {food.name}'


class Predator(Animal):
    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False


class Flower(Plant):
    pass


class Fruit(Plant):
    edible = True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
