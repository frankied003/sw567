import unittest

from triangleCheck import classify_triangle


class TestTriangles(unittest.TestCase):
    def rightTriangleTest(self):
        self.assertEqual(classify_triangle(3, 4, 5), "RightTriangle")
        self.assertEqual(classify_triangle(5, 5, 5), "RightTriangle")

    def equalTriangleTest(self):
        self.assertEqual(classify_triangle(5, 5, 5), "Equilateral")

    def invalidTriangleTest(self):
        self.assertEqual(classify_triangle(10, 2, 1), "InvalidTriangle")
        self.assertEqual(classify_triangle(-2, 2, 1), "InvalidTriangle")
        self.assertNotEqual(classify_triangle(2.2, 2, 2), "InvalidTriangle")

    def ScaleneTriangleTest(self):
        self.assertEqual(classify_triangle(1, 2, 3), "ScaleneTriangle")
        self.assertNotEqual(classify_triangle(4, 4, 5), "ScaleneTriangle")

    def testIsosceles(self):
        self.assertEqual(classify_triangle(2, 2, 4), "IsocelesTriangle")
        self.assertEqual(classify_triangle(10, 5, 5), "IsocelesTriangle")
        self.assertNotEqual(classify_triangle(2, 5, 4), "IsocelesTriangle")


if __name__ == "__main__":
    print("Running these test, gimme a millisec")
    unittest.main()
