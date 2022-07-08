import timeit
from classes import Slots, NoSlots

from pympler.asizeof import asizeof


COUNT_NUMBER = 1000000
REPEAT_NUMBER = 10


def main():
    """"""
    slotted_time = sum(timeit.repeat("c = Slots(1, 'a'); s = c.a + 1", number=COUNT_NUMBER, globals=globals(
    ), repeat=REPEAT_NUMBER))/REPEAT_NUMBER
    non_slotted_time = sum(timeit.repeat(
        "c = NoSlots(1, 'a'); s = c.a + 1", number=COUNT_NUMBER, globals=globals(), repeat=REPEAT_NUMBER))/REPEAT_NUMBER

    print(
        f"Performance improvement: {100*(non_slotted_time - slotted_time)/non_slotted_time:.2f}%")

    size_slot = asizeof(Slots(a=1, b="a"))
    size_no_slot = asizeof(NoSlots(a=1, b="a"))

    print(
        f"Memory usage improvement: {100*(size_no_slot - size_slot)/size_no_slot:.2f}%")


if __name__ == "__main__":
    main()
