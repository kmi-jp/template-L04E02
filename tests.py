import time

from delay import delay


def test_delay():
    @delay()
    def my_sum(a, b):
        return a + b

    start = time.perf_counter()
    result = my_sum(2, 3)
    duration = time.perf_counter() - start

    assert duration > 1
    assert result == 5


def test_delay_long():
    @delay(seconds=3)
    def my_sum(a, b):
        return a + b

    start = time.perf_counter()
    result = my_sum(2, 3)
    duration = time.perf_counter() - start

    assert duration > 3
    assert result == 5


def test_assure_functools_wraps():
    @delay()
    def my_sum(a, b):
        """Docstring"""
        return a + b

    assert my_sum.__name__ == "my_sum"
    assert my_sum.__doc__ is not None


def test_docstrings():
    assert delay.__doc__ is not None
