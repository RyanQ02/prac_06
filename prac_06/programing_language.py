class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        print("{}, {}, {}, first appeared in {}".format(self.name, self.typing, self.reflection, self.year))
