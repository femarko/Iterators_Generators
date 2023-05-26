import types

def flat_generator(list_of_lists):
    count_list = 0
    count_element = -1
    while count_list <= len(list_of_lists) - 1:
        try:
            count_element += 1
            result = list_of_lists[count_list][count_element]
            yield result
        except IndexError:
            try:
                count_list += 1
                count_element = 0
                result = list_of_lists[count_list][count_element]
                yield result
            except IndexError:
                return

def test_2():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()