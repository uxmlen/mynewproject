# main.py
def add_two(a: int, b: int) -> int:
    """sum two number"""
    return a + b


def main() -> None:
    """add two number"""
    a, b = map(int, input().split())
    res = add_two(a, b)
    print(res)


if __name__ == '__main__':
    main()
