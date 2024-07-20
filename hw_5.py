import random
import hw_5_SRTINGS


class Planet:
    def __init__(self):
        self.food_amount = 10
        self.id_counter = 0
        self.herbivores = []
        self.predators = []
        self.dict_id = {}
        self.dict_kind_names = {}

    def add_food(self, food):
        self.food_amount += food

    def show_food_amount(self):
        print("Food amount: " + str(self.food_amount))

    def get_id(self):
        self.id_counter += 1
        return self.id_counter

    def add_kind(self, name, size, predator_flag, habitat, max_age):
        self.dict_kind_names[name] = Kind(name, size, predator_flag, habitat, max_age)

    def reproduce(self, id_1, id_2):
        if id_1 == id_2:
            print(hw_5_SRTINGS.REPRODUCE_SAME_ANIMAL_ERROR)
            return 0
        try:
            return self.dict_id[id_1].reproduce(self.dict_id[id_2])
        except NameError:
            print(hw_5_SRTINGS.NO_ANIMALS_ERROR)
            return 0

    def create_new_animal(self, kind, satiety):
        self.add_animal(kind, 0, satiety,
                        ["Male", "Female"][random.randint(0, 1)])

    def add_animal(self, kind, age, satiety, sex):
        if age > kind.max_age:
            return 0
        match kind.habitat:
            case "Water":
                if kind.predator_flag:
                    animal_id = self.get_id()
                    animal = AquaticAnimals(kind, animal_id, age, satiety,
                                            sex, self)
                    if not animal.dead_flag:
                        self.predators.append(animal)
                        self.dict_id[animal_id] = animal
                else:
                    animal_id = self.get_id()
                    animal = AquaticAnimals(kind, animal_id, age, satiety,
                                            sex, self)
                    if not animal.dead_flag:
                        self.herbivores.append(animal)
                        self.dict_id[animal_id] = animal
            case "Air":
                if kind.predator_flag:
                    animal_id = self.get_id()
                    animal = AerialAnimals(kind, animal_id, age, satiety,
                                           sex, self)
                    if not animal.dead_flag:
                        self.predators.append(animal)
                        self.dict_id[animal_id] = animal
                else:
                    animal_id = self.get_id()
                    animal = AerialAnimals(kind, animal_id, age, satiety,
                                           sex, self)
                    if not animal.dead_flag:
                        self.herbivores.append(animal)
                        self.dict_id[animal_id] = animal
            case "Land":
                if kind.predator_flag:
                    animal_id = self.get_id()
                    animal = LandAnimals(kind, animal_id, age, satiety,
                                         sex, self)
                    if not animal.dead_flag:
                        self.predators.append(animal)
                        self.dict_id[animal_id] = animal
                else:
                    animal_id = self.get_id()
                    animal = LandAnimals(kind, animal_id, age, satiety,
                                         sex, self)
                    if not animal.dead_flag:
                        self.herbivores.append(animal)
                        self.dict_id[animal_id] = animal
        return 1

    def show_kind(self, name):
        in_flag = False
        try:
            print(str(self.dict_kind_names[name]))
        except NameError:
            print(hw_5_SRTINGS.NO_KIND_ERROR)

    def show_kinds(self):
        for kind in self.dict_kind_names:
            print(str(self.dict_kind_names[kind]))

    def show_animal(self, id):
        try:
            print(str(self.dict_id[id]))
        except NameError:
            print(hw_5_SRTINGS.NO_ANIMAL_ERROR)

    def show_animals(self):
        if not self.dict_id:
            print(hw_5_SRTINGS.EMPTY_PLANET_MESSAGE)
            return
        for animal in self.dict_id:
            print(str(self.dict_id[animal]))

    def corpse_destroyer(self):
        cntr = 0
        while cntr < len(self.herbivores):
            if self.herbivores[cntr].dead_flag:
                self.herbivores.pop(cntr)
                del self.dict_id[self.herbivores[cntr].id]
            else:
                cntr += 1
        cntr = 0
        while cntr < len(self.predators):
            if self.predators[cntr].dead_flag:
                self.predators.pop(cntr)
                del self.dict_id[self.predators[cntr].id]
            else:
                cntr += 1

    def step(self):
        for animal in self.herbivores + self.predators:
            animal.grow_old()
        self.corpse_destroyer()
        for animal in self.herbivores:
            animal.eat()
        self.corpse_destroyer()
        for animal in self.predators:
            animal.eat()
        self.corpse_destroyer()
        for animal in self.herbivores + self.predators:
            animal.hunger_check()
        self.corpse_destroyer()


