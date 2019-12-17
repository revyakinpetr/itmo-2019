# -*- coding: utf-8 -*-

"""Test framework."""
import glob
import os
from importlib import util as importutil

TEST_PATH_FORMAT = '{path}/test_*.py'
TEST_INFO_FORMAT = '{filename}/{test_name} - {msg}'


def find_files(path):
    """Find and return python test files in path.

    Args:
        path: Path to files.

    Returns:
        List of files.

    """
    if path == '':
        path = '.'
    if os.path.exists(path):
        return glob.glob(TEST_PATH_FORMAT.format(path=path))
    return []


def get_module_spec(filename):
    """Return module spec.

    Args:
        filename: Name of file.

    Returns:
        module spec.

    """
    return importutil.spec_from_file_location(
        filename[:-3], filename,
    )


def get_test_module(module):
    """Geting test module.

    Args:
        module: Spec of module.

    Returns:
        module.

    """
    return importutil.module_from_spec(module)


def get_tests(module_spec, test_module):
    """Get tests from file.

    Args:
        module_spec: Module spec.
        test_module: Test module object.

    Returns:
        List of tests.

    """
    module_spec.loader.exec_module(test_module)
    return [
        test for test in dir(test_module)  # noqa: WPS421
        if test.startswith('test_')
    ]


def exec_test(test_name, test_module):
    """Execut test.

    Args:
        test_name: Name of test.
        test_module: Test module object.

    Returns:
        message ok or fail.

    """
    try:
        vars(test_module)[test_name]()  # noqa: WPS421
    except Exception:
        return 'fail'
    return 'ok'


def show_info(filename, test_name, msg):
    """Print result in command line.

    Args:
        filename: File name.
        test_name: Name of test.
        msg: ok or fail message.

    """
    print_text = TEST_INFO_FORMAT.format(
        filename=filename,
        test_name=test_name,
        msg=msg,
    )
    print(print_text)  # noqa: T001


def run_tests(test_dir=''):  # noqa: WPS210
    """Runing test in directory.

    Args:
        test_dir: User's test directory

    """
    found_files = find_files(test_dir)

    for found_file in found_files:
        module_spec = get_module_spec(found_file)
        test_module = get_test_module(module_spec)
        tests = get_tests(module_spec, test_module)

        for test in tests:
            exec_res = exec_test(test, test_module)
            show_info(found_file, test, exec_res)
