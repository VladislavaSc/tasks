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
                pass
            else:
                print('I dont know this command')


    def __help_text(self):
        print('Commands available: ')
        print('1 - choose ingredients')
        print('0 - exit')

    def choose_ingredients(self):
        print('Ingredient list: ')


if __name__ == '__main__':
    raf9 = Raf9()
    raf9()