class Kind:
    def __init__(self, name, size, predator_flag, habitat, max_age):
        self.name = name
        self.size = size
        self.predator_flag = predator_flag
        self.habitat = habitat
        self.max_age = max_age

    def __repr__(self):
        final_str = hw_5_SRTINGS.SEPARATOR + "Name: {}\nSize: {}\n".format(
            self.name, self.size)
        if self.predator_flag:
            final_str += "It is predator\n"
        else:
            final_str += "It is herbivorous\n"
        final_str += "Habitat: {}\nMax age: {}\n".format(self.habitat,
                                                         self.max_age) + hw_5_SRTINGS.SEPARATOR
        return final_str


class Animal():
    def __init__(self, kind, id, age, satiety, sex, planet):
        self.kind = kind
        self.id = id
        self.age = age
        self.sex = sex
        self.satiety = satiety
        self.dead_flag = False
        self.is_it_ate = False
        self.planet = planet
        if self.age > self.kind.max_age:
            self.dead()

    def __repr__(self):
        return hw_5_SRTINGS.SEPARATOR + "Kind: {}\nId: {}\nAge: {}\nSatiety: {}\nSex: {}\n".format(
            self.kind.name, self.id, self.age, self.satiety,
            self.sex) + hw_5_SRTINGS.SEPARATOR

    def grow_old(self):
        self.age += 1
        if self.age > self.kind.max_age:
            self.dead()

    def eat(self):
        if self.dead_flag:
            return
        if self.kind.predator_flag:
            if random.randint(1, 2) == 1:
                try:
                    self.planet.herbivores[
                        random.randint(0, len(self.planet.herbivores) - 1)].dead()
                    self.satiety += 53
                    self.is_it_ate = True

                except ValueError:
                    self.satiety -= 16
            else:
                self.satiety -= 16
        else:
            if self.planet.food_amount != 0:
                self.planet.food_amount -= 1
                self.satiety += 26
                self.is_it_ate = True
        self.satiety = min(100, self.satiety)

    def hunger_check(self):
        if not self.is_it_ate:
            self.satiety -= 9
        if self.satiety < 10:
            self.dead()
        self.is_it_ate = False

    def dead(self):
        if self.kind.predator_flag:
            for animal_indx in range(len(self.planet.predators)):
                if self.planet.predators[animal_indx].id == self.id:
                    self.planet.predators.pop(animal_indx)
                    break
        else:
            for animal_indx in range(len(self.planet.herbivores)):
                if self.planet.herbivores[animal_indx].id == self.id:
                    self.planet.herbivores.pop(animal_indx)
                    break
        if self.id in self.planet.dict_id:
            self.planet.dict_id.pop(self.id)
        self.planet.food_amount += self.kind.size
        self.dead_flag = True


class AquaticAnimals(Animal):
    def reproduce(self, animal):
        if self.kind.name != animal.kind.name:
            print(hw_5_SRTINGS.REPRODUCE_DIFFERENT_KINDS_ERROR)
            return 0
        if self.satiety <= 50 or animal.satiety <= 50:
            print(hw_5_SRTINGS.REPRODUCE_HUNGER_ERROR)
            return 0
        if self.sex == animal.sex:
            print(hw_5_SRTINGS.REPRODUCE_SAME_SEX_ERROR)
            return 0
        for i in range(10):
            self.planet.create_new_animal(self.kind, 23)
        return 1


class AerialAnimals(Animal):
    def reproduce(self, animal):
        if self.kind.name != animal.kind.name:
            print(hw_5_SRTINGS.REPRODUCE_DIFFERENT_KINDS_ERROR)
            return 0
        if self.satiety <= 42 or animal.satiety <= 42:
            print(hw_5_SRTINGS.REPRODUCE_HUNGER_ERROR)
            return 0
        if self.age <= 3 or animal.age <= 3:
            print(hw_5_SRTINGS.REPRODUCE_AGE_ERROR)
            return 0
        if self.sex == animal.sex:
            print(hw_5_SRTINGS.REPRODUCE_SAME_SEX_ERROR)
            return 0
        for i in range(4):
            self.planet.create_new_animal(self.kind, 64)
        return 1


class LandAnimals(Animal):
    def reproduce(self, animal):
        if self.kind.name != animal.kind.name:
            print(hw_5_SRTINGS.REPRODUCE_DIFFERENT_KINDS_ERROR)
            return 0
        if self.satiety <= 20 or animal.satiety <= 20:
            print(hw_5_SRTINGS.REPRODUCE_HUNGER_ERROR)
            return 0
        if self.age <= 5 or animal.age <= 5:
            print(hw_5_SRTINGS.REPRODUCE_AGE_ERROR)
            return 0
        if self.sex == animal.sex:
            print(hw_5_SRTINGS.REPRODUCE_SAME_SEX_ERROR)
            return 0
        for i in range(2):
            self.planet.create_new_animal(self.kind, 73)
        return 1
