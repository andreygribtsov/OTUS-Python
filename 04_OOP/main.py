class Point:
    
    c = 10 

    def __init__(self):
        self.a = 10
        self.b = 12
        self.__x = 25

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if x > 10:
            self.__x = 10
        if x < 0:
            self.__x = 0


    def my_print(self):
        print(self.a, self.b, self.c)


p = Point()

print(f'F = {p.x}')
p.x = -10
print(f'if x = -10 F = {p.x}')
p.x = 20
print(f'if x = 20 F = {p.x}')

p.__x = 15
