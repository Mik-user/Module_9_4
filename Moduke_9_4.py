from random import choice

class MysticBall:
    def __init__(self,*words):
        self.words = words

    def __call__(self, *words):
        return choice(self.words)

first = 'Мама мыла раму'
second = 'Рамена мало было'
my_function = lambda x,y: (x==y)
rez = list(map(my_function, first, second))
print(list(rez))

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name,'w',encoding='utf-8') as file:
            file.write(f'{data_set}')
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


first_ball = MysticBall('меня', 'жена', 'любящая','спать','зовет')
print(first_ball())
print(first_ball())
print(first_ball())