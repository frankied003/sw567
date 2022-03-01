# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework


class TestTriangles(unittest.TestCase):
    """
    Tests for running the traiangles program
    """

    # define multiple sets of tests as functions with names that begin

    def test_right_triangle(self):
        """
        Testing for right triangle
        """
        self.assertEqual(
            classifyTriangle(3, 4, 5), "Right", "3,4,5 is a Right triangle"
        )
        self.assertEqual(
            classifyTriangle(5, 3, 4), "Right", "5,3,4 is a Right triangle"
        )
        self.assertEqual(
            classifyTriangle(4, 5, 3), "Right", "4,5,3 is a Right triangle"
        )
        self.assertNotEqual(
            classifyTriangle(5, 5, 5), "Right", "5,5,5 is not a Right triangle"
        )
        self.assertNotEqual(
            classifyTriangle(1, 5, 20), "Right", "1,5,20 is not a Right triangle"
        )

    def test_equil_triangle(self):
        """
        Testing for equilateral triangle
        """
        self.assertEqual(
            classifyTriangle(1, 1, 1), "Equilateral", "1,1,1 should be equilateral"
        )
        self.assertEqual(
            classifyTriangle(4, 4, 4), "Equilateral", "4,4,4 should be equilateral"
        )
        self.assertNotEqual(
            classifyTriangle(1, 4, 4), "Equilateral", "1,4,4 should not be equilateral"
        )
        self.assertNotEqual(
            classifyTriangle(3, 4, 5), "Equilateral", "3,4,5 should not be equilateral"
        )

    def test_scalene_triangle(self):
        """
        Testing for equilateral triangle
        """
        self.assertEqual(
            classifyTriangle(4, 2, 3), "Scalene", "4, 2, 3 should be scalene"
        )
        self.assertEqual(
            classifyTriangle(5, 8, 9), "Scalene", "5,8,9 should be scalene"
        )
        self.assertNotEqual(
            classifyTriangle(1, 4, 4), "Scalene", "1,4,4 should not be scalene"
        )
        self.assertNotEqual(
            classifyTriangle(3, 4, 5), "Scalene", "3,4,5 should not be scalene"
        )

    def test_isoceles_triangle(self):
        """
        Testing for equilateral triangle
        """
        self.assertEqual(
            classifyTriangle(1, 2, 2), "Isoceles", "1,2,2 should be Isoceles"
        )
        self.assertEqual(
            classifyTriangle(8, 5, 8), "Isoceles", "8,5,8 should be Isoceles"
        )
        self.assertNotEqual(
            classifyTriangle(2, 4, 3), "Isoceles", "2,4,3 should not be Isoceles"
        )
        self.assertNotEqual(
            classifyTriangle(3, 4, 5), "Isoceles", "3,4,5 should not be Isoceles"
        )


if __name__ == "__main__":
    print("Running unit tests")
    unittest.main()
