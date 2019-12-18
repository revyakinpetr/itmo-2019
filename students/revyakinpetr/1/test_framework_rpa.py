# -*- coding: utf-8 -*-

import os

from runtests_rpa import (
    exec_test,
    find_files,
    get_module_spec,
    get_test_module,
    get_tests,
)

CURRENT_DIR = os.getcwd()
MY_DIR = '/students/revyakinpetr/1/'
FILENAME = r'{0}{1}test_framework_rpa.py'.format(CURRENT_DIR, MY_DIR)  # noqa: E501


def test_files_list():
    """Test files list."""
    assert find_files('') == []  # noqa: WPS342, WPS520
    assert find_files('{0}{1}'.format(CURRENT_DIR, MY_DIR)) == [FILENAME]  # noqa: WPS34, E501
    assert find_files('C:\\itmo\\4kusr\\7sem') == []  # noqa: WPS342, WPS520


def test_module_spec():
    """Test module spec."""
    assert get_module_spec(FILENAME).origin == FILENAME
    assert get_module_spec(FILENAME).name == FILENAME[:-3]


def test_test_module():
    """Test test module."""
    module_spec = get_module_spec(FILENAME)
    assert type(get_test_module(module_spec)).__name__ == 'module'


def test_get_tests():
    """Test get tests."""
    module_spec = get_module_spec(FILENAME)
    test_module = get_test_module(module_spec)
    tests = get_tests(module_spec, test_module)
    assert tests == [
        'test_exec_test',
        'test_files_list',
        'test_get_tests',
        'test_module_spec',
        'test_test_module',
    ]


def test_exec_test():
    """Test exec test."""
    module_spec = get_module_spec(FILENAME)
    test_module = get_test_module(module_spec)
    test_name = get_tests(module_spec, test_module)[1]
    assert exec_test(test_name, test_module) == 'ok'
