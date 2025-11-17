from __future__ import annotations
import math
from typing import Union, Tuple


class Vector:
    def __init__(self, coord_x: float, coord_y: float) -> None:
        self.x = round(coord_x, 2)
        self.y = round(coord_y, 2)

    def __add__(self, other: Vector) -> Vector:
        result_x = self.x + other.x
        result_y = self.y + other.y
        return Vector(result_x, result_y)

    def __sub__(self, other: Vector) -> Vector:
        result_x = self.x - other.x
        result_y = self.y - other.y
        return Vector(result_x, result_y)

    def __mul__(
        self, value: Union[float, Vector]
    ) -> Union[float, Vector]:
        if isinstance(value, Vector):
            dot_product = (self.x * value.x) + (self.y * value.y)
            return dot_product

        result_x = self.x * value
        result_y = self.y * value
        return Vector(round(result_x, 2), round(result_y, 2))

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: Tuple[float, float],
        end_point: Tuple[float, float],
    ) -> Vector:
        delta_x = end_point[0] - start_point[0]
        delta_y = end_point[1] - start_point[1]
        return cls(delta_x, delta_y)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)

        norm_x = self.x / length
        norm_y = self.y / length
        return Vector(round(norm_x, 2), round(norm_y, 2))

    def angle_between(self, other: Vector) -> int:
        dot_product = self * other
        length_product = self.get_length() * other.get_length()

        if length_product == 0:
            return 0

        cosine_angle = dot_product / length_product
        cosine_angle = max(min(cosine_angle, 1), -1)

        degrees_angle = math.degrees(math.acos(cosine_angle))
        return int(round
