class Animal:
    def __init__(self, name):
        self.name = name
    alive = True # Атрибут "Живой".
    fed = False # Атрибут "Сытый (накормленный)."


class Plant:
    def __init__(self, name):
        self.name = name
    edible = False  # Атрибут "Съедобный".

class Flower(Plant):
    pass

class Fruit(Plant):
    edible = True

class Mammal(Animal):
    def eat(self, food):
        if isinstance(food, Plant):
            if food.edible == True:
                print(f'{self.name} съел {food.name}.')
                self.fed = True
                self.alive = True
            else:
                print(f'{self.name} не стал есть {food.name}.')
                self.alive = False
                self.fed = True
        else:
            print(f'Ошибка! {food} не относится к классу {Plant}! Внесите изменения в данные!')

class Predator(Animal):
    def eat(self, food):
        if isinstance(food, Plant):
            if food.edible == True:
                print(f'{self.name} съел {food.name}.')
                self.fed = True
                self.alive = True
            else:
                print(f'{self.name} не стал есть {food.name}.')
                self.alive = False
                self.fed = True
        else:
            print(f'Ошибка! {food} не относится к классу {Plant}! Внесите изменения в данные!')



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









