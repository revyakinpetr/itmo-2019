# -*- coding: utf-8 -*-

from typing import Callable, Tuple

from requests.packages import urllib3

# We reuse implementation from the direct version:
from cats_direct_rpa import (
    create_parser,
    fetch_cat_fact,
    fetch_cat_image,
    save_cat,
)


class CatProcessor(object):
    """

    Knows exactly how to process cats.

    Only uses composition.

    """

    def __init__(
        self,
        fetch_text: Callable[[], str],
        fetch_image: Callable[[], Tuple[str, urllib3.response.HTTPResponse]],
        process_text_and_image: Callable[[int, str, Tuple[str, urllib3.response.HTTPResponse]], None],  # noqa: E501, WPS221
    ):
        """Saves dependencies into internal state.

        Args:
            fetch_text: Def fetch text.
            fetch_image: Def fetch img.
            process_text_and_image: Def process txt img.

        """
        self._fetch_text = fetch_text
        self._fetch_image = fetch_image
        self._process_text_and_image = process_text_and_image

    def __call__(self, index: int):
        """Runs the process of cat downloading.

        Args:
            index: Index of cats.

        Returns:
            Return __call__.

        """
        return self._process_text_and_image(
            index,
            self._fetch_text(),
            self._fetch_image(),
        )


def main(
    cats_to_fetch: int,
    process_cat: CatProcessor,
    show_information: Callable[[str], None],
):
    """Fetches cats and saves the into temp folder.

    Args:
        cats_to_fetch: Number of cats.
        process_cat: Cat Processor class.
        show_information: Def for showing information.

    """
    if not cats_to_fetch:
        show_information('No cats :(')
        return

    for cat_index in range(1, cats_to_fetch + 1):
        process_cat(cat_index)
    show_information('Cats downloaded!')


if __name__ == '__main__':
    # Building dependencies:
    cat_processor = CatProcessor(fetch_cat_fact, fetch_cat_image, save_cat)

    # Building our main:
    main(
        create_parser().parse_args().count,
        process_cat=cat_processor,
        show_information=print,  # noqa: T002
    )
