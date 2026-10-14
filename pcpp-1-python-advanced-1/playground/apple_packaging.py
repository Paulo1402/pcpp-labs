import random


class Apple:
    count: int = 0
    total_weight: float = 0

    def __init__(self, weight):
        self._weight = weight

        Apple.count += 1
        Apple.total_weight += weight


class ApplePackaging:
    MAX_WEIGHT = 0.2
    MIN_WEIGHT = 0.5

    def __init__(self, apple_count, max_apple_weight):
        self._apple_count = apple_count
        self._max_apple_weight = max_apple_weight

        self._apples = []

    def pack(self):
        try:
            while Apple.count < self._apple_count:
                if Apple.total_weight >= self._max_apple_weight:
                    raise RuntimeError("Pack is full. Over capacity")

                weight = self._random_weight()
                apple = Apple(weight)

                self._apples.append(apple)

            print("Packing finished!")
        except RuntimeError:
            print("Over capacity! Stopping packing!")
        finally:
            print(f"Apples: {Apple.count}")
            print(f"Apples weight: {Apple.total_weight}")

    def _random_weight(cls):
        return random.uniform(cls.MAX_WEIGHT, cls.MIN_WEIGHT)


if __name__ == "__main__":
    packaging = ApplePackaging(apple_count=1000, max_apple_weight=400)
    packaging.pack()
