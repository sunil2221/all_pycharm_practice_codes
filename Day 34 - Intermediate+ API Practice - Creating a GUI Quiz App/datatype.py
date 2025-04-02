age: int
name: str
is_human: bool
height: float

# (input type) -> output type
def even(n: int) -> str:
    if n % 2 == 0:
        return "even number"
    else:
        return "odd number"


print(even(3))
# print(even("three"))