from typing import Iterable, Optional, TypeVar

T = TypeVar('T')


def find_max(items: Iterable[T]) -> Optional[T]:
    """Find the maximum element in an iterable of comparable items.

    Args:
        items: An iterable (list, tuple, generator, etc.) of comparable elements.

    Returns:
        The maximum element in the iterable, or None if the iterable is empty.

    Complexity:
        Time: O(n) where n is the number of elements in the iterable.
        Space: O(1) additional space.

    Examples:
        >>> find_max([1, 3, 2])
        3
        >>> find_max([]) is None
        True
        >>> find_max((x for x in range(5)))
        4
    """
    return max(items, default=None)
