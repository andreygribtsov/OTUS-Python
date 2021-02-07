
# create own class Exception
class PositiveValueError(ValueError):

    def __str__(self):
        return 'Age can not be a negative'


class Bear():
    def __init__(self, name, age):
        self.name = name
        
        if age < 0:
            raise PositiveValueError() 
        self.age = age

    def __str__(self):
        return f'{self.name} {self.age}'



bear = Bear('Dude', -20)
print(bear)

