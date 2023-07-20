# Доработать функцию flat_generator.
# Должен получиться генератор, который принимает список списков
# и возвращает их плоское представление.
# Функция test в коде ниже  должна отработать без ошибок.
# import types
#
#
# def flat_generator(list_of_lists):
#
#     ...
#     yield
#     ...
#
#
# def test_2():
#
#     list_of_lists_1 = [
#         ['a', 'b', 'c'],
#         ['d', 'e', 'f', 'h', False],
#         [1, 2, None]
#     ]
#
#     for flat_iterator_item, check_item in zip(
#             flat_generator(list_of_lists_1),
#             ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
#     ):
#
#         assert flat_iterator_item == check_item
#
#     assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
#
#     assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)
#
#
# if __name__ == '__main__':
#     test_2()
#
import types

def flat_generator(list_of_lists):
    # Счётчик для текущего списка внутри списка списков:
    counter=-1
    while counter < len(list_of_lists)-1:
        counter += 1
        # Текущий список
        current_list = list_of_lists[counter]
        for el in current_list:
            yield el


list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]]



def test_2():


    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)

# Список выходных данных :
results_list = []


if __name__ == '__main__':
    test_2()
    for item in flat_generator(list_of_lists_1):
        results_list.append(item)
    print(results_list)






