

import gc



from common.find_stone_pair import F, get_all_stone_pair


def test_find_one_stone_pair():
    """
        test find one stone pair
        there are 3 test case
    """
    arr = [1, 4, 3]
    d = 2
    result = F(arr, d)
    assert (1, 3) == result

    arr = []
    d = 3
    result = F(arr, d)
    assert () == result

    arr = [1, 3, 4]
    d = 4
    result = F(arr, d)
    assert () == result


def test_get_all_stone_pair():
    """
        test get all stone pair
    """

    arr = [1, 3, 5, 6, 7, 8, 3, 1]
    d = 2
    result = get_all_stone_pair(arr, d)
    assert {(1, 3), (6, 8), (5, 7),  (3, 5)} == result

    arr = [1, 3, 5, 6, 7, 8, 3, 1]
    d = 8
    result = get_all_stone_pair(arr, d)
    assert set() == result

    arr = []
    d = 0
    result = get_all_stone_pair(arr, d)
    assert set() == result


def test_gc():
    print(gc.get_threshold())
