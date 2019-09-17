# -*- coding: utf-8 -*-

"""Test file number one."""


def my_sum(first, second):
    """Sum function."""
    return first + second


def test_sum():
    """Test sum function."""
    assert my_sum(1, 2) == 3  # noqa: S101


def my_mult(first, second):
    """Multiply function."""
    return first * second


def test_mult():
    """Test multiply function."""
    assert my_mult(5, 3) == 15  # noqa: S101, WPS432
    assert my_mult(2, 4) == 8  # noqa: S101
    assert my_mult(-2, 4) == -8  # noqa: S101
    assert my_mult(2, -4) == -8  # noqa: S101
    assert my_mult(-2, -4) == 8  # noqa: S101
