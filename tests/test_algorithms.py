import pytest

from src.algorithms import first_unique_index


@pytest.mark.parametrize(
    "text, expected",
    [
        ("A", 0),
        ("Ab", 0),
        ("aaA", 2),
        ("abac", 1),
        ("aabb", -1),
        ("", -1),
    ],
)
def test_first_unique_index(text, expected):
    assert first_unique_index(text) == expected