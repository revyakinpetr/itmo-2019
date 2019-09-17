# -*- coding: utf-8 -*-

"""Test framework."""
import glob
import os
import traceback
from importlib import util as importutil


def check_path(path):
    """Check existing of path."""
    if not path:
        path = os.getcwd()
    return os.path.exists(path)


def find_files(path):
    """Find and return python test files in path."""
    if not path:
        path = os.getcwd()
    return glob.glob('{path}/test_*.py'.format(path=path))


def run_tests(filename):  # noqa: WPS210
    """Find tests and execute them."""
    module_spec = importutil.spec_from_file_location(
        filename[:-3], filename,
    )

    test_module = importutil.module_from_spec(module_spec)
    module_spec.loader.exec_module(test_module)
    tests = [
        test for test in dir(test_module)  # noqa: WPS421
        if test.startswith('test_')
    ]

    return_string = ''
    for test in tests:
        try:  # noqa: WPS229
            vars(test_module)[test]()  # noqa: WPS421
            return_string += '{0} {1} - ok\n'.format(filename, test)
        except Exception:
            prms = [filename, test, traceback.format_exc()]
            return_string += '{0} {1} - fail\n{2}'.format(*prms)
    return return_string


if __name__ == '__main__':
    path = input('Введи путь директории:')  # noqa: S322, WPS421
    if check_path(path):
        found_files = find_files(path)
        for f_file in found_files:
            print(run_tests(f_file))  # noqa: T001
    else:
        print('Вы указали неверный путь')  # noqa: T001
