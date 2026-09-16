"""Главный модуль проекта."""


def greet(name: str) -> str:
    """Вернуть приветствие для имени."""
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(greet("Git"))
