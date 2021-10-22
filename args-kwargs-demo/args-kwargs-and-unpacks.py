# concatenate.py
def concatenate(**kwargs):
    result = ""
    print("kwargs is dict\n", kwargs)
    print("kwargs dict values \n", list(kwargs.values()))
    # Iterating over the Python kwargs dictionary
    for arg in kwargs.values():
        result += arg+' '
    return result


print("[kwargs]")

obj = concatenate(
    a="Real",
    b="Python",
    c="Is",
    d="Great",
    e="!"
)

print(obj)

print()


def my_sum(*args: any) -> any:
    """Sum of all given numbers

    Arguments:
    *args - number, list, tuple
    """
    print("args is tuple\n", args)
    # Iterating over the Python args tuple
    return sum(args)


print("[args]")
print(f"Sum = {my_sum(1, 2, 3)}")

print()

# Dicts and unpacks
# '*' unpacks iterables, such as list, tuple
# '**' unpacks dictionaries

print("[Unpacks]")
my_first_dict = {"A": 1, "B": 2}
my_second_dict = {"C": 3, "D": 4}
my_merged_dict = {**my_first_dict, **my_second_dict}

print(my_first_dict)
print(my_second_dict)
print(my_merged_dict)

print()

print(f"Sum = {my_sum(*[1,2,3], *[4,5,6])}")
print(f"Sum = {my_sum(*(1,2,3), *(4,5,6))}")

print()

print([*'Bala'])

tupla = (1, 'Pedro', 2, 'Reis')
print([*tupla])
