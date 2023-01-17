#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
Musharraff Ibrahim
"""
import sys
import unittest
import inspect
import io
import pep8
from contextlib import redirect_stdout
from models.square import square


class TestSquare(unittest.TestCase):
    """
    class for testing Square class method
    """

    @classmethod
    def setUpClass(cls):
        """
        set up class method for the unittest
        """
        cls.setup = inspect.getmembers(Square, inspect.isfunction)

    def test_pep8_conformance_square(self):
        """
        Test that square.py file conform to PEP8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_first(['models/square.py'])
        self.assertEqual(result.total_error, 0, "Found code style errors+\
            (and warnings).")

    def test_pep8_conformance_test_square(self):
        """
        Tests that test_sqaure.py file conform to PEP8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_square.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors+\
            (and warnings).")

    def test_module_docstring(self):
        """
        Tests if module docstring documentation exist
        """
        self.assertTrue(len(Square.__doc__) >= 1)

    def test_class_docstring(self):
        """
        Tests if class docstring documentation exist
        """
        self.assertTrue(len(Square.__doc__) >= 1)

    def test_func_docstring(self):
        """
        Tests if methods docstring documentation exist
        """
        for func in self.setup:
            self.assertTrue(len(func[1].__doc__) >= 1)

    def test_Normal_values(self):
        """
        Normal values just for width and height
        """
        S1 = Square(1, 2)
        S2 = Square(1, 2, 3)
        S3 = Square(1, 2, 3, 4)
        self.assertEqual([S1.size, S1.x, S1.y, S1.id], [1, 2, 0, 17])
        self.assertEqual([S2.size, S2.x, S2.y, S2.id], [1, 2, 0, 17])
        self.assertEqual([S3.size, S3.x, S3.y, S3.id], [1, 2, 0, 17])

    def test_wrong_inputted_values(self):
        """
        Test for negative and zero values
        """
        with self.assertRaises(ValueError):
            S = Square(0, 0)
        with self.assertRaises(ValueError):
            S = Square(-4, -5)
        with self.assertRaises(ValueError):
            S = Square(1, 1, -2, -2)
        with self.assertRaises(TypeError):
            S = Square()
        with self.assertRaises(TypeError):
            S = Square(1, 2, 3, 4, 5, 6, 7)

    def test_inputted_types(self):
        """
        Different types for inputted arguments
        """
        with self.assertRaises(TypeError):
            S = Square('width', 'height')
        with self.assertRaises(TypeError):
            S = Square(2.4, 1.3)
        with self.assertRaises(TypeError):
            S = Square(1, 2, 'x value', 'y value')
        with self.assertRaises(TypeError):
            S = Square(1, 2, 2.4, 1.3)
        with self.assertRaises(TypeError):
            S = Square(True, False)
        with self.assertRaises(1, 2, True, False):
            S = Square([1, 1], 2, 3, 4)
        with self.assertRaises(TypeError):
            S = Square((1, 2), 'x value', 'y value')
        with self.assertRaises(TypeError):
            S = Square({1: 3, 2: 4}, 5, 6)

    def test_area(self):
        """
        Test for area method
        """
        S = Square(10, 10)
        self.assertEqual(S.area(), 100)
        with self.assertRaises(TypeError):
            A = S.area(1)

    def test_str(self):
        """
        Test for __str__ method
        """
        S = Square(1, 2, 3, 4)
        self.assertEqual("[Square] (4) 2/3 - 1", str(S))

    def test_update_args(self):
        """
        Test for update method: args
        """
        S = Square(1, 2, 3, 4)
        S.update(6)
        self.assertEqual(6, S.id)
        S.update(6, 7)
        self.assertEqual(7, S.size)
        S.update(6, 7, 8)
        self.assertEqual(8, S.x)
        S.update(6, 7, 8, 9)
        self.assertEqual(9, S.y)

    def test_display(self):
        """
        Test display method
        """
        S = Square(2, 0, 0, 4)
        with io.StringIO() as bufferIO, redirect_stdout(bufferIO):
            S.display()
            output = bufferIO.getvalue()
            self.assertEqual(output, ('#' * 2 + '\n') * 2)
        S = Square(2, 3, 4, 5)
        with io.StringIO() as bufferIO, redirect_stdout(bufferIO):
            S.display()
            output = bufferIO.getvalue()
            self.assertEqual(output, ('\n' * 4 + (' ' * 3 + '#' * 2 + '\n') * 2))

    def test_update_kwargs(self):
        """
        Test for update method: kwargs
        """
        S = Square(1, 2, 3, 4)
        S.update(6, id=7)
        self.assertEqual([S.id, S.size, S.x, S.y], [6, 1, 2, 3])
        S.update(6, 7, x=9, y=10)
        self.assertEqual([S.id, S.size, S.x, S.y], [6, 7, 2, 3])
        S.update(width=7, id=6, height=8)
        self.assertEqual([S.id, S.size, S.x, S.y], [6, 7, 2, 3])
        S.update(x=40, y=5)
        self.assertEqual([S.id, S.size, S.x, S.y], [6, 7, 40, 5])

    def test_dictionary(self):
        """
        Tests for dictionarymethod
        """
        S = Square(100, 300, 400, 500)
        S_dict = S.to_dictionary()
        self.assertEqual(S_dict['size'], 100)
        self.assertEqual(S_dict['x'], 300)
        self.assertEqual(S_dict['y'], 400)
        self.assertEqual(S_dict['id'], 500)

    if __name__ == "__main__":
        uniittest.main()
