import random, sys

class Collectibles:

    def collect(self, points):
        print("Collected {} points".format(points))


class Coins(Collectibles):

    __coins = {"gold": 200, "silver": 50, "cooper": 10}

    def __init__(self):
        # randomising the type of coin at the construct stage
        self.name = random.choice(list(Coins.__coins))
        self.points = Coins.__coins[self.name]


class Potions(Collectibles):
    __potions = {"purple": 50, "green": -100, "orange": 30}

    def __init__(self):
        # randomising the type and colour of potion at the construct stage
        self.colour = random.choice(list(Potions.__potions))
        self.points = Potions.__potions[self.colour]

### End of Classes declaration

# GLOBAL VARIABLES
total_points = 0
levelUp = False
# A list for coins and potions. If your game demands it you could have also two different lists
# one for coins and one for potions.
list_of_collectibles = []

# Main Loop
while True:

    while total_points <= 600:

        # Try/Except to capture unwanted input
        try:
            player = int(input("Enter a number between 1 and 6: "))

            if player in range(1, 4):
                # append a coin
                list_of_collectibles.append(Coins())
                # we get the last entered collectible - the one we just appended
                # and add the corresponding points
                list_of_collectibles[len(list_of_collectibles) - 1].collect(list_of_collectibles[len(list_of_collectibles) - 1].points)
                total_points += list_of_collectibles[len(list_of_collectibles) - 1].points

            elif player in range(4, 7):
                # append a Potion
                list_of_collectibles.append(Potions())
                # as above
                list_of_collectibles[len(list_of_collectibles) - 1].collect(list_of_collectibles[len(list_of_collectibles) - 1].points)

                if list_of_collectibles[len(list_of_collectibles) - 1].colour == "green" and total_points < 100:
                    total_points = 0
                else:
                    total_points += list_of_collectibles[len(list_of_collectibles) - 1].points
            else:
                print("Only numbers between 1 and 6 please!")

            print("Total points:{}".format(total_points))
            if total_points > 300 and not levelUp:
                print("You leveled up!!!!")
                levelUp = True

            # If the user inputs anything else but a number between 1-6
        except ValueError:
            print("Only numbers please!")

        # If the user inputs a CTRL+C to exit (or Windows equivalent exit shortcut) capture
        # this and exit
        except KeyboardInterrupt:
            print("Bye Bye")
            sys.exit()

    else:
        print("You have enough now!!!!")

    # Game continues....
    input("Where next ? s/n/e/w")




