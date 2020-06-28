from pprint import pprint


class Animal:
    feed = 'голоден/голодна'
    milk = 'не доена'
    eggs = 'яйца не собраны'
    talk = 'молчит'
    trim = 'не стрижен'

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def feed_animal(self):
        self.feed = 'сыт'

    def get_milk(self):
        self.milk = 'подоена'

    def get_eggs(self):
        self.eggs = 'яйца собраны'

    def get_overall_weight(self):
        weight_dict = {self.name: self.weight}
        return weight_dict


class Goose(Animal):

    def talking(self):
        self.talk = 'гогочет'


class Cow(Animal):

    def talking(self):
        self.talk = 'мычит'


class Sheep(Animal):

    def talking(self):
        self.talk = 'бебекает'


class Hen(Animal):

    def talking(self):
        self.talk = 'кудахчет'


class Goat(Animal):

    def talking(self):
        self.talk = 'мемекает'


class Duck(Animal):

    def talking(self):
        self.talk = 'крякает'


duck = Duck('Кряква', 1)

goose0 = Goose('Серый', 3)
goose1 = Goose('Белый', 2)

goat0 = Goat('Рога', 80)
goat1 = Goat('Копыта', 90)

hen0 = Hen('Ко-Ко', 2)
hen1 = Hen('Кукареку', 3)

sheep0 = Sheep('Барашек', 150)
sheep1 = Sheep('Кудрявый', 100)

cow = Cow('Манька', 700)

print(f'{goat0.name} весит {goat0.weight} кг')
print(f'{goose0.name} весит {goose0.weight} кг')
print(f'{goose1.name} весит {goose1.weight} кг')
print(f'{goose0.name} и {goose1.name} вместе весят {goose0.weight + goose1.weight} кг')
cow.talking()
print(f'{cow.name} {cow.talk}')
cow.get_milk()
print(f'{cow.name} {cow.milk}')
hen1.get_eggs()
print(f'У {hen0.name} {hen0.eggs}, а у {hen1.name} {hen1.eggs}')

weight_list = [
    goose0.get_overall_weight(),
    goose1.get_overall_weight(),
    duck.get_overall_weight(),
    goat0.get_overall_weight(),
    goat1.get_overall_weight(),
    hen0.get_overall_weight(),
    hen1.get_overall_weight(),
    sheep0.get_overall_weight(),
    sheep1.get_overall_weight(),
    cow.get_overall_weight()]

pprint(weight_list)

animal_name = None
max_weight = 0
overall_weight = 0
for item in weight_list:
    for key, value in item.items():
        overall_weight += value
        if max_weight < value:
            max_weight = value
            animal_name = key

print(f'{animal_name} - самое тяжёлое животное: {max_weight} кг')
print(f'Вес всех животных на ферме: {overall_weight} кг')
