def functiontest(*args):
    print("args tuple:", args)

functiontest(1, 2, 3)


def test(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)


test(
    "thisisanargstring",
    name="Talha",
    role="student",
    teacher="ali"
)

