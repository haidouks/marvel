import pytest
import cli
from random import randint


matching_test_keyword = "hulk"
nonmatching_test_keyword = "qweasdzxc"

@pytest.fixture
def empty_keyword():
    '''Returns all characters'''
    return cli.search_marvel_characters(keyword="")

@pytest.fixture
def matching_keyword():
    '''Returns matching characters'''
    return cli.search_marvel_characters(keyword=matching_test_keyword)

@pytest.fixture
def nonmatching_keyword():
    '''Returns empty list'''
    return cli.search_marvel_characters(keyword=nonmatching_test_keyword)

def test_return_all_characters(empty_keyword):
    assert len(empty_keyword) >= 1
    index = randint(0,len(empty_keyword)-1)
    assert empty_keyword[index].get("name") is not None
 
def test_empty_characters_list(nonmatching_keyword):
    assert len(nonmatching_keyword) == 0

def test_matching_characters_list(matching_keyword):
    assert len(matching_keyword) > 0
    index = randint(0,len(matching_keyword)-1)
    assert matching_test_keyword.lower() in matching_keyword[index]["name"].lower()