def invalid_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return True
    if a + b <= c and b + c <= a and c + a <= b:
        return True
    return False


def classify_triangle(a, b, c):
    if invalid_triangle(a, b, c):
        return "InvalidTriangle"
    elif a == b and b == c:
        return "EquilateralTriangle"
    elif a * a + b * b == c * c:
        return "RightTriangle"
    elif b * b + c * c == a * a:
        return "RightTriangle"
    elif c * c + a * a == b * b:
        return "RightTriangle"
    elif a != b and b != c and a != c:
        return "ScaleneTriangle"
    else:
        return "IsocelesTriangle"


classify_triangle(1, 2, 3)
