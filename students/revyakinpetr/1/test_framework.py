# -*- coding: utf-8 -*-

"""Tests for testing runtest."""
import os

from runtests import check_path, find_files, run_tests


def test_check_path():
    """Test existing path."""
    assert check_path('')  # noqa: S101
    assert check_path('hello') is False  # noqa: S101


def test_files_list():
    """Test finding test files in directory."""
    current_dir = os.getcwd()
    test_result = [
        r'{0}\test_framework.py'.format(current_dir),
        r'{0}\test_one.py'.format(current_dir),
        r'{0}\test_two.py'.format(current_dir),
    ]
    assert test_result == find_files('')  # noqa: S101


def test_run_tests():
    """Test executing test."""
    test_result = 'test_one.py test_mult - ok\n'
    assert test_result in run_tests(r'.\test_one.py')  # noqa: S101
    test_result = 'test_two.py test_mult - fail\nTraceback'
    assert test_result in run_tests(r'.\test_two.py')  # noqa: S101
