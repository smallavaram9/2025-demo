"""Unit tests for maxFinder.find_max function."""

from maxFinder import find_max


def test_empty_input():
    """Test that find_max returns None for empty input."""
    assert find_max([]) is None
    assert find_max(()) is None


def test_list_of_ints():
    """Test find_max with a list of positive integers."""
    assert find_max([1, 2, 3, 4, 5]) == 5
    assert find_max([5, 4, 3, 2, 1]) == 5
    assert find_max([3, 1, 4, 1, 5, 9, 2, 6]) == 9


def test_list_with_negative_numbers():
    """Test find_max with negative numbers."""
    assert find_max([-1, -2, -3]) == -1
    assert find_max([-5, 0, 5]) == 5
    assert find_max([-10, -20, -5, -1]) == -1


def test_list_with_duplicates():
    """Test find_max with duplicate values."""
    assert find_max([5, 5, 5]) == 5
    assert find_max([1, 3, 3, 2]) == 3
    assert find_max([7, 7, 1, 7, 2]) == 7


def test_generator_input():
    """Test find_max with generator input."""
    assert find_max(x for x in range(10)) == 9
    assert find_max(x * 2 for x in [1, 2, 3]) == 6
    assert find_max(x for x in []) is None
