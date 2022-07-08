from classes import Slots, NoSlots


def main():
    # no slots
    c = NoSlots(a=1, b="flajdf")
    print(c.__dict__)
    c.variavel_nova = None
    print(c.__dict__)

    # with slots
    # c = Slots(a=1, b="flajdf")
    # print(c.__dict__)
    # c.loucura_total = None
    # print(c.__dict__)


if __name__ == "__main__":
    main()
