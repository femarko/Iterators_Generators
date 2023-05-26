class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.count_list = 0
        self.count_element = -1
        return self

    def __next__(self):
        try:
            self.count_element += 1
            element = self.list_of_list[self.count_list][self.count_element]
        except IndexError:
            try:
                self.count_list += 1
                self.count_element = 0
                element = self.list_of_list[self.count_list][self.count_element]
            except IndexError:
                raise StopIteration
        return element


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()