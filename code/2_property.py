# Underscore, Getter, Setter

class Example:
    def __init__(self):
        self.x = 0
        self.__y =0 # private
        self._z = 0 # protected

    @property
    def y(self):
        print('Get Method')
        return self.__y

    @y.setter
    def y(self, value):
        print('Set Method')
        if value < 1:
            raise ValueError('양수를 입력하세요')
        self.__y=value

    @y.deleter
    def y(self):
        print('Del Method')
        del self.__y


test = Example()

test.x = 0
test.y = 13

print(f'x instance is {test.x}')
print(f'y instance is {test.y}')
test.y = 0
