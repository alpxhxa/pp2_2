# ex 01 (*args)
def sum_numbers(*args):
    print(sum(args))

sum_numbers(1, 2, 3, 4)


# ex 02 (*args)
def print_all(*args):
    for item in args:
        print(item)

print_all("apple", "banana", "cherry")


# ex 03 (**kwargs)
def show_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

show_info(name="Alex", age=18)


# ex 04 (*args + **kwargs)
def combined(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

combined(1, 2, 3, name="John", city="NY")


# ex 05 (**kwargs)
def build_profile(**kwargs):
    return kwargs

profile = build_profile(username="alpha", level=10)
print(profile)