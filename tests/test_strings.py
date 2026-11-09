"""Unit tests for text_toolkit.strings using unittest."""

import unittest
from text_toolkit.strings import slugify, is_palindrome, word_count, reverse_words


class TestSlugify(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(slugify("Hello World!"), "hello-world")

    def test_multiple_spaces(self):
        self.assertEqual(slugify("  Python  is Great  "), "python-is-great")

    def test_punctuation_stripped(self):
        self.assertEqual(slugify("What's up, doc?"), "whats-up-doc")

    def test_empty(self):
        self.assertEqual(slugify(""), "")


class TestIsPalindrome(unittest.TestCase):

    def test_simple(self):
        self.assertTrue(is_palindrome("racecar"))

    def test_with_spaces(self):
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))

    def test_not_palindrome(self):
        self.assertFalse(is_palindrome("hello"))

    def test_case_insensitive(self):
        self.assertTrue(is_palindrome("RaceCar"))

    def test_punctuation_ignored(self):
        self.assertTrue(is_palindrome("Was it a car or a cat I saw?"))


class TestWordCount(unittest.TestCase):

    def test_two_words(self):
        self.assertEqual(word_count("hello world"), 2)

    def test_empty(self):
        self.assertEqual(word_count(""), 0)

    def test_multiple_spaces(self):
        self.assertEqual(word_count("one   two    three"), 3)


class TestReverseWords(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(reverse_words("hello world"), "world hello")

    def test_three_words(self):
        self.assertEqual(reverse_words("one two three"), "three two one")

    def test_single_word(self):
        self.assertEqual(reverse_words("hello"), "hello")


if __name__ == "__main__":
    unittest.main()