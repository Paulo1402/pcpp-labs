from datetime import datetime


def exec_time(func):
    def inner(*args, **kwargs):
        start = datetime.now()
        print(f'Start time: {start.strftime("%Y-%m-%d %H:%M:%S")}')

        result = func(*args, **kwargs)

        end = datetime.now()
        print(f'End time: {end.strftime("%Y-%m-%d %H:%M:%S")}')

        diff = end - start
        print(f"{func.__name__} took {diff.total_seconds():.6f} to execute")

        return result

    return inner


@exec_time
def fibonnaci(n):
    sequence = [0, 1]
    if n <= 0:
        return []
    elif n == 1:
        return [0]

    for _ in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])

    return sequence


if __name__ == "__main__":
    print(fibonnaci(10))
