import binary_search.binary_search as bs

def test_should_return_minus_one_if_item_not_found_in_the_list():
    arr = [1,2,3,4,5,6,7,8,9,10]
    assert bs.search(arr, 15) == -1

def test_should_return_index_if_5_found_in_the_list():
    arr = [1,2,3,4,5,6,7,8,9,10]
    assert bs.search(arr, 5) == 4

def test_should_return_index_if_4_found_in_the_list():
    arr = [1,2,3,4,5,6,7,8,9,10]
    assert bs.search(arr, 4) == 3

def test_should_return_minus_one_if_list_is_empty():
    assert bs.search([], 15) == -1

# pytest --cov-report html:cov_html --cov=binary_search test