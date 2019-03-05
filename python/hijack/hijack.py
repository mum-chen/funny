def random_import():
    def hijack_volunteer():
        global Volunteer
        from volunteer import Volunteer as _V
        Volunteer = _V

    def hijack_sacrifice():
        global Sacrifice
        from sacrifice import Sacrifice as _S
        Sacrifice = _S

    def hijack_warrior():
        global Warrior
        from warrior import Warrior as _W
        Warrior = _W

    hijack_list = [
        hijack_volunteer,
        hijack_sacrifice,
        hijack_warrior,
    ]

    import random
    random.shuffle(hijack_list)
    for hijack in hijack_list:
        hijack()

if __name__ == "__main__":
    random_import()

    print("Volunteer say:")
    v = Volunteer()
    v.say_name()

    print("Warrior say:")
    w = Warrior()
    w.say_name()

    print("Sacrifice say:")
    s = Sacrifice()
    s.say_name()
