def fibonacciSeries(num: int) -> int:
    if num == 0:
        return 0
    if num == 1:
        return 1
    return fibonacciSeries(num - 1) + fibonacciSeries(num - 2)


if __name__ == "__main__":
    print(fibonacciSeries(9))
