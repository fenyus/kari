import random


class Person:
    def __init__(self, name, blocked_names):
        self.name = name
        self.blocked_names = blocked_names
        self.picked_name = "NONE"
        self.reserved = False

    def set_picked_name(self, name):
        self.picked_name = name

    def set_reserved(self):
        self.reserved = True


persons = (
    Person("Agi_neni", ("Gabor_ba",)),
    Person("Gabor_ba", ("Agi_neni",)),
    Person("Gyongyver", ("Geri", "Luca")),
    Person("Geri", ("Gyongyver", "Luca")),
    Person("Luca", ("Gyongyver", "Geri")),
    Person("Kincso", ("Tamas",)),
    Person("Tamas", ("Kincso",)),
    Person("Dori", ("Levi",)),
    Person("Levi", ("Dori",)),
    Person("Anna", ("Ati",)),
    Person("Csabi", ()),
)
number_of_persons = len(persons)
for person in persons:
    num_of_iteration = 0
    while True:
        picked_index = random.randint(0, number_of_persons - 1)
        if person.name not in persons[picked_index].blocked_names:
            if person.name != persons[picked_index].picked_name:
                if person.name != persons[picked_index].name:
                    if persons[picked_index].reserved == False:
                        person.set_picked_name(persons[picked_index].name)
                        persons[picked_index].set_reserved()
                        with open(person.name + ".txt", "w") as f:
                            f.write(person.picked_name)

        if person.picked_name != "NONE":
            break
        elif num_of_iteration == 100:
            print("No match found for ", person.name)
            break
        else:
            num_of_iteration = num_of_iteration + 1
