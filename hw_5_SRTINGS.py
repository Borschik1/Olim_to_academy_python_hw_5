SEPARATOR = "-----------------------------------------------------------------\n"

NO_KIND_ERROR = "There is no kind with that name"
NO_ANIMAL_ERROR = "There is no animal with that ID"
NO_ANIMALS_ERROR = "There are no animals with theese IDs"
ANIMAL_TOO_OLD_ERROR = "This creature too old. It can't be created"
EMPTY_PLANET_MESSAGE = "The planet is empty"

REPRODUCE_DIFFERENT_KINDS_ERROR = "There are two different kinds. You can't " \
                                  "reproduce them "
REPRODUCE_HUNGER_ERROR = "One of that animals too hunger for reproducing"
REPRODUCE_SAME_SEX_ERROR = "There are two animal with the same sex. You " \
                           "Youcan't reproduce them "
REPRODUCE_AGE_ERROR = "One of that animals too young for reproducing"
REPRODUCE_SAME_ANIMAL_ERROR = "There is one animal. For reproduction you need to enter two different IDs"

HELP = SEPARATOR + "help - show all commands\nstop - end " \
                   "simulation\nadd_creature <name> <age> <satiety> <sex> - " \
                   "add new animal\nshow_kind <name> - show kind with that " \
                   "name\nshow_kinds - show all kinds\nshow_creature <ID> - " \
                   "show animal with that ID " \
                   "\nshow_creatures - show all animals\nreproduce " \
                   "<first ID> <second ID> - reproduce two animals\nstep - " \
                   "advances time by 1\nfood - show food amount in the " \
                   "planet\nadd_food <amount> - add this amount of food to " \
                   "the planet\n" + \
       SEPARATOR
WELCOME_STRING = "Welcome! There is my world simulation. From bellow you can " \
                 "find 12 kinds of animals in that world. If you need " \
                 "information about functions - enter \"help\" "
WRONG_ARGUMENTS_ERROR = "Wrong arguments! If you want help, enter \"help\""
COMMAND_NOT_FOUND = "Command not found"
BINARY_SEX_ERROR = "Unrecognized sex. Creatures can be only \"Male\" and \"Female\""
DONE = "Command completed"
