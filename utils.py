"""Вспомогательные функции."""


def sum_even(numbers: list[int]) -> int:
    """Сумма чётных чисел списка."""
    return sum(n for n in numbers if n % 2 == 0)
