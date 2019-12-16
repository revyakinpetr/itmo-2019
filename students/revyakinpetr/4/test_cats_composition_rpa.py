# -*- coding: utf-8 -*-

import os
import shutil
import subprocess  # noqa: S404
import unittest

import cats_composition_rpa


class TestCatsComposition(unittest.TestCase):
    """Unittest class for cats composition."""

    def setUp(self):
        """Set up test case."""
        self.index = 5
        self.temp = 'temp'
        if not os.path.exists(self.temp):
            os.mkdir(self.temp)
        self.str_format = 'python students/revyakinpetr/4/cats_composition_rpa.py {0}'  # noqa: E800, E501
        self.integration_arg = '--count=2'

    def tearDown(self):
        """Tear down test case."""
        shutil.rmtree(self.temp)

    def test_main(self):
        """Test main function."""
        cat_processor = cats_composition_rpa.CatProcessor(
            fetch_text=cats_composition_rpa.fetch_cat_fact,
            fetch_image=cats_composition_rpa.fetch_cat_image,
            process_text_and_image=cats_composition_rpa.save_cat,
        )

        fact_path = '{0}/cat_{1}_fact.txt'.format(self.temp, self.index)
        if os.path.exists(fact_path):
            os.remove(fact_path)

        cats_composition_rpa.main(
            self.index,
            process_cat=cat_processor,
            show_information=print,  # noqa: T002
        )

        self.assertTrue(os.path.exists(fact_path))

    def test_integration(self):
        """Integration test."""
        str_command = self.str_format.format(self.integration_arg)
        subprocess_res = subprocess.call(str_command, shell=True)  # noqa: S602, E501
        self.assertEqual(subprocess_res, 0)


if __name__ == '__main__':
    unittest.main()
