import pytest

from unittest.mock import patch

from data_structures_and_algorithms.python.Data-Structure.linked_list.linked_list import Node, LinkedList

def test_import():
    assert LinkedList


l_list = LinkedList()


def test_empty():
    actual = l_list.head
    expect = None
    assert actual == expect


def test_insert():
    l_list.insert(5)
    actual = l_list.includes(5)
    expect = True
    assert actual == expect


def test_head():
    l_list.insert(5)
    l_list.insert(3)
    l_list.insert(9)
    actual = l_list.head.value
    expect = 9
    assert actual == expect
    actual2 = l_list.head.next.value
    expect2 = 3
    assert actual2 == expect2




def test_return():
    actual = l_list.__str__()
    expect = "{9} --->{3} --->{5} --->{5} --->None"
    assert actual == expect


def test_append():
    l_list.append(8)
    actual = l_list.__str__()
    expect = "{9} --->{3} --->{5} --->{5} --->{8} --->None"
    assert actual == expect


def test_insert_before():
    l_list.insertBefore(6, 20)
    actual = l_list.__str__()
    expect = "{9} --->{3} --->{5} --->{5} --->{8} --->None"
    assert actual == expect

def test_insert_after():
    l_list.insertAfter(10, 6)
    actual = l_list.__str__()
    expect = "{9} --->{3} --->{5} --->{5} --->{8} --->None"
    assert actual == expect

