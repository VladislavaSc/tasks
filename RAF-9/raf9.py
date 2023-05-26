import json


class Raf9:
    def __init__(self):
        self.ingredients = ['lemon', 'mint', 'ice', 'soda', 'orange', 'tomato']

    def __call__(self, *args, **kwargs):
        while True:
            self.__help_text()
            command = input('Enter command: ')
            if command == '0':
                print('All the best, come again!')
                break
            elif command == '1':
                current_ints = self.choose_ingredients()
                self.find_cocktail(current_ints)
            else:
                print('I dont know this command')


    def __help_text(self):
        print('Commands available: ')
        print('1 - choose ingredients')
        print('0 - exit')

    def get_cocktails_from_db(self):
        with open('cocktail.json', r) as json_file:
            self.cocktails = json.load(json_file)

    def find_cocktail(self, current_ings):
        pass

    def choose_ingredients(self):
        choose_ings = []
        print('Ingredient list: ')

        i = 0
        for ing in self.ingredients:
            i += 1
            print(f'{i}. {ing}')

        print('0 - for exit')

        while True:
            command = input('Enter command: ')
            if command == '0':
                return choose_ings
            else:
                if command.isdigit():
                    number = int(command)
                    if number > len(self.ingredients):
                        print('There is no such ingredient in the list')
                    else:
                        choose_ings.append(self.ingredients[number-1])
                else:
                    print('Enter ingredient number')

if __name__ == '__main__':
    raf9 = Raf9()
    raf9()
