
class Guitar:
    def __init__(self, name, year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost


    def __str__(self):
        return "{} ({}): ${}".format(self.name,str(self.year), str(self.cost))

    def get_age(self):
        age = 2018 - int(self.year)
        return age

    def is_vintage(self):
        if self.year >= 50:
            return True


