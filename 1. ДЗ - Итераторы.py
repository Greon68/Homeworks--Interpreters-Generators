
# Доработать класс FlatIterator в коде ниже.
# Должен получиться итератор, который принимает список списков
# и возвращает их плоское представление, т. е. последовательность,
# состоящую из вложенных элементов.
# Функция test в коде ниже также должна отработать без ошибок.

# class FlatIterator:
#
#     def __init__(self, list_of_list):
#         ...
#
#     def __iter__(self):
#         ...
#         return self
#
#     def __next__(self):
#         ...
#         return item
#
#
# def test_1():
#
#     list_of_lists_1 = [
#         ['a', 'b', 'c'],
#         ['d', 'e', 'f', 'h', False],
#         [1, 2, None]
#     ]
#
#     for flat_iterator_item, check_item in zip(
#             FlatIterator(list_of_lists_1),
#             ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
#     ):
#
#         assert flat_iterator_item == check_item
#
#     assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
#
#
# if __name__ == '__main__':
#     test_1()

# check - "проверять", "сверить"


# Задача - распаковать список списков

class FlatIterator:

    def __init__(self, list_of_list):
        # Входящий список списков
        self.list_of_list = list_of_list
        # Текущий список
        self.current_list=[]

    def __iter__(self):
        # Счётчик количества списков в списке списков list_of_list
        self.counter = -1
        # Cчётчик индексов элементов текущего списка
        self.index = -1
        return self


    def __next__(self):
        self.index +=1 #=0 при  первом проходе
        if self.index >= len (self.current_list):
            self.counter +=1  #=0 при  первом проходе
        # Условие  выхода
            if self.counter >= len(self.list_of_list):
                raise StopIteration

            self.current_list = self.list_of_list[self.counter]
            self.index = 0

        return self.current_list[self.index]




list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]


def test_1():

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


# Список выходных данных:
results_list = []

if __name__ == '__main__':
    test_1()
    # Решение задачи:
    for item in FlatIterator(list_of_lists_1):
        results_list.append(item)
    print(results_list) # --> ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


