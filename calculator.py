def add(a: int, b: int) -> int:
feature/conflict-b
    print(f"[debug] adding {a} and {b}")
    """Return the sum of two integers."""
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("add expects integers")
 main
    return a + b

def main():
    print("add(2,3) =", add(2,3))

if __name__ == "__main__":
    main()
