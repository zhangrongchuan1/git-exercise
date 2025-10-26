from exercise1 import Vector
from exercise2 import Point2D


class Rectangle:
    def __init__(self, lower_left: Point2D, dx: float, dy: float) -> None:
        self._lower_left = lower_left
        self._dx = dx
        self._dy = dy

    def corner(self, i: int) -> Point2D:
        assert i < 4
        result = Point2D(self._lower_left.x, self._lower_left.y)
        result += Vector([
            self._dx if self._is_idx_on_right_edge(i) else 0.0,
            self._dy if self._is_idx_on_upper_edge(i) else 0.0
        ])
        return result

    @property
    def lower_left(self) -> Point2D:
        return self._lower_left

    @property
    def upper_right(self) -> Point2D:
        return self.corner(3)
        
            
    def contains(self, point: Point2D, tolerance: float = 0.0) -> bool:# Task B
        # Task A: remove duplication by defining a function
        #         that checks if a value is within an interval
        #         and reuse that here.
        ll_px = point.x - self._lower_left.x
        ll_py = point.y - self._lower_left.y
        return (-tolerance <= ll_px <= self._dx + tolerance) and \
               (-tolerance <= ll_py <= self._dy + tolerance)

    def _is_idx_on_upper_edge(self, i: int) -> bool:
        return i in [2, 3]
    
    def _is_idx_on_right_edge(self, i: int) -> bool:
        return i in [1, 3]

    # def is_in_interval(...) -> bool: # Task A
    @staticmethod
    def _is_in_interval(value: float, lower: float, upper: float, tolerance: float = 0.0) -> bool:
        return (lower - tolerance) <= value <= (upper + tolerance)

def test_rectangle_contains_exact() -> None:
    rectangle = Rectangle(lower_left=Point2D(1.0, 2.0), dx=2.5, dy=1.5)
    for i in range(4):
        assert rectangle.contains(rectangle.corner(i))


def test_rectangle_contains_tolerance() -> None:
    rectangle = Rectangle(lower_left=Point2D(1.0, 2.0), dx=2.5, dy=1.5)
    lower_left = rectangle.corner(0)
    lower_right = rectangle.corner(1)
    upper_left = rectangle.corner(2)
    upper_right = rectangle.corner(3)

    assert rectangle.contains(lower_left)
    assert rectangle.contains(upper_left)
    assert rectangle.contains(lower_right)
    assert rectangle.contains(upper_right)

    eps = 1e-10
    lower_left -= Vector([eps, eps])
    lower_right += Vector([eps, -eps])
    upper_left += Vector([-eps, eps])
    upper_right += Vector([eps, eps])

    assert not rectangle.contains(lower_left)
    assert not rectangle.contains(upper_left)
    assert not rectangle.contains(lower_right)
    assert not rectangle.contains(upper_right)

    # Task B: make the tests below pass by adding optional tolerance argument to `contains`
    assert not rectangle.contains(lower_left, tolerance=eps/2.0)
    assert not rectangle.contains(upper_left, tolerance=eps/2.0)
    assert not rectangle.contains(lower_right, tolerance=eps/2.0)
    assert not rectangle.contains(upper_right, tolerance=eps/2.0)

    assert rectangle.contains(lower_left, tolerance=eps*2.0)
    assert rectangle.contains(upper_left, tolerance=eps*2.0)
    assert rectangle.contains(lower_right, tolerance=eps*2.0)
    assert rectangle.contains(upper_right, tolerance=eps*2.0)
