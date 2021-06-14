import pytest

from unittest.mock import patch

from data_structures_and_algorithms.python.code_challenge.linked_list.linked_list import Node, LinkedList


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
    l_list.insert(10)
    l_list.insert(18)
    actual = l_list.head.value
    expect = 18
    assert actual == expect
    actual2 = l_list.head.next.value
    expect2 = 10
    assert actual2 == expect2




def test_return():
    actual = l_list.__str__()
    expect = "{18} --->{10} --->{5} --->{5} --->None"
    assert actual == expect


def test_append():
    l_list.append(8)
    actual = l_list.__str__()
    expect = "{18} --->{10} --->{5} --->{5} --->{8} --->None"
    assert actual == expect

