import math


def calculate_area(a, b, c):

    if not (a + b > c and a + c > b and b + c > a):
        return None


    p = (a + b + c) / 2


    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return area


def are_triangles_equal(sides1, sides2):

    if len(sides1) != 3 or len(sides2) != 3:
        return "Foul!!!"


    if any(side <= 0 for side in sides1) or any(side <= 0 for side in sides2):
        return "Foul!!!"


    area1 = calculate_area(*sides1)
    area2 = calculate_area(*sides2)


    if area1 is None or area2 is None:
        return "Foul!!!"


    if math.isclose(area1, area2, rel_tol=1e-9):
        return "Equal"
    else:
        return "Foul!!!"



sides_triangle1 = (6, 8, 10)
sides_triangle2 = (6, 8, 10)


result = are_triangles_equal(sides_triangle1, sides_triangle2)
print(result)
