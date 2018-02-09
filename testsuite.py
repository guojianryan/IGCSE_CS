import os
import glob
import timeit

class TestCase:
    def __init__(self, file_name, func):
        self._func = func
        self._file_name = file_name
        self._inputs = None
        self._actual = None
        self._expected = None
        self._result = True

    @property
    def inputs(self):
        return self._inputs

    @inputs.setter
    def inputs(self, value):
        self._inputs = value

    @property
    def actual(self):
        return self._actual

    @actual.setter
    def actual(self, value):
        self._actual = value

    @property
    def expected(self):
        return self._expected

    @expected.setter
    def expected(self, value):
        self._expected = value.rstrip("\n")

    def run(self):
        start = timeit.default_timer()
        self.actual = self._func(*self.inputs)
        stop = timeit.default_timer()
        print("File: ", self._file_name)
        print("Run time: " + str((stop - start)))
        self.result = self.expected == str(self.actual)
        if not self.result:
            print("Test Case Failed: \tExpected: {0}, Actual: {1}".format(self.expected,self.actual))
        return self.result

class TestSuite:
    def __init__(self, year, level, question_number, func):
        self.year = year
        self.level = level
        self.question_number = question_number
        self.func = func
        self.cases = list()
        self.failed = 0
        self.passed = 0

    def start(self):
        folder = os.path.join(os.path.join(os.getcwd(), str(self.year)),"{0}{1}".format(self.level, self.question_number))
        print(folder)
        for input_file_name in glob.glob(os.path.join(folder, '*.in')):
            c = TestCase(input_file_name, self.func)
            with open(input_file_name) as input_file_handle:
                inputs = [line.strip().split() for line in input_file_handle if line.strip()!=""]
                c.inputs = inputs

            output_file_name = input_file_name[0:-2] + "out"
            with open(output_file_name) as output_file_handle:
                c.expected = output_file_handle.readline()

            if c.run() == True:
                self.passed = self.passed + 1
            else:
                self.failed = self.failed + 1

        print("passed: {0}, failed: {1}".format(self.passed, self.failed))