import random, sys

class Collectibles:

    coins = {"gold": 200, "silver": 50, "cooper": 10}
    potions = {"purple potion": 50, "green potion": -100, "orange potion": 30}

    def collect(self, type, points):
        print("You collected a {} ! That is {} points".format(type, points))


class Coins(Collectibles):

    def __init__(self):
        # randomising the type of coin at the construct stage
        self.name = random.choice(list(Coins.coins))
        self.points = Coins.coins[self.name]


class Potions(Collectibles):

    def __init__(self):
        # randomising the type and colour of potion at the construct stage
        self.colour = random.choice(list(Potions.potions))
        self.points = Potions.potions[self.colour]

### End of Classes declaration

# GLOBAL VARIABLES
total_points = 0
levelUp = False
# A list for coins and potions. If your game demands it you could have also two different lists
# one for coins and one for potions.
my_collectibles = {}

# Main Loop
while True:

    while total_points <= 600:

        # Try/Except to capture unwanted input
        try:
            player = int(input("Enter a number between 1 and 6: "))

            if player in range(1, 4):

                coin = Coins()
                if coin.name not in my_collectibles.keys():
                    my_collectibles[coin.name] = 1
                else:
                    my_collectibles[coin.name] += 1

                coin.collect(coin.name, coin.points)
                total_points += coin.points

            elif player in range(4, 7):

                potion = Potions()
                if potion.colour not in my_collectibles.keys():
                    my_collectibles[potion.colour] = 1
                else:
                    my_collectibles[potion.colour] += 1

                potion.collect(potion.colour, potion.points)

                if potion.colour == "green" and total_points < 100:
                    total_points = 0
                else:
                    total_points += potion.points

            else:
                print("Only numbers between 1 and 6 please!")

            print(my_collectibles)

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




