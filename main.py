"""Главный модуль проекта."""

from utils import sum_even


def greet(name: str) -> str:
    """Вернуть приветствие для имени."""
    return f"Hello, {name}! Welcome!"


if __name__ == "__main__":
    print(greet("Git"))
    print(sum_even([1, 2, 3, 4]))
