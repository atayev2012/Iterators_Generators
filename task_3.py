def list_flattener(data_list):
    data = []
    for item in data_list:
        if type(item).__name__ == "list":
            data += list_flattener(item)
        else:
            data += [item]
    return data


class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.flat_list = list_flattener(self.list_of_list)
        self.cursor = -1
        return self

    def __next__(self):
        self.cursor += 1
        if self.cursor >= len(self.flat_list):
            raise StopIteration
        item = self.flat_list[self.cursor]
        return item


def test_3():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()
 