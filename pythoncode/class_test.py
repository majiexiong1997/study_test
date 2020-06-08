import yaml
from method_summary import yaml_test

class Animal(object):
    def __init__(self, name, color, age, gender):
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
    yaml.warnings({'YAMLLoadWarning': False})
    # with open('test.yml', 'rb') as f:
    #     all_data = yaml.load(f)
    #     print(all_data)
    a = yaml_test.yaml_load('test.yml').load_yaml()
    cat_data = a['cat']
    dog_data = a['d']
    #
    cat = cat(cat_data['name'], cat_data['color'], cat_data['age'], cat_data['gender'], cat_data['hair'])
    print(f'{cat.name},{cat.color},{cat.age},{cat.gender},{cat.hair}')
    cat.catch_mouse()
    dog = dog(dog_data['name'], dog_data['color'], dog_data['age'], dog_data['gender'], dog_data['hair'])
    print(f'{dog.name},{dog.color},{dog.age},{dog.gender},{dog.hair}')
    dog.watch_house()
