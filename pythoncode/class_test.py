class Animal(object):
    def __init__(self,name,color,age,gender):
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender
    def call(self):
        print('这个动物会叫')
    def run(self):
        print('这个动物会跑')

class cat(Animal):
    def __init__(self, name, color, age, gender,hair):
        super().__init__(name, color, age, gender)
        self.hair = hair
    def catch_mouse(self):
        print('我抓住了老鼠')
    def call(self):
        print('喵喵喵')

class dog(Animal):
    def __init__(self, name, color, age, gender,hair):
        super().__init__(name, color, age, gender)
        self.hair = hair

    def watch_house(self):
        print('我会看家')
    def call(self):
        print('汪汪汪')


if __name__ == '__main__':

    cat = cat('tom','蓝猫','4','公','短毛')
    print(f'{cat.name},{cat.color},{cat.age},{cat.gender},{cat.hair}')
    cat.catch_mouse()
    dog = dog('feizhai','牧羊犬','6','母','长毛')
    print(f'{dog.name},{dog.color},{dog.age},{dog.gender},{dog.hair}')
    dog.watch_house()


