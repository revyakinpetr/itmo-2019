# -*- coding: utf-8 -*-

"""Tests for testing runtest."""
from runtests import check_path, find_files, run_tests


def test_check_path():
    """Test existing path."""
    assert check_path('')  # noqa: S101
    assert check_path('hello') is False  # noqa: S101


def test_files_list():
    """Test finding test files in directory."""
    test_result = [r'.\test_framework.py', r'.\test_one.py', r'.\test_two.py']
    assert find_files('') == test_result  # noqa: S101
    assert find_files(r'C:\itmo\4kusr\7sem') == []  # noqa: WPS520, S101


def test_run_tests():
    """Test executing test."""
    test_result = 'test_one.py test_mult - ok\n'
    assert test_result in run_tests('test_one.py')  # noqa: S101
    test_result = 'test_two.py test_mult - fail\nTraceback'
    assert test_result in run_tests('test_two.py')  # noqa: S101
    test_result = 'test_three.py test_mult - fail\nTraceback'
    assert test_result in run_tests('C:/itmo/4kusr/7sem/web/test_three.py')  # noqa: S101, E501
