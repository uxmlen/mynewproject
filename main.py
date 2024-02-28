# main.py
def add_three(a: int, b: int, c: int) -> int:
    """sum two number"""
    return a + b


def main() -> None:
    """add three number"""
    print("enter three numbers: 3 3 3")
    a, b, c = map(int, input().split())
    res = add_three(a, b, c)
    print(res)


if __name__ == '__main__':
    main()