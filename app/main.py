import math


class Vector:
    def __init__(self, coord_x: float, coord_y: float) -> None:
        self.x = round(coord_x, 2)
        self.y = round(coord_y, 2)

    def __add__(self, other_vector: "Vector") -> "Vector":
        return Vector(
            self.x + other_vector.x,
            self.y + other_vector.y,
        )

    def __sub__(self, other_vector: "Vector") -> "Vector":
        return Vector(
            self.x - other_vector.x,
            self.y - other_vector.y,
        )

    def __mul__(self, value: float | "Vector") -> float | "Vector":
        if isinstance(value, Vector):
            return (
                self.x * value.x
                + self.y * value.y
            )

        return Vector(
            round(self.x * value, 2),
            round(self.y * value, 2),
        )

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: tuple[float, float],
        end_point: tuple[float, float],
    ) -> "Vector":
        start_x, start_y = start_point
        end_x, end_y = end_point
        return cls(end_x - start_x, end_y - start_y)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        return Vector(
            round(self.x / length, 2),
            round(self.y / length, 2),
        )

    def angle_between(self, other_vector: "Vector") -> int:
        dot_product = self * other_vector
        magnitude = self.get_length() * other_vector.get_length()
        cosine_angle = dot_product / magnitude

        angle_deg = math.degrees(math.acos(cosine_angle))
        return round(angle_deg)

    def get_angle(self) -> int:
        reference = Vector(0, 1)
        return self.angle_between(reference)

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)

        new_x = (
            self.x * math.cos(radians)
            - self.y * math.sin(radians)
        )
        new_y = (
            self.x * math.sin(radians)
            + self.y * math.cos(radians)
        )

        return Vector(round(new_x, 2), round(new_y, 2))

    def __repr__(self) -> str:
        return f"Vector(x={self.x}, y={self.y})"
