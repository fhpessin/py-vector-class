import math


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    # ---------------- MAGIC METHODS ---------------- #

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        # Multiplicação por número → retorna novo Vector
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)

        # Multiplicação por Vector → retorna dot product
        if isinstance(other, Vector):
            return round((self.x * other.x) + (self.y * other.y), 4)

        raise TypeError("Multiplication allowed only with int, float, or Vector.")

    # ---------------- CLASSMETHOD ---------------- #

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple, end_point: tuple) -> "Vector":
        x = end_point[0] - start_point[0]
        y = end_point[1] - start_point[1]
        return cls(x, y)

    # ---------------- VECTOR PROPERTIES ---------------- #

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: "Vector") -> int:
        dot = self * other
        len1 = self.get_length()
        len2 = other.get_length()

        if len1 == 0 or len2 == 0:
            return 0

        cos_a = dot / (len1 * len2)
        cos_a = max(min(cos_a, 1), -1)  # evitar erros numéricos

        angle = math.degrees(math.acos(cos_a))
        return round(angle)

    def get_angle(self) -> int:
        # Ângulo relativo ao eixo Y positivo
        base_vector = Vector(0, 1)
        return self.angle_between(base_vector)

    def rotate(self, degrees: int) -> "Vector":
        rad = math.radians(degrees)
        new_x = self.x * math.cos(rad) - self.y * math.sin(rad)
        new_y = self.x * math.sin(rad) + self.y * math.cos(rad)
        return Vector(new_x, new_y)

    # ---------------- DEBUG REPRESENTATION ---------------- #

    def __repr__(self) -> str:
        return f"Vector(x={self.x}, y={self.y})"
