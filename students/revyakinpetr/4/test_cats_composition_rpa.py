# -*- coding: utf-8 -*-

# type: ignore  # noqa E800

import os
import shutil
import subprocess  # noqa: S404
import unittest

from cats_composition_rpa import CatProcessor, main
from cats_direct_rpa import fetch_cat_fact, fetch_cat_image, save_cat


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
        cat_processor = CatProcessor(
            fetch_text=fetch_cat_fact,
            fetch_image=fetch_cat_image,
            process_text_and_image=save_cat,
        )

        fact_path = '{0}/cat_{1}_fact.txt'.format(self.temp, self.index)
        if os.path.exists(fact_path):
            os.remove(fact_path)

        main(
            self.index,
            process_cat=cat_processor,
            show_information=print,  # noqa: T002
        )

        assert os.path.exists(fact_path)

    def test_integration(self):
        """Integration test."""
        str_command = self.str_format.format(self.integration_arg)
        subprocess_res = subprocess.call(str_command, shell=True)  # noqa: S602, E501
        assert subprocess_res == 0


if __name__ == '__main__':
    unittest.main()
