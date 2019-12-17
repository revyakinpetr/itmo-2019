# -*- coding: utf-8 -*-

# type: ignore  # noqa: E800

import os
import shutil
import subprocess  # noqa: S404
import unittest

import pytest

from cats_direct_rpa import (
    create_parser,
    fetch_cat_fact,
    fetch_cat_image,
    save_cat,
)


class TestCatsDirect(unittest.TestCase):  # noqa: WPS230
    """Unittest class for cats_direct_rpa."""

    def setUp(self):
        """Set up test case."""
        self.http_error_text = 'HTTP fail'
        self.temp = 'temp'
        if not os.path.exists(self.temp):
            os.mkdir(self.temp)
        self.args = ['--count', '4']
        self.image_formats = ['jpg', 'jpeg', 'gif', 'png']
        self.image_name = ['students/revyakinpetr/4/test_cat_image', 'jpg']
        self.save_params = {
            'index': 4,
            'fact': 'test fact',
            'image_path': '{0}.{1}'.format(*self.image_name),
        }
        self.str_format = 'python students/revyakinpetr/4/cats_direct_rpa.py {0}'  # noqa: E800, E501
        self.integration_arg = '--count=2'

    def tearDown(self):
        """Tear down test case."""
        shutil.rmtree(self.temp)

    def test_parse_args(self):
        """Test parse arguments."""
        parse_result = create_parser().parse_args(self.args)
        assert parse_result.count == int(self.args[1])

    @pytest.mark.remote_data
    def test_fetch_cat_fact(self):
        """Test fatch cat fact."""
        try:
            cats_fact = fetch_cat_fact()
        except Exception:
            self.fail(self.http_error_text)

        assert cats_fact

    @pytest.mark.remote_data
    def test_fetch_cat_image(self):
        """Test fatch cat image."""
        try:
            cat_image = fetch_cat_image()
        except Exception:
            self.fail(self.http_error_text)

        assert len(cat_image) == 2
        assert cat_image[0] in self.image_formats

    def test_save_cat(self):
        """Test save cat fact and image."""
        assert os.path.isfile(self.save_params['image_path'])

        with open(self.save_params['image_path'], 'rb') as test_image:
            save_cat(
                index=self.save_params['index'],
                fact=self.save_params['fact'],
                image=(self.image_name[1], test_image),
            )

        fact_path = 'temp/cat_{0}_fact.txt'.format(self.save_params['index'])
        with open(fact_path, 'r') as fact:
            assert fact.read() == self.save_params['fact']

        image_path = 'temp/cat_{0}_image.{1}'.format(
            self.save_params['index'],
            self.image_name[1],
        )
        with open(image_path, 'rb') as img:
            assert img.read()

    def test_integration(self):
        """Integration test."""
        str_command = self.str_format.format(self.integration_arg)
        subprocess_res = subprocess.call(str_command, shell=True)  # noqa: S602
        assert subprocess_res == 0


if __name__ == '__main__':
    unittest.main()
