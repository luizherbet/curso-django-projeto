from random import randint
from faker import Faker

def rand_ratio():
    return randint(840,900), randint(473,573)

fake = Faker('pt-BR')

def make_recipe():
    return{
        'title': fake.sentence(nb_words=6),
        'description': fake.sentence(nb_words=12),
        'cover' : {'url':'https://loremflicker.com/%s/%s/food,cook' % rand_ratio()}
    }

if __name__ == '__main__':
    from pprint import pprint
    pprint(make_recipe())