# This script holds the names of all your pets when your parent allow just one

class Pet:
    def __init__(self, name):
        self.name = name


def ask_pet_data():
    while True: # https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response/23294659
        petinput = input("Type the name of your pet: ")
        if len(petinput) == 0:
            print("All pets must have names.")
            continue
        else:
            mypet = Pet(petinput)
            print("Your pet is called {0}.".format(mypet.name))
            return mypet

def ask_pet_destroy():
    while True:
        action = input("You already have a pet called {0}. Destroy? (y/n): ".format(mypet.name))
        if action.lower() not in ('y', 'n'):
            print("Invalid choice.")
        else:
            return action


if __name__ == "__main__":
    mypet = None
    while True:
        try:
            if mypet is None:
                mypet = ask_pet_data()
            else:
                raise ValueError
        except ValueError as error:
            petdestroy = ask_pet_destroy()
            if petdestroy == 'y':
                print("{0} destroyed. Have a nice day.".format(mypet.name))
                mypet = None
                continue
            elif petdestroy == 'n':
                print("{0} was not destroyed.".format(mypet.name))
                continue
            else:
                print('You found a bug. Make a pull request if you figure out what it was.')
