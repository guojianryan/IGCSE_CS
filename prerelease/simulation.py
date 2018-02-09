import os

class Simulation:
    def __init__(self):
        self._input = input

    def restore(self):
        return self._input

    def simulate_code_reading(self):
        def read_code():
            cow_codes = None
            with open(os.path.join(os.path.join(os.getcwd(), "prerelease/codes.in"))) as file:
                cow_codes = file.readlines()
            for code in cow_codes:
                yield code

        cows_from_file = read_code()

        def input_cows(msg):
            return next(cows_from_file).strip()

        return input_cows

    def simulate_yield_reading(self):
        def read_yield():
            yields = None
            with open(os.path.join(os.path.join(os.getcwd(), "prerelease/yields.in"))) as file:
                yields = file.readlines()
            for y in yields:
                yield y

        yield_from_file = read_yield()

        def input_yield(msg):
            return next(yield_from_file).strip()

        return input_yield