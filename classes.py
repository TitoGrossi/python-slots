from dataclasses import dataclass


class Slots:
    __slots__ = ("a", "b")

    def __init__(self, a: int, b: str) -> None:
        self.a: int = a
        self.b: str = b

    def dummy(self):
        return f"{self.a} {self.b}"


class NoSlots:
    def __init__(self, a: int, b: str) -> None:
        self.a: int = a
        self.b: str = b

    def dummy(self):
        return f"{self.a} {self.b}"


# @dataclass(slots=True)
# class ParentA:
#     a: int


# @dataclass(slots=True)
# class ParentB:
#     b: int


# class Child(ParentA, ParentB):
#     ""


# if __name__ == "__main__":
#     c = Child()
