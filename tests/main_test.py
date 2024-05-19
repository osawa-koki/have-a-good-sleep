import pytest


@pytest.mark.parametrize(
    "a, b",
    [
        (1 + 1, 2),
        (1 + 3, 4),
        (1 + 5, 6),
    ],
)
def test_main(a, b):
    assert a == b
