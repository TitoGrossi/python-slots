from dataclasses import dataclass


@dataclass(slots=True)
class DC:
    a: int
    b: str


# @dataclass(slots=True)
# class Parent1:
#     a: int
#     b: str


# @dataclass(slots=True)
# class Parent2:
#     c: int
#     d: str


# @dataclass(slots=True)
# class Child(Parent1, Parent2):
#     """"""


def main():
    print(DC(a=1, b="a"))


if __name__ == "__main__":
    main()
