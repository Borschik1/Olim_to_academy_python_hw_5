import hw_5_SRTINGS
from hw_5 import Planet, AerialAnimals, AquaticAnimals, LandAnimals

planet = Planet()

planet.add_kind("Wolf", 3, True, "Land", 15)
planet.add_kind("Mouse", 1, False, "Land", 6)
planet.add_kind("Lion", 4, True, "Land", 21)
planet.add_kind("Deer", 4, False, "Land", 12)

planet.add_kind("Shark", 4, True, "Water", 30)
planet.add_kind("Dolphin", 3, True, "Water", 30)
planet.add_kind("Tuna", 3, True, "Water", 12)
planet.add_kind("Carp", 2, False, "Water", 21)

planet.add_kind("Pelican", 3, True, "Air", 24)
planet.add_kind("Dove", 1, False, "Air", 9)
planet.add_kind("Albatross", 5, True, "Air", 30)
planet.add_kind("Kiwi", 1, False, "Air", 21)

print(hw_5_SRTINGS.WELCOME_STRING)
planet.show_kinds()

while True:
    user_input = input().split(" ")
    match user_input[0]:
        case "stop":
            break
        case "help":
            print(hw_5_SRTINGS.HELP)
        case "add_creature":
            try:
                if user_input[4] not in ["Male", "Female"]:
                    print(hw_5_SRTINGS.BINARY_SEX_ERROR)
                else:
                    if not planet.add_animal(planet.dict_kind_names[user_input[1]],
                                      int(user_input[2]), int(user_input[3]),
                                      user_input[4]):
                        print(hw_5_SRTINGS.ANIMAL_TOO_OLD_ERROR)
                    else:
                        print(hw_5_SRTINGS.DONE)
            except IndexError or ValueError:
                print(hw_5_SRTINGS.WRONG_ARGUMENTS_ERROR)
        case "food":
            planet.show_food_amount()
        case "add_food":
            try:
                planet.add_food(int(user_input[1]))
                print(hw_5_SRTINGS.DONE)
            except IndexError or ValueError:
                print(hw_5_SRTINGS.WRONG_ARGUMENTS_ERROR)
        case "show_kind":
            try:
                planet.show_kind(user_input[1])
            except IndexError or ValueError:
                print(hw_5_SRTINGS.WRONG_ARGUMENTS_ERROR)
        case "show_kinds":
            planet.show_kinds()
        case "show_creature":
            try:
                planet.show_animal(int(user_input[1]))
            except IndexError or ValueError:
                print(hw_5_SRTINGS.WRONG_ARGUMENTS_ERROR)
        case "show_creatures":
            planet.show_animals()
        case "reproduce":
            try:
                if planet.reproduce(int(user_input[1]), int(user_input[2])):
                    print(hw_5_SRTINGS.DONE)
            except IndexError or ValueError:
                print(hw_5_SRTINGS.WRONG_ARGUMENTS_ERROR)
        case "step":
            planet.step()
            print(hw_5_SRTINGS.DONE)
        case _:
            print(hw_5_SRTINGS.COMMAND_NOT_FOUND)
